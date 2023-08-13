from git import Repo
import os
import shutil


DEFAULT_LOCAL = "../local"


class GitWorks:
    """Working with GIT system"""
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
            try:
                local_repo = Repo.clone_from(url, path)
            except Exception as e:
                raise e
        return local_repo

    def get_commits(self, filepath):
        """
        :param filepath: path to file from local repository
        :return: last commit datetime and comment
        """
        commits = list(self.__localrepo.iter_commits(paths=filepath))
        return commits[::-1][0].committed_datetime, commits[::-1][0].message

    def local_add(self, filename, comment=None):
        """
        :param filename: filename with extension e.g. file.xml
        :param comment: commit comment. "Small changes" if None
        """
        try:
            self.__localrepo.git.add(filename)
        except Exception as e:
            raise e
        self.__localrepo.git.commit("-m", comment if comment is not None else "Small changes")

    def local_remote_push(self):
        try:
            self.__localrepo.remotes.origin.push()
        except Exception as e:
            raise e

    def local_remote_update(self):
        try:
            self.__localrepo.remotes.origin.pull()
        except Exception as e:
            raise e
