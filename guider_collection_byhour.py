import json
import pandas as pd
import pickle
import datetime,os

import utils
import queryBeacons as qb

databank_filepath = './databank/positions'
os.makedirs(databank_filepath,exist_ok=True)

beacon_ids = utils.get_beacons()
print('=== load beacons ids ===')

for beacon in beacon_ids:
    recordName= f'{beacon}.pkl'
    pickle_filepath = os.path.join(databank_filepath,recordName)
    
    if os.path.isfile(pickle_filepath):
        print(f'=== {beacon}.pkl exist, loading ===')

        txyzPd_origin = pd.read_pickle(pickle_filepath)
        starTime = txyzPd_origin.iloc[-1]['positionTime']
        endTimeUTC = datetime.datetime.now(datetime.UTC)
        endTime = endTimeUTC.isoformat()[:-12]+"000Z"
        
        txyzPd = qb.getBCtxyz(beacon,starTime,endTime)
        print(f'=== {beacon} quering txyz ===')
        if isinstance(txyzPd,pd.DataFrame):
            if len(txyzPd) > 0:
                txyzPdnew = pd.concat([txyzPd_origin,txyzPd],axis=0,ignore_index=True)
                txyzPdnew.to_pickle(pickle_filepath)
                
                print(f'=== complete {beacon} txyz update ===')
            else:
                print(f'=== {beacon} no new data ===')
    else:
        print(f'=== no {beacon}.pkl ===')
        starTimeUTC = datetime.datetime.now(datetime.UTC) - datetime.timedelta(hours=30)
        endTimeUTC = datetime.datetime.now(datetime.UTC)
        
        starTime = starTimeUTC.isoformat()[:-12]+"000Z"
        endTime = endTimeUTC.isoformat()[:-12]+"000Z"
        
        txyzPd = qb.getBCtxyz(beacon,starTime,endTime)
        
        print(f'=== {beacon} quering txyz ===')
        
        if isinstance(txyzPd,pd.DataFrame):
            if len(txyzPd) > 0:
                txyzPd.to_pickle(pickle_filepath)
                print(f'=== complete {beacon} txyz update ===')
            else:
                print(f'=== {beacon} no new data ===')                

# datetime.datetime.now().isoformat()[:-7]+".000Z"  "2024-07-30T01:30:00.000Z"
#datetime.datetime.now(datetime.UTC)


