import math
import string
from PyQt6.QtWidgets import QWidget
from styles import Styles

from widgets.themed_widgets.colored_text import ColoredText
from widgets.utility_widgets.horizontal_group import HorizontalGroup


class LabeledWidget(HorizontalGroup):
    def __init__(self, label_text: string, widget: QWidget, spacing: int = Styles.theme.medium_spacing, margins = (math.inf, 0, 0, 0)):
        self.widget: QWidget = widget
        self.label = ColoredText(label_text, Styles.theme.label_color, Styles.theme.label_font_size)

        super().__init__([self.label, self.widget], spacing, margins)

        
        
