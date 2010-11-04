# jDoctest pygments style based on flasky style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class jDoctestStyle(Style):
    background_color = "#fafafa"
    default_style = ""

    styles = {
        Comment:                   "#567",        # class: 'c'
        Comment.Single:            "italic #a97", # class: 'c1'

        Keyword:                   "#925",        # class: 'k'
        Keyword.Constant:          "#45a",        # class: 'kc'
        Keyword.Declaration:       "#a61",        # class: 'kd'

        Operator:                  "#666",        # class: 'o'

        Punctuation:               "#333",        # class: 'p'

        Name:                      "#000",        # class: 'n'
        Name.Attribute:            "#b58",        # class: 'na'
        Name.Builtin:              "#442",        # class: 'nb'
        Name.Tag:                  "bold #45a",   # class: 'nt'

        Number:                    "#b69",        # class: 'm'
        String:                    "#690",        # class: 's'
        Generic.Output:            "bold #568",   # class: 'go'
        Generic.Prompt:            "#876",        # class: 'gp'
    }
