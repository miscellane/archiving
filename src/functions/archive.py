"""
Module archive
"""
import glob
import os
import zipfile

import pandas as pd

import config
import src.functions.directories


class Archive:
    """
    Class Archive
    """

    def __init__(self):
        """
        The constructor
        """

        self.root = config.root
        self.archives = config.archives
        self.ext = config.ext

        self.archiveslist = config.archiveslist

        self.archivestype = config.archivestype
        self.archivesuri = os.path.join(self.root, self.archives)

    def details(self):
        """
        Creates a list of the archive files.  The file name is config.archiveslist

        :return: Status message
        """

        inventory = pd.DataFrame(
            data={'uri': glob.glob(pathname=os.path.join(self.root, self.archives, '*.' + self.archivestype))}
        )
        inventory['filename'] = inventory.uri.apply(lambda x: os.path.basename(x))
        inventory.drop(columns=['uri'], inplace=True)
        inventory.to_csv(path_or_buf=self.archiveslist, index=False, encoding='UTF-8')

        return 'Ready.  The list of zip files is summarised in {}'.format(self.archiveslist)

    def zipping(self, r):
        """
        Zips directories

        :param r: Records of directories that will be archived.
        :return:
        """

        # The archive name will be the raw directory name
        directory = r.directory
        archivename = os.path.basename(directory)

        # Open ...
        zip_object = zipfile.ZipFile(os.path.join(self.archivesuri, archivename + '.zip'), 'x')

        # The list of images in 'directory'
        images = glob.glob(os.path.join(directory, self.ext))

        # Write each image in the list to a zip archive
        try:
            [zip_object.write(filename=images[i], arcname=os.path.basename(images[i]),
                              compress_type=zipfile.ZIP_DEFLATED) for i in range(len(images))]
            state = 0
        except OSError as err:
            raise err

        # ... Close
        zip_object.close()

        src.functions.directories.Directories().cleanup([r.directory])

        return state
