# -*- encoding: utf-8 -*-

"""
GET Market Data from Indian Energy Exchange (IEX)

IEX hosts and publishes various market reports (like DAM, RTM, etc.)
through their webportal available at https://www.iexindia.com/. The
files is available (to download) as Excel/PDF reports behind a
sophisticated AJAX enabled server. This scripts downloads all the
required reports in a RAW format (mostly `*.xlsx`) files and saves
in a local file system.
"""

import os # miscellaneous os interfaces
import sys # object manipulation of system
import json # read and manipulate json objects
import time # miscellaneous for time manipulation
import datetime as dt # module to manipulate datetime

from utils_ import * # noqa: F403 # pylint: disable:unused-import
from webdriver import create_chromedriver

def download(report : str, driver : object, outpath : str, outfile : tuple = tuple()) -> bool:
    URL = "https://www.iexindia.com/marketdata/{extension}.aspx"

    # set the driver with additional parameters
    driver.get(URL.format(extension = report)) # TODO dynamic setup
    params = dict(behavior = "allow", downloadPath = outpath)
    driver.execute_cdp_cmd("Page.setDownloadBehavior", params)

    # read the operations involved in fetching the reports
    operations = get_secrets(filepath = os.path.join(os.getcwd(), "secrets.yaml"))
    operations = operations["operations"][report] # get the operations for the report

    # get waittime, and description messages from the `key-value` like:
    wait_times = [d["waittime"] for d in operations.values()]
    desc_msgs_ = [d["message_"] for d in operations.values()]

    for operation, wait, message in zip(operations.keys(), wait_times, desc_msgs_):
        driver.find_element("id", operation).click()
        timer_(wait, desc = message) # allow the operation to complete

    # download the excel file to the path
    driver.find_element("link text", "Excel").click()
    timer_(11, desc = "Downloading Excel File")
    driver.quit() # safely close the driver, release cache

    # once the file is downloaded, rename the file using `os.rename`
    os.rename(os.path.join(outpath, outfile[0]), os.path.join(outpath, outfile[1]))
    return True


if __name__ == "__main__":
    print(f"{time.ctime()} | Starting IEX Market Data Downloads...")

    # get the additional arguments using `sys.argv`
    _, date = sys.argv

    # get the driver with configurations from `../utilities/`
    _, driver = create_chromedriver()

    # download each report specifically, using the section
    REPORTS = [
        # the following reports are available from 01.04.2012
        "market_snapshot", # marketdata/dam/marketsnapshot
    ]

    # read general configurations of each report from `config.json`
    config = json.load(open("config.json", "r"))

    # download report for the date
    date = dt.datetime.strptime(date, "%Y-%m-%d")

    for report in REPORTS:
        # each report can be downloaded invoking `download()`, all
        # files are downloaded into a specific database folder in
        # local file system, finally the raw files are transformed
        # and loaded using a different scripts - all of this is
        # controlled from this file
        download(
            report = report, driver = driver,
            outpath = os.path.join(os.getcwd(), "data"),
            outfile = (
                config[report]["default_name"],
                config[report]["final_name"].format(date = f"{date.year}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}")
            ),
        )
