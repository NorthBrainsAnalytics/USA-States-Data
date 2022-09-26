from enum import IntEnum
import pandas as pd
import requests as req
from IPython.display import display

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

connectionCheck = req.get \
    ('http://apps.bea.gov/api/data?&UserID=64C1A606-C86B-4702-A5D0-977F79A936D1&method=GETDATASETLIST&ResultFormat=JSON')

web_url = 'https://apps.bea.gov/api/data'

Menu = IntEnum('pick', 'SAEMP25N SAEMP27N SAGDP1 SAGDP9N \
SAGDP6N SAINC5N SAINC6N SAPCE2 QUIT')

if connectionCheck:
    print(f'Connection with BEA`s server established with code {connectionCheck.status_code} ✅')
else:
    print(f'Connection with BEA`s server failed with code {connectionCheck.status_code} ⛔️')

while True:
    pick = int(input("""
Pick number of chosen BEA's 📂 frame:
1. SAEMP25N
2. SAEMP27N
3. SAGDP1
4. SAGDP9N 
5. SAGDP6N
6. SAINC5N 
7. SAINC6N
8. SAPCE2
9. QUIT
"""))

    if pick == Menu.SAEMP25N:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAEMP25N',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAEMP25N = pd.DataFrame(get)
        print('Line Codes for SAEMP25N frame below:')
        display(SAEMP25N)


    elif pick == Menu.SAEMP27N:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAEMP27N',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAEMP27N = pd.DataFrame(get)
        print('Line Codes for SAEMP27N frame below:')
        display(SAEMP27N)


    elif pick == Menu.SAGDP1:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAGDP1',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAGDP1 = pd.DataFrame(get)
        print('Line Codes for SAGDP1 frame below:')
        display(SAGDP1)


    elif pick == Menu.SAGDP9N:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAGDP9N',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAGDP9N = pd.DataFrame(get)
        print('Line Codes for SAGDP9N frame below:')
        display(SAGDP9N)


    elif pick == Menu.SAGDP6N:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAGDP6N',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAGDP6N = pd.DataFrame(get)
        print('Line Codes for SAGDP6N frame below:')
        display(SAGDP6N)


    elif pick == Menu.SAINC5N:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAINC5N',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAINC5N = pd.DataFrame(get)
        print('Line Codes for SAINC5N frame below:')
        display(SAINC5N)


    elif pick == Menu.SAINC6N:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAINC6N',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAINC6N = pd.DataFrame(get)
        print('Line Codes for SAINC6N frame below:')
        display(SAINC6N)


    elif pick == Menu.SAPCE2:
        params = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'RESULTFORMAT': 'JSON',
                  'TARGETPARAMETER': 'LINECODE',
                  'TABLENAME': 'SAPCE2',
                  'DATASETNAME': 'REGIONAL',
                  'METHOD': 'GETPARAMETERVALUESFILTERED'}
        get = req.get(web_url, params).json()['BEAAPI']['Results']['ParamValue']
        SAPCE2 = pd.DataFrame(get)
        print('Line Codes for SAPCE2 frame below:')
        display(SAPCE2)

    else:
        print('❗️ Something went wrong or')

    if pick == 30:
        print('To many requests - connection close ‼️')
        break

    elif pick == 9:
        print('connection closed by user 👨🏼‍💻')
        break
