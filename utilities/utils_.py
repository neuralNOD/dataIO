# -*- encoding: utf-8 -*-

"""
A General List of Utility Functions

These are a set of functions which can be used generally, and/or
specific to a particular use case. Check documentations at function
level for more information.

List of Available `lambda` Functions and their Use Case:
    * timer_ : Adds a Progress Bar while Awaiting in a Operation
               The AJAX enabled websites are slow, which requires a
               wait time. This function simply adds a progress bar
               using the `tqdm` and `time.sleep(secs)` module.
"""

import os
import time
import yaml

from tqdm import tqdm as TQ

### *** LAMBDAs *** ###
timer_ = lambda secs, desc = None : [
        time.sleep(1) for _ in TQ(range(secs), total = secs, desc = desc)
    ]


### *** LONG UTILITY FUNCTION(s) *** ###
def get_secrets(filepath : str) -> dict:
    """
    Read and Parse the `secrets.yaml` File

    Each module has a `secrets.yaml` file (check /README.md) which is
    parsed using the `pyYAML` library, and the dictionary contents
    are returned to the module.
    """

    with open(filepath, "r") as f:
        content = yaml.load(f, Loader = yaml.FullLoader)

    return content


def create_dir(base : str, year : int, month : int) -> str:
    """
    Create a Directory Structure like `base/year/month` using OS

    By default, a file is saved to a directory which is partitioned
    like `basedir/<year>/<month>` and the month name is decorated as
    "%m-%B" as in `dt.datetime.strftime` module.
    """

    months = {
        1 : "JAN", 2 : "FEB", 3 : "MAR", 4 : "APR",
        5 : "MAY", 6 : "JUN", 7 : "JUL", 8 : "AUG",
        9 : "SEP", 10: "OCT", 11 : "NOV", 12 : "DEC"
    }

    year = str(year)
    month = f"{str(month).zfill(2)}-{months.get(month)}"

    path = os.path.join(base, year, month)
    os.makedirs(path, exist_ok = True)
    return path
