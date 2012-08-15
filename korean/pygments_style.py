# jDoctest pygments style based on flasky style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class KoreanStyle(Style):
    background_color = "#eee"
    default_style = ""

    styles = {
        Comment:                   "#a97",        # class: 'c'
        Comment.Single:            "italic",      # class: 'c1'

        Keyword:                   "#985eaa",     # class: 'k'
        #Keyword.Constant:          "#78c3c0",     # class: 'kc'
        #Keyword.Declaration:       "#ce6049",     # class: 'kd'

        Operator:                  "#9e7da2",     # class: 'o'

        Punctuation:               "#000000",        # class: 'p'

        Name:                      "#000000",        # class: 'n'
        Name.Variable:             "#6d6b85",
        #Name.Attribute:            "#ce6049",     # class: 'na'
        #Name.Builtin:              "#78c3c0",     # class: 'nb'
        #Name.Tag:                  "bold #6d7e9c",# class: 'nt'

        Number:                    "#a56453",     # class: 'm'
        String:                    "#a56453",     # class: 's'
        #String.Escape:             "#9e7da2",     # class: 'se'
        Generic.Output:            "#6c7086",   # class: 'go'
        Generic.Prompt:            "#bdafa0",     # class: 'gp'
    }
