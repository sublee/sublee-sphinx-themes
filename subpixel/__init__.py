try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
import os
import re
import sys

from pygments.style import Style
from pygments.token import *


META_STYLES = {
    Keyword:        '{title_color}',        # class: 'k'
    Operator:       '{text_color}',         # class: 'o'
    Punctuation:    '{text_color}',         # class: 'p'
    Name:           '{text_color}',         # class: 'n'
    Name.Variable:  '{title_color}',        # class: 'nv'
    Number:         '{title_color}',        # class: 'm'
    String:         '{title_color}',        # class: 's'
    Generic.Output: '{text_color}',         # class: 'go'
    Generic.Prompt: '{title_color}',        # class: 'gp'
    Generic.Error:  '{vlink_color}',        # class: 'gr'
    Comment:        '{title_color} italic', # class: 'c'
}


class ModuleHook(object):

    def __init__(self, module):
        self.module = module

    def __getattr__(self, attr):
        if attr.startswith('AutoStyle('):
            theme_name = re.search(r'\((.+)\)$', attr).group(1)
            return self.generate_pygments_style(theme_name)
        else:
            return getattr(self.module, attr)

    def generate_pygments_style(self, theme_name):
        config = ConfigParser()
        path = os.path.join(os.path.dirname(__file__), '..',
                            theme_name, 'theme.conf')
        with open(path) as f:
            config.readfp(f)
        theme_options = dict(config.items('options'))
        tmp_styles = {}
        def repl(match):
            opt = match.group(1)
            color = theme_options.get(opt, '#000000')
            color = re.sub('#(.)(.)(.)$', r'#\1\1\2\2\3\3', color)
            return color
        for token, val in META_STYLES.iteritems():
            tmp_styles[token] = re.sub(r'{(.+?)}', repl, val)
        class AutoStyle(Style):
            background_color = 'transparent'
            styles = tmp_styles
        AutoStyle.__name__ = '%sStyle' % theme_name.title()
        return AutoStyle


sys.modules[__name__] = ModuleHook(sys.modules[__name__])
