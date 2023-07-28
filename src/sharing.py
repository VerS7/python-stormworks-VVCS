from git import Repo


class GitWorks:
    def __init__(self, path, remote_url):
        self.__localrepo = self.__create_repo(path, remote_url)

    def __create_repo(self, path, url):
        try:
            local_repo = Repo(path)
        except:
            local_repo = Repo.clone_from(url, path)
        return local_repo

    def local_add(self, file, comment=None):
        self.__localrepo.git.add(file)
        self.__localrepo.git.commit("-m", comment if comment is not None else "Small changes")

    def local_remote_push(self):
        self.__localrepo.remotes.origin.push()

    def local_update(self):
        self.__localrepo.remotes.origin.pull()