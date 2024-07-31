import json
import pandas as pd
import pickle
import datetime,os, glob

import utils

databank_filepath = './databank/positions'
os.makedirs(databank_filepath,exist_ok=True)

beacon_ids = utils.get_beacons()

for beacon in beacon_ids:
    recordName= f'{beacon}.pkl'
    pickle_filepath = os.path.join(databank_filepath,recordName)
    excelName = f'{beacon}.xlsx'
    excel_path = os.path.join("C:/Users/guide/Documents/ntuhBeaconTXYZ",excelName)
    
    if os.path.isfile(pickle_filepath):
        print(f'=== {beacon}.pkl exist, loading ===')
        txyzPd_origin = pd.read_pickle(pickle_filepath)
        txyzPd_origin.to_excel(excel_path)
        print(f'=== {beacon} copy complete ===')
        

                

# datetime.datetime.now().isoformat()[:-7]+".000Z"  "2024-07-30T01:30:00.000Z"
#datetime.datetime.now(datetime.UTC)


