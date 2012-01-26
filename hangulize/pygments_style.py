# jDoctest pygments style based on flasky style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class HangulizeStyle(Style):
    background_color = "#333"
    default_style = ""

    styles = {
        Comment:                   "#a97",        # class: 'c'
        Comment.Single:            "italic",      # class: 'c1'

        Keyword:                   "#faec8d",     # class: 'k'
        Keyword.Constant:          "#78c3c0",     # class: 'kc'
        Keyword.Declaration:       "#ce6049",     # class: 'kd'

        Operator:                  "#9e7da2",     # class: 'o'

        Punctuation:               "#999",        # class: 'p'

        Name:                      "#ccc",        # class: 'n'
        Name.Attribute:            "#ce6049",     # class: 'na'
        Name.Builtin:              "#78c3c0",     # class: 'nb'
        Name.Tag:                  "bold #6d7e9c",# class: 'nt'

        Number:                    "#ce6049",     # class: 'm'
        String:                    "#8db269",     # class: 's'
        String.Escape:             "#9e7da2",     # class: 'se'
        Generic.Output:            "bold #568",   # class: 'go'
        Generic.Prompt:            "#78c3c0",     # class: 'gp'
    }
