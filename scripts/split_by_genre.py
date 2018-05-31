"""
Copy the test-set files to directories by genre based on config
"""

__author__ = 'Pablo Ruiz'
__date__ = '24/09/17'
__email__ = 'pabloruizfabo@gmail.com'


import os
from shutil import copy as shcopy
import sys


# config path
import inspect
here = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
sys.path.append(here)

import config as cfg


def create_genre_directories(cf):
    """
    Create directories for genres based on config
    @param cf: a module with config values, at L{config.py}
    """
    if not os.path.exists(cf.bdir_by_genre):
        os.makedirs(cf.bdir_by_genre)
    for gr, subgens in cf.genres.items():
        grdir = os.path.join(cf.bdir_by_genre, gr)
        try:
            os.makedirs(grdir)
        except OSError:
            assert os.path.exists(grdir)
            pass
        if len(subgens) > 0:
            for subgen in subgens:
                try:
                    os.makedirs(os.path.join(grdir, subgen))
                except OSError:
                    assert os.path.exists(os.path.join(grdir, subgen))


def copy_to_genre_directories(cf):
    """
    Copy files from directory where they're not divided by genre
    to their respective genre directories, based on config.
    @param cf: a module with config values, at L{config.py}
    """
    for gr, fn2nbr in cf.filenames.items():
        assert gr in cf.genres or gr in cf.all_genre_keys
        for fn, _ in fn2nbr.items():
            infn = os.path.join(cf.bdir, fn)
            # is genre
            if gr in cf.genres:
                ffn = os.path.join(os.path.join(cf.bdir_by_genre, gr), fn)
            # is subgenre
            elif gr in cf.all_genre_keys:
                pargr = [ke for ke in cf.genres if gr in cf.genres[ke]]
                assert pargr
                assert len(pargr) == 1
                pargrdir = os.path.join(cf.bdir_by_genre, pargr[0])
                subgendir = os.path.join(pargrdir, gr)
                ffn = os.path.join(subgendir, fn)
            shcopy(infn, ffn)


def main(cf):
    """Run"""
    create_genre_directories(cf)
    copy_to_genre_directories(cf)


if __name__ == "__main__":
    main(cfg)