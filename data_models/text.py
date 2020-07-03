"""This class creates the object structure for Text content"""

from data_models.contents import ContentType, _Content


class Text(_Content):
    """This class creates Text object"""

    def __init__(self, text_str, text_type='', is_bold=False):
        super(Text, self).__init__(ContentType.TEXT)
        self.type = text_type
        self.text_string = text_str
        self.font_style = ''
        self.is_bold = is_bold
