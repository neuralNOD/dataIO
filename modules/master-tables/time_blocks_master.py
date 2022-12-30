# -*- encoding: utf-8 -*-

"""
An Automated Script to Create "TimeBlocksMaster" Table

Given a time interval, the function generates a time blocks table
with columns: [block, start_time, end_time] based on block interval.
The code is kept as dynamic as possible, with user inputs are to be
decided later.
"""

import datetime as dt # module to manipulate unix datetime

def create_time_blocks(block_interval : int) -> dict:
    """
    Create a Time Blocks Master Table based

    Given the `block_interval` in minutes, the function generates a
    `dict()` or `json` that has the block number and start and end
    time for each block. Do note that there is overlapping time
    at each interval, but this is forcefully done as required by IEX.
    """

    time_blocks = {k : [] for k in [
        "time_block", # actual block number
        "start_time", # block start time, equivalent to `block * block_interval`
        "block_end_time", # the actual time when the block ends
        "iex_block_end_time" # iex has overlapping time issues, taken care
    ]}
    num_blocks_ = int(24 * 60 / block_interval) # `block_interval` in minutes

    init_time_ = dt.datetime(2000, 1, 1, 0, 0) # generate time from here
    for block in range(num_blocks_):
        start_time = (init_time_ + dt.timedelta(minutes = block_interval * block)).time()
        block_end_time = (
            init_time_ + dt.timedelta(minutes = block_interval * (block + 1)) -
            dt.timedelta(seconds = 1)
        ).time()
        iex_block_end_time = (init_time_ + dt.timedelta(minutes = block_interval * (block + 1))).time()

        # add data to dictionary object
        for k, v in zip(time_blocks.keys(), [block + 1, start_time, block_end_time, iex_block_end_time]):
            time_blocks[k].append(v)

    return time_blocks


if __name__ == "__main__":
    import json
    print(json.dumps(create_time_blocks(block_interval = 15), indent = 2, default = str))
