from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel


DEFAULT_STYLE = "color: rgb(255, 255, 255);" \
                "background-color: <BG>;" \
                "border-top-right-radius: 5px;" \
                "border-bottom-right-radius: 5px;"

DEFAULT_COLOR = "rgba(49, 206, 51, 200)"
ALARM_COLOR = "rgba(255, 0, 0, 200)"
EXCEPT_COLOR = "rgba(214, 235, 0, 200)"


class infoLabelWidget(QLabel):
    """Animated info label"""
    def __init__(self, parent):
        super().__init__(parent)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)

        self.setFont(font)

        self.setMargin(10)
        self.setObjectName(u"infoLabel")
        self.setGeometry(QRect(0, 0, 185, 45))

        self.setStyleSheet(DEFAULT_STYLE.replace("<BG>", DEFAULT_COLOR))

        self.setText("Placeholder")

        self.hide()

        self.__anim_start = QPropertyAnimation(self, b"geometry")
        self.__anim_hold = QPropertyAnimation(self, b"size")
        self.__anim_end = QPropertyAnimation(self, b"geometry")

        self.__anim_group = QSequentialAnimationGroup()
        self.__anim_group.addAnimation(self.__anim_start)
        self.__anim_group.addAnimation(self.__anim_hold)
        self.__anim_group.addAnimation(self.__anim_end)

        self.__anim_start.setDuration(500)
        self.__anim_hold.setDuration(1000)
        self.__anim_end.setDuration(500)

        self.__anim_start.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.__anim_end.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.__anim_start.setStartValue(QRect(self.x(), self.y(), 0, self.height()))
        self.__anim_start.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))

        self.__anim_end.setStartValue(QRect(self.x(), self.y(), self.width(), self.height()))
        self.__anim_end.setEndValue(QRect(self.x(), self.y(), 0, self.height()))

    def show_message(self, message=None, color=None, wait_time=None):
        """
        :param str message: message to be shown. Must include \n if long message
        :param str color: rgb, rgba, hex color of background. By default - DEFAULT_COLOR
        :param wait_time: hold time in milliseconds. By default - 1000ms / 1s
        """
        self.setStyleSheet(DEFAULT_STYLE.replace("<BG>", DEFAULT_COLOR))
        if wait_time is not None:
            self.__anim_hold.setDuration(wait_time)
        if message is not None:
            self.setText(message)
        if color is not None:
            self.setStyleSheet(DEFAULT_STYLE.replace("<BG>", color))
        self.__anim()

    def __anim(self):
        if self.isHidden():
            self.show()
        self.__anim_group.start()

