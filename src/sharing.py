from git import Repo
import os
import shutil


DEFAULT_LOCAL = "../local"


class GitWorks:
    def __init__(self, path, remote_url):
        self.__localrepo = self.__create_repo(path, remote_url)

    def __create_repo(self, path, url):
        if not os.path.exists(DEFAULT_LOCAL):
            os.makedirs(DEFAULT_LOCAL)
        try:
            local_repo = Repo(path)
        except:
            shutil.rmtree(DEFAULT_LOCAL)
            os.makedirs(DEFAULT_LOCAL)
            local_repo = Repo.clone_from(url, path)
        return local_repo

    def local_add(self, filename, comment=None):
        self.__localrepo.git.add(filename)
        self.__localrepo.git.commit("-m", comment if comment is not None else "Small changes")

    def local_remote_push(self):
        self.__localrepo.remotes.origin.push()

    def local_remote_update(self):
        self.__localrepo.remotes.origin.pull()
