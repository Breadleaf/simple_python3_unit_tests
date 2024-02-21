import os
import enum

class STYLE(enum.Enum):
    """
    Enum for the style of the text
    """

    NORMAL = 0
    BOLD = 1
    LIGHT = 2
    ITALIC = 3
    UNDERLINE = 4


class COLOR(enum.Enum):
    """
    Enum for the color of the text
    """

    NONE = 0
    BLACK = 30
    RED = 31
    GREEN = 32 
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37


class ColorFormatBuilder:
    """
    Class to build a colored text stream for posix systems
    """

    def __init__(self):
        """
        Constructor
        """

        self.text = ""

        if os.name == 'posix':
            self.text = "\033[0m"


    def begin():
        """
        Constructor; call this rather than __init__
        """

        return ColorFormatBuilder()


    def setFormat(self, style: STYLE, color: COLOR = COLOR.NONE):
        """
        Set the format of the text
        NOTE: you can stack styles by making two calls to this function, the first with no color and the second with the desired color
        """

        if os.name == 'posix':
            if color == COLOR.NONE:
                self.text += f"\033[{style.value}m"
            else:
                self.text += f"\033[{style.value};{color.value}m"

        return self


    def resetFormat(self):
        """
        Reset the format of the text
        """

        self.setFormat(STYLE.NORMAL)
        return self


    def addText(self, text: str):
        """
        Add text to the current text stream
        """

        self.text += text

        if os.name == 'posix':
            self.text += "\033[0m"

        return self


    def build(self):
        """
        Build the text stream and return it
        """

        return self.text


    def __str__(self):
        """
        Return the text stream
        """

        return self.text
