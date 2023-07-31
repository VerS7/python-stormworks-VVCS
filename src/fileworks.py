from sharing import DEFAULT_LOCAL
from os import listdir
from os.path import isfile, join, splitext
from shutil import copy


class FileWorks:
    def __init__(self, data_path, local_path=DEFAULT_LOCAL):
        self.__dp = data_path
        self.__lp = local_path

    def game_get_vehicle_names(self):
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__dp}/vehicles")
                           if isfile(join(f"{self.__dp}/vehicles", f)))
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def local_get_vehicle_names(self):
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__lp}/vehicles")
                           if isfile(join(f"{self.__lp}/vehicles", f)) and not splitext(f)[0] == ".gitkeep")
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def game_get_microprocessor_names(self):
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__dp}/microprocessors")
                           if isfile(join(f"{self.__dp}/microprocessors", f)))
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def local_get_microprocessor_names(self):
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__lp}/microprocessors")
                           if isfile(join(f"{self.__lp}/microprocessors", f)) and not splitext(f)[0] == ".gitkeep")
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def vehicle_copy_to_local(self, vehicle_name):
        try:
            for ext in ("png", "xml"):
                copy(f"{self.__dp}/vehicles/{vehicle_name}.{ext}", f"{self.__lp}/vehicles/")
        except FileNotFoundError as e:
            raise e

    def microprocessor_copy_to_local(self, vehicle_name):
        try:
            for ext in ("png", "xml"):
                copy(f"{self.__dp}/microprocessors/{vehicle_name}.{ext}", f"{self.__lp}/microprocessors/")
        except FileNotFoundError as e:
            raise e