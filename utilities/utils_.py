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
