# jDoctest pygments style based on flasky style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class TrueSkillStyle(Style):
    background_color = "transparent"
    default_style = ""

    styles = {
        Comment:                   "#a97",        # class: 'c'
        Comment.Single:            "italic",      # class: 'c1'

        Keyword:                   "#b78e35",     # class: 'k'
        Keyword.Constant:          "#78c3c0",     # class: 'kc'
        Keyword.Declaration:       "#ce6049",     # class: 'kd'

        Operator:                  "#9e9a5f",     # class: 'o'

        Punctuation:               "#c2d76f",     # class: 'p'

        Name:                      "#c8d841",     # class: 'n'
        Name.Attribute:            "#ce6049",     # class: 'na'
        Name.Builtin:              "#78c3c0",     # class: 'nb'
        Name.Tag:                  "bold #f1ebc9",# class: 'nt'

        Number:                    "#d37c59",     # class: 'm'
        String:                    "#8db269",     # class: 's'
        String.Escape:             "#9e7da2",     # class: 'se'
        Generic.Output:            "#7f9574",     # class: 'go'
        Generic.Prompt:            "#569a81",     # class: 'gp'
    }
