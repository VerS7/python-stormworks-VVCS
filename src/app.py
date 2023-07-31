from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPixmap, QImage, QIcon
from ui_main import Ui_VVCS
from itemWidget import itemWidget
from settings_loader import Settings
from fileworks import FileWorks, DEFAULT_LOCAL
from sharing import *


class MainWindow(QMainWindow, Ui_VVCS):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_VVCS()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.fileworks = FileWorks(self.settings.data_path)
        self.share = GitWorks(DEFAULT_LOCAL, self.settings.repo_access)

        self.current_item = None

        self.ui.gameVehiclesList.pressed.connect(lambda: self.clear_selection(self.ui.serverVehiclesList))
        self.ui.serverVehiclesList.pressed.connect(lambda: self.clear_selection(self.ui.gameVehiclesList))

        self.ui.serverVehiclesList.itemSelectionChanged.connect(lambda: self.draw_item_info())
        self.ui.gameVehiclesList.itemSelectionChanged.connect(lambda: self.draw_item_info())

        self.ui.CommitBtn.clicked.connect(lambda: self.commit_item())
        self.ui.syncGameBtn.clicked.connect(lambda: self.share.local_remote_push())

        self.ui.refreshBtn.clicked.connect(lambda: self.update_from_remote())

        self.reload_remote()
        self.reload_game()

        self.ui.updateLabel.hide()

    def update_from_remote(self):
        try:
            self.share.local_remote_update()
        except:
            pass
        self.reload_remote()

    def commit_item(self):
        if self.current_item[0] == "local":
            comment = None if len(self.ui.CommentLine.toPlainText()) == 0 else self.ui.CommentLine.toPlainText()
            self.fileworks.vehicle_copy_to_local(self.current_item[1].text())
            for ext in ("xml", "png"):
                try:
                    if self.current_item[1].type == "vehicle":
                        self.share.local_add(f"vehicles/{self.current_item[1].text()}.{ext}", comment)
                    if self.current_item[1].type == "microprocessor":
                        self.share.local_add(f"microprocessors/{self.current_item[1].text()}.{ext}", comment)
                except Exception as e:
                    print(e)
            self.reload_remote()

    def reload_remote(self):
        self.ui.serverVehiclesList.clear()
        for elem in self.fileworks.local_get_vehicle_names():
            self.ui.serverVehiclesList.addItem(itemWidget(elem, "vehicle"))

        for elem in self.fileworks.local_get_microprocessor_names():
            self.ui.serverVehiclesList.addItem(itemWidget(elem, "microprocessor"))

    def reload_game(self):
        self.ui.gameVehiclesList.clear()
        for elem in self.fileworks.game_get_vehicle_names():
            self.ui.gameVehiclesList.addItem(itemWidget(elem, "vehicle"))

        for elem in self.fileworks.game_get_microprocessor_names():
            self.ui.gameVehiclesList.addItem(itemWidget(elem, "microprocessor"))

    def clear_selection(self, qlist):
        selected = qlist.selectedItems()
        if len(selected) != 0:
            selected[0].setSelected(False)

    def draw_item_info(self):
        selected = None
        if len(self.ui.gameVehiclesList.selectedItems()) != 0:
            selected = self.ui.gameVehiclesList.selectedItems()[0]
            self.current_item = ("local", selected)

        if len(self.ui.serverVehiclesList.selectedItems()) != 0:
            selected = self.ui.serverVehiclesList.selectedItems()[0]
            self.current_item = ("remote", selected)

        if selected is not None:
            self._draw()

    def _draw(self):
        if self.current_item is None:
            return
        if self.current_item[0] == "local":
            path = self.settings.data_path
            self.ui.updateLabel.hide()

        if self.current_item[0] == "remote":
            path = "../local"
            self.ui.updateLabel.show()

        if self.current_item[1].type == "vehicle":
            image = f"{path}/vehicles/{self.current_item[1].text()}.png"

        if self.current_item[1].type == "microprocessor":
            image = f"{path}/microprocessors/{self.current_item[1].text()}.png"

        pixmapImage = QPixmap(image)
        pixmapImage = pixmapImage.scaled(225, 225, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.ui.imageLabel.setPixmap(pixmapImage)
        self.ui.nameLabel.setText(self.current_item[1].text())