# jDoctest pygments style based on flasky style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class EnergyStyle(Style):
    background_color = ""
    default_style = ""

    styles = {
        Comment:                   "#aa9977", # class: 'c'
        Comment.Single:            "italic",  # class: 'c1'
        Keyword:                   "#4477aa", # class: 'k'
        Operator:                  "#334477", # class: 'o'
        Punctuation:               "#334477", # class: 'p'
        Name:                      "#334477", # class: 'n'
        Name.Variable:             "#4477aa",
        Number:                    "#4477aa", # class: 'm'
        String:                    "#4477aa", # class: 's'
        Generic.Output:            "#334477", # class: 'go'
        Generic.Prompt:            "#4477aa", # class: 'gp'
    }
