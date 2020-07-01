"""
Module distribute
"""
import shutil
import os
import config

import dask.dataframe as dd


class Distribute:
    """
    Distributes a set of files into a number of directories, in preparation for archiving.
    """

    def __init__(self):
        """
        The constructor
        """

        self.zfill = config.zfill
        self.nfiles = config.nfiles
        self.rootsplits = os.path.join(config.root, config.splits) + os.sep

    @staticmethod
    def move(r):
        """
        Moves files.

        :param r: A DataFrame row consisting of source & destination values for shutil.move()
        :return:
        """
        try:
            shutil.move(src=r.src, dst=r.dst)
        except shutil.Error as err:
            raise err

        return 0

    def destinations(self, series):
        """
        Creates the destination string of each file that will be moved.

        :param series: dask.dataframe.Series of directory base names

        :return:
        """
        return self.rootsplits + series

    @staticmethod
    def splits(series):
        """
        Creates the splits directories into which files will be split

        :param series: dask.dataframe.Series of directory base names
        :return:
        """

        array_of_splits = series.unique().compute().values

        for split in array_of_splits:
            if not os.path.exists(os.path.join(split)):
                os.makedirs(split)

    def exc(self, blob: dd.DataFrame):
        """

        :param blob: That includes URI of the files to be moved
        :return:
        """

        # Determine destination
        blob['indices'] = blob.index
        blob['division'] = blob.indices.floordiv(self.nfiles).astype(str).str.zfill(self.zfill)
        blob['dst'] = self.destinations(blob['division'])

        # Create the splits directories
        self.splits(series=blob.dst)

        # Move
        blob['success'] = blob[['src', 'dst']].apply(self.move, axis=1, meta=('success', 'int'))

        return blob.drop(columns=['indices', 'division'])
