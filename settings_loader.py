import json
from pathlib import Path


DEFAULT_PATH = "config.json"


class Settings:
    def __init__(self, data_path=None, pat=None, url=None):
        self.__json = self.__load_json(DEFAULT_PATH)

        self.__pat = pat if pat is not None else self.pat_from_json()
        self.__url = url if url is not None else self.url_from_json()

        self.data_path = data_path if data_path is not None else self.path_from_json()
        self.repo_access = self.__create_access_url()

    def __create_access_url(self):
        return self.__url.replace("<TOKEN>", self.__pat)

    def __load_json(self, json_path):
        fp = Path(json_path)
        if fp.exists() and fp.suffix == ".json":
            with open(fp, encoding="utf-8") as file:
                return json.load(file)
        raise Exception("Can't find .json file, is it exist?")

    def path_from_json(self):
        return self.__json["Stormworks"]["data_path"]

    def pat_from_json(self):
        return self.__json["Git"]["PAT"]

    def url_from_json(self):
        return self.__json["Git"]["url"]

