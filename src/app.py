from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui_main import Ui_VVCS
from itemWidget import itemWidget
from settingsLoader import Settings
from fileworks import FileWorks
from sharing import *
from infoLabel import infoLabelWidget, EXCEPT_COLOR, ALARM_COLOR


class MainWindow(QMainWindow, Ui_VVCS):
    """Main window"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_VVCS()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(), self.height())

        self.settings = Settings()
        self.fileworks = FileWorks(self.settings.data_path)
        self.share = GitWorks(DEFAULT_LOCAL, self.settings.repo_access)

        self.infoLabel = infoLabelWidget(self)

        self.current_item = None

        self.ui.gameVehiclesList.pressed.connect(lambda: self.clear_selection(self.ui.serverVehiclesList))
        self.ui.serverVehiclesList.pressed.connect(lambda: self.clear_selection(self.ui.gameVehiclesList))

        self.ui.serverVehiclesList.itemSelectionChanged.connect(lambda: self.draw_item_info())
        self.ui.gameVehiclesList.itemSelectionChanged.connect(lambda: self.draw_item_info())

        self.ui.CommitBtn.clicked.connect(lambda: self.commit_item())
        self.ui.syncGameBtn.clicked.connect(lambda: self.push_to_remote())
        self.ui.syncServBtn.clicked.connect(lambda:  self.load_to_game())
        self.ui.refreshBtn.clicked.connect(lambda: self.update_from_remote())

        self.reload_remote()
        self.reload_game()

        self.ui.updateLabel.hide()

    def push_to_remote(self):
        try:
            self.share.local_remote_push()
            self.infoLabel.show_message("Changes loaded \nto remote!")
        except:
            self.infoLabel.show_message("Can't push to remote!", ALARM_COLOR)

    def load_to_game(self):
        if len(zip(self.fileworks.local_get_microprocessor_names(), self.fileworks.local_get_vehicle_names())) == 0:
            self.infoLabel.show_message("Nothing to load!", EXCEPT_COLOR)

        for vehicle in self.fileworks.local_get_vehicle_names():
            try:
                self.fileworks.vehicle_copy_to_data(vehicle)
            except:
                pass

        for micro in self.fileworks.local_get_microprocessor_names():
            try:
                self.fileworks.microprocessor_copy_to_data(micro)
            except:
                pass

        self.reload_game()
        self.infoLabel.show_message("Updates loaded \nto game data!")

    def update_from_remote(self):
        try:
            self.share.local_remote_update()
        except:
            pass
        self.reload_remote()
        self.reload_game()

    def commit_item(self):
        if self.current_item is not None and self.current_item[0] == "local":
            comment = None if len(self.ui.CommentLine.toPlainText()) == 0 else self.ui.CommentLine.toPlainText()
            for ext in ("xml", "png"):
                try:
                    if self.current_item[1].type == "vehicle":
                        self.fileworks.vehicle_copy_to_local(self.current_item[1].text())
                        self.share.local_add(f"vehicles/{self.current_item[1].text()}.{ext}", comment)

                    if self.current_item[1].type == "microprocessor":
                        self.fileworks.microprocessor_copy_to_local(self.current_item[1].text())
                        self.share.local_add(f"microprocessors/{self.current_item[1].text()}.{ext}", comment)
                except Exception as e:
                    self.infoLabel.show_message("Can't commit this object!", ALARM_COLOR)
                    print(e)
                    return None

            self.reload_remote()
            self.infoLabel.show_message("Changes commited!")

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
            self.__draw()

    def __draw_comment(self):
        if self.current_item[1].type == "vehicle":
            filepath = f"vehicles/{self.current_item[1].text()}.xml"

        if self.current_item[1].type == "microprocessor":
            filepath = f"microprocessors/{self.current_item[1].text()}.xml"

        commit = self.share.get_commits(filepath)

        self.ui.CommentLine.setReadOnly(True)
        self.ui.CommentLine.setText(commit[1])
        self.ui.updateLabel.setText(commit[0].strftime("%m-%d-%y %H:%M"))

    def __clear_comment(self):
        self.ui.CommentLine.setText("")
        self.ui.updateLabel.setText("00-00-00 00:00")
        self.ui.CommentLine.setReadOnly(False)

    def __draw(self):
        if self.current_item is None:
            return
        if self.current_item[0] == "local": # If item selected from local objects list in game data folder
            path = self.settings.data_path
            self.ui.updateLabel.hide()
            self.ui.CommitBtn.show()
            self.__clear_comment()

        if self.current_item[0] == "remote": # If item selected from remote objects list in local repo
            path = "../local"
            self.ui.updateLabel.show()
            self.ui.CommitBtn.hide()
            self.__draw_comment()

        if self.current_item[1].type == "vehicle":
            image = f"{path}/vehicles/{self.current_item[1].text()}.png"

        if self.current_item[1].type == "microprocessor":
            image = f"{path}/microprocessors/{self.current_item[1].text()}.png"

        pixmapImage = QPixmap(image)
        pixmapImage = pixmapImage.scaled(225, 225, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.ui.imageLabel.setPixmap(pixmapImage)
        self.ui.nameLabel.setText(self.current_item[1].text())