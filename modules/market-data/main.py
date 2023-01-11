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
import time # miscellaneous for time manipulation

from utils_ import * # noqa: F403 # pylint: disable:unused-import
from webdriver import create_chromedriver

def download(report : str, driver : object, outpath : str, outfile : str = None) -> bool:
    URL = "https://www.iexindia.com/marketdata/{extension}.aspx"

    # set the driver with additional parameters
    driver.get(URL.format(extension = report)) # TODO dynamic setup
    params = dict(behavior = "allow", downloadPath = os.path.join(os.getcwd(), outpath))
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

    return True


if __name__ == "__main__":
    print(f"{time.ctime()} | Starting IEX Market Data Downloads...")

    # get the driver with configurations from `../utilities/`
    _, driver = create_chromedriver()

    # download each report specifically, using the section
    REPORTS = [
        # the following reports are available from 01.04.2012
        "market_snapshot", # marketdata/dam/marketsnapshot
    ]

    for report in REPORTS:
        # each report can be downloaded invoking `download()`, all
        # files are downloaded into a specific database folder in
        # local file system, finally the raw files are transformed
        # and loaded using a different scripts - all of this is
        # controlled from this file
        download(
            report = report, driver = driver,
            outpath = os.path.join("data")
            # outpath = os.path.join("Market Data - Day Ahead Market (DAM)", "Market Snapshot")
        )
