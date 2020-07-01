import glob
import math
import os
import sys

import dask.dataframe as dd
import numpy as np
import pandas as pd


def main():

    # Prepare
    directories.exc()

    # The data files
    listof = glob.glob(pathname=os.path.join(config.root, config.data, config.ext))
    temporary = pd.DataFrame(data={'src': listof})

    # Distributing
    npartitions = os.cpu_count() - 1
    distributing = dd.from_pandas(temporary, npartitions=npartitions)
    distributing = distribute.exc(distributing)

    distributing.visualize(filename=os.path.join('docs', 'distributing'), format='pdf')
    computation = distributing.compute(scheduler='processes')

    # Archiving: Herein, chunksize is the number rows per partition
    identifiers: np.ndarray = computation.dst.unique()

    chunksize = math.floor(identifiers.shape[0] / npartitions)
    chunksize = chunksize if chunksize > 0 else 1

    archiving: dd.core.DataFrame = dd.from_array(x=identifiers, chunksize=chunksize, columns=['directory'])
    archiving['success'] = archiving[['directory']].apply(archive.zipping, axis=1, meta=('success', 'int'))

    archiving.visualize(filename=os.path.join('docs', 'archiving'), format='pdf')
    archiving.compute(scheduler='processes')

    # The archives
    print(archive.details())


if __name__ == '__main__':
    sys.path.append(os.getcwd())
    sys.path.append(os.path.join(os.getcwd(), 'src'))

    import config
    import src.functions.directories
    import src.functions.distribute
    import src.functions.archive

    directories = src.functions.directories.Directories()
    distribute = src.functions.distribute.Distribute()
    archive = src.functions.archive.Archive()

    main()
