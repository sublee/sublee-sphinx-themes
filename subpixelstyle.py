import ConfigParser
import os
import re
import sys

from pygments.style import Style
from pygments.token import *


META_STYLES = {
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
        tmp_styles = {}
        for token, opt in META_STYLES.iteritems():
            color = theme_options.get(opt, '#000000')
            color = re.sub('#(.)(.)(.)$', r'#\1\1\2\2\3\3', color)
            tmp_styles[token] = color
        class SubpixelStyle(Style):
            background_color = 'transparent'
            styles = tmp_styles
        SubpixelStyle.__name__ = '%sStyle' % theme.title()
        return SubpixelStyle


sys.modules[__name__] = ModuleHook(sys.modules[__name__])
