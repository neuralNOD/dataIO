# -*- encoding: utf-8 -*-

"""
Code to Parse RAW File(s) of Various Formats

The downloaded excel files are parsed using builtin `pandas`
functionalities. The functions provided below are callable to
parse files on the go.
"""

import pandas as pd

def read_market_snapshot(filepath : str, filetype : str = "single", **kwargs) -> pd.DataFrame:
    frame = pd.read_excel(filepath, skiprows = 5)
    frame = frame[[
        "Date | Hour | Time Block", "Unnamed: 2", # date and block identifier
        "Purchase Bid (MW)", "Sell Bid (MW)",
        "MCV (MW)",
        [col for col in frame.columns if "MCP (Rs/MWh)" in col][0]
    ]]
    
    # rename columns using our names - housekeeping
    frame.columns = ["EffectiveDate", "BlockID", "PurchaseBid", "SellBid", "MCV", "MCP"]

    # for each day, there should be 96 records, thus given `filetype == single`
    # and `filetype == multiple` it should be easier to get the files as in:
    if filetype == "single":
        n_ = 96 # there should be 96 records for each day
    elif filetype == "multiple":
        try:
            d_ = kwargs["days"]
        except KeyError as err:
            raise ValueError("In multiple filetype, no. of days must be passed.")
            
        n_ = 96 * d_
    else:
        raise ValueError(f"`filetype == {filetype}` not in ['single', 'multiple'].")
    
    frame = frame.iloc[:n_, :]
    
    # forward file date column, and cast to date
    frame["EffectiveDate"].ffill(inplace = True)
    frame["EffectiveDate"] = pd.to_datetime(frame["EffectiveDate"], format = "%d-%m-%Y")
    
    # parse the float columns and type cast
    for col in ["PurchaseBid", "SellBid", "MCV", "MCP"]:
        frame[col] = frame[col].apply(lambda x : float(x) if x != "-" else float(-1))

    return frame
