import requests
import json, datetime,os
import pandas as pd

# datetime.datetime.now().isoformat()[:-7]+".000Z"  "2024-07-30T01:30:00.000Z"
# datetime.datetime.now(datetime.UTC)
def getBCtxyz(beaconId,starTime,endTime):
    url = 'http://127.0.0.1:8686/rtls/rest/1.0.0/track/positions/query'  
    headers = {'x-api-key': 'ntuh7c55c1778af945bb8f9bd764d7157e50',
               'x-app-id':'ntuh-app'}
    
    queryJson ={"queryType": "item",
            "itemUid": beaconId,
            "fields": ["positionTime","position"],
            "period": {
                "start": starTime,
                "end": endTime,
                "startExcluded": True,
                "endExcluded": True
                },
            "start": 0,
            "limit": 10000}
    
    x = requests.post(url, headers=headers, json = queryJson)
    query_response = json.loads(x.text)
    
    if query_response['success']:
        query_data = query_response['data']
        colName=query_data['fields']
        position_time_xyz = pd.DataFrame(query_data['content'],columns=colName)
        return position_time_xyz
    else:
        return query_response['success']