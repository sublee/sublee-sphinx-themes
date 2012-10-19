import ConfigParser
import os
import re
import sys

from pygments.style import Style
from pygments.token import *


class ModuleHook(object):

    def __init__(self, module):
        self.module = module

    def __getattr__(self, attr):
        if attr.startswith('generate('):
            return self.generate(re.search(r'\((.+)\)$', attr).group(1))
        else:
            return getattr(self.module, attr)

    def generate(self, theme):
        config = ConfigParser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__), theme, 'theme.conf')
        with open(path) as f:
            config.readfp(f)
        theme_options = dict(config.items('options'))
        def replace(match):
            color = theme_options.get(match.group(1), '#000000')
            color = re.sub('#(.)(.)(.)$', '#\1\1\2\2\3\3', color)
            return color
        for token, opt in SubpixelStyle.meta_styles.iteritems():
            color = theme_options.get(opt, '#000000')
            color = re.sub('#(.)(.)(.)$', '#\1\1\2\2\3\3', color)
            SubpixelStyle.styles[token] = color
        SubpixelStyle.__name__ = '%sStyle' % theme.title()
        return SubpixelStyle


class SubpixelStyle(Style):

    background_color = 'transparent'
    meta_styles = {
        Keyword:        'title_color', # class: 'k'
        Operator:       'text_color',  # class: 'o'
        Punctuation:    'text_color',  # class: 'p'
        Name:           'text_color',  # class: 'n'
        Name.Variable:  'title_color', # class: 'nv'
        Number:         'title_color', # class: 'm'
        String:         'title_color', # class: 's'
        Generic.Output: 'text_color',  # class: 'go'
        Generic.Prompt: 'title_color', # class: 'gp'
        Generic.Error:  'vlink_color', # class: 'gr'
    }


sys.modules[__name__] = ModuleHook(sys.modules[__name__])
