from PySide6.QtGui import QFont, QBrush, QColor, QIcon
from PySide6.QtWidgets import QListWidgetItem


class itemWidget(QListWidgetItem):
    def __init__(self, title, type="microprocessor" or "vehicle"):
        super().__init__()

        self.icon_type = type

        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)

        brush = QBrush(QColor(29, 35, 34, 255))
        brush1 = QBrush(QColor(255, 255, 255, 255))

        self.type = type
        self.setText(title)

        self.setFont(font)

        self.setBackground(brush)
        self.setForeground(brush1)

        icon = QIcon()
        icon.addFile(f"../res/{self.icon_type}.ico")

        self.setIcon(icon)
