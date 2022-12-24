# -*- encoding: utf-8 -*-

"""
Webdriver Definations for ETL Tool

The webdrivers are dynamic to access/control various websites to
extract, transform and load (etl) data. Popular drivers associated
with `chrome (using selenium)` and others are defined. Dynamic nature
is preserved and the driver is not restricted to any particular
module. The `utilities` directory is to be added under `$PATH` so
the modules and definations are available system-wide.
"""

from typing import Iterable
from tqdm import tqdm as TQ

import selenium.webdriver as webdriver
import selenium.webdriver.chrome as chromedriver

def create_chromedriver(
    options : Iterable = [
        "--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
):
    """
    Create a dynamic `chromedriver` with various options to control
    `AJAX` enabled websites to perform data extractions. In general,
    in a dynamic website involves various clicks and accessing
    particular elements to get the data. To use the module, define
    the `options` and other parameters.

    :type  options: array-like
    :param options: A list of options for the driver. By default, the
                    driver is enabled with: 
                        * `--headless` : chrome headless options.
                        * `--no-sandbox` : run in local system
                          instead of sandbox environment.
                        * `--disable-dev-shm-usage` : disable
                          developer mode from driver.
    """

    chrome_options = chromedriver.options.Options()

    # enable chrome options as defined by user, or get the default
    for option in TQ(options, desc = "enabling chrome-options:"):
        chrome_options.add_argument(option) # let allow `n` options

    # define driver module base, this variable is returned and is
    # used as the main `chromedriver` and control options, note the
    # `selenium` drivers version, which defines control like:
    # ? `driver.find_element_by_id(*args, **kwargs)` : selenium < 2.3.0
    # ? `driver.find_element("id, *args, **kwargs)` : selenium >= 4.7.2
    driver = webdriver.Chrome(options = chrome_options)

    return chrome_options, driver
