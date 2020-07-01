"""
Module directories
"""
import os

import config


class Directories:
    """
    For setting-up the directories for files splitting & archives
    """

    def __init__(self):
        """
        This constructor encodes the default directories for splits & archives
        """

        self.splits = os.path.join(os.getcwd(), config.splits)
        self.archives = os.path.join(os.getcwd(), config.archives)
        self.directories = [self.splits, self.archives]

    @staticmethod
    def cleanup(listof):
        """
        Clears the splits & archives directories

        :param listof: The list of directories that will be cleared.
        :return: None
        """

        for path in listof:
            files_ = [os.remove(os.path.join(base, file))
                      for base, directories, files in os.walk(path)
                      for file in files]

            if any(files_):
                raise Exception(
                    "Unable to delete all the files within directory {}".format(path))

        for path in listof:
            directories_ = [os.removedirs(os.path.join(base, directory))
                            for base, directories, files in os.walk(path, topdown=False)
                            for directory in directories
                            if os.path.exists(os.path.join(base, directory))]

            if any(directories_):
                raise Exception("Unable to delete all the directories within {}".format(path))

    @staticmethod
    def create(listof):
        """
        Creates the splits & archives directories

        :param listof: The list of directories that will be created.
        :return: None
        """

        for path in listof:
            if not os.path.exists(path):
                os.makedirs(path)

    def exc(self):
        """
        Entry point

        :return: None
        """
        self.cleanup(self.directories)
        self.create(self.directories)
