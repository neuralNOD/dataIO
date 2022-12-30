# -*- encoding: utf-8 -*-

"""
An Automated Script to Create "TimeBlocksMaster" Table

Given a time interval, the function generates a time blocks table
with columns: [block, start_time, end_time] based on block interval.
The code is kept as dynamic as possible, with user inputs are to be
decided later.
"""

import warnings
import datetime as dt # module to manipulate unix datetime

# add the path to `errors` directory
import os
import sys
sys.path.append(os.path.join("..", "..", "errors"))

from __warnings import InProgress # noqa: F403 # pylint: disable=unused-import

def create_time_blocks(block_interval : int) -> dict:
    """
    Create a Time Blocks Master Table based

    Given the `block_interval` in minutes, the function generates a
    `dict()` or `json` that has the block number and start and end
    time for each block. Do note that there is overlapping time
    at each interval, but this is forcefully done as required by IEX.

    :type  block_interval: int
    :param block_interval: Enter the block interval in minutes, which
                           creates the time blocks master.
    """

    time_blocks = {k : [] for k in [
        "time_block", # actual block number
        "start_time", # block start time, equivalent to `block * block_interval`
        "block_end_time", # the actual time when the block ends
        "iex_block_end_time" # iex has overlapping time issues, represented as `str`
    ]}

    if (24 * 60 % block_interval) != 0:
        warnings.warn("TODO Raise Issue.", InProgress)
        num_blocks_ = int(24 * 60 / block_interval) + 1
    else:
        num_blocks_ = int(24 * 60 / block_interval)

    init_time_ = dt.datetime(2000, 1, 1, 0, 0) # generate time from here
    for block in range(num_blocks_):
        start_time = (init_time_ + dt.timedelta(minutes = block_interval * block)).time()
        block_end_time = (
            init_time_ + dt.timedelta(minutes = block_interval * (block + 1)) -
            dt.timedelta(seconds = 1)
        ).time()

        if (block + 1) != num_blocks_:
            iex_block_end_time = str((init_time_ + dt.timedelta(minutes = block_interval * (block + 1))).time())
        else:
            iex_block_end_time = "24:00:00"

        # add data to dictionary object
        for k, v in zip(time_blocks.keys(), [block + 1, start_time, block_end_time, iex_block_end_time]):
            time_blocks[k].append(v)

    return time_blocks


def create_block_range(block_interval : int, seperator : str = " - ") -> dict:
    """
    Create a Block Range as in IEX Data Sheets

    Given a `block_interval` the function adds a parameter called
    `block_range` which can be used to directly query and merge
    based on IEX tables. Also, send a seperator tag used for `join`
    command.
    """

    time_blocks = create_time_blocks(block_interval = block_interval)
    time_blocks |= dict(block_range = [])

    for block in range(int(24 * 60 / block_interval)):
        time_blocks["block_range"].append(f"{seperator}".join(map(
            lambda y : str(y)[:-3],
            [time_blocks["start_time"][block], time_blocks["iex_block_end_time"][block]]
        )))

    return time_blocks


if __name__ == "__main__":
    import json
    print(json.dumps(create_time_blocks(block_interval = 15), indent = 2, default = str))
