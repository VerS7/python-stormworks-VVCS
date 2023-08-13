from sharing import DEFAULT_LOCAL
from os import listdir
from os.path import isfile, join, splitext
from shutil import copy


class FileWorks:
    """File system interacting"""
    def __init__(self, data_path, local_path=DEFAULT_LOCAL):
        self.__dp = data_path
        self.__lp = local_path

    def game_get_vehicle_names(self):
        """Get file names of vehicles from game data"""
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__dp}/vehicles")
                           if isfile(join(f"{self.__dp}/vehicles", f)))
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def local_get_vehicle_names(self):
        """Get file names of vehicles from cloned local repository"""
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__lp}/vehicles")
                           if isfile(join(f"{self.__lp}/vehicles", f)) and not splitext(f)[0] == ".gitkeep")
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def game_get_microprocessor_names(self):
        """Get file names of microprocessors from game data"""
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__dp}/microprocessors")
                           if isfile(join(f"{self.__dp}/microprocessors", f)))
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def local_get_microprocessor_names(self):
        """Get file names of microprocessors from cloned local repository"""
        try:
            vehicles = set(splitext(f)[0] for f in listdir(f"{self.__lp}/microprocessors")
                           if isfile(join(f"{self.__lp}/microprocessors", f)) and not splitext(f)[0] == ".gitkeep")
        except FileNotFoundError as e:
            raise e
        return list(vehicles)

    def vehicle_copy_to_local(self, vehicle_name):
        """
        :param vehicle_name: name of vehicle file without extension
        Copy .png & .xml vehicle files from game data to local repository
        """
        try:
            for ext in ("png", "xml"):
                copy(f"{self.__dp}/vehicles/{vehicle_name}.{ext}", f"{self.__lp}/vehicles/")
        except FileNotFoundError as e:
            raise e

    def microprocessor_copy_to_local(self, vehicle_name):
        """
        :param vehicle_name: name of microprocessor file without extension
        Copy .png & .xml microprocessor files from game data to local repository
        """
        try:
            for ext in ("png", "xml"):
                copy(f"{self.__dp}/microprocessors/{vehicle_name}.{ext}", f"{self.__lp}/microprocessors/")
        except FileNotFoundError as e:
            raise e

    def vehicle_copy_to_data(self, vehicle_name):
        """
        :param vehicle_name: name of vehicle file without extension
        Copy .png & .xml vehicle files from local repository to game data
        """
        try:
            for ext in ("png", "xml"):
                copy(f"{self.__lp}/vehicles/{vehicle_name}.{ext}", f"{self.__dp}/vehicles/")
        except FileNotFoundError as e:
            raise e

    def microprocessor_copy_to_data(self, vehicle_name):
        """
        :param vehicle_name: name of microprocessor file without extension
        Copy .png & .xml microprocessor files from local repository to game data
        """
        try:
            for ext in ("png", "xml"):
                copy(f"{self.__lp}/microprocessors/{vehicle_name}.{ext}", f"{self.__dp}/microprocessors/")
        except FileNotFoundError as e:
            raise e
