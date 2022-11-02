import pandas as pd
import requests as req


class GetRegionalData:
    """ Upload BEA's data by line code and table name - assigned to Regional Dataset"""

    def __init__(self):
        self.params_x = {'USERID': '64C1A606-C86B-4702-A5D0-977F79A936D1',
                  'METHOD': 'GETDATA',
                  'DATASETNAME': 'REGIONAL',
                  'YEAR': 'ALL',    #specific year, LAST5 or LAST10
                  'TABLENAME': '',
                  'GEOFIPS': 'STATE',
                  'LINECODE': 1,
                  'RESULTFORMAT': 'JSON'}

    def bea_frame_return(self, line_code, table_name) -> dict:
        """
        🧠 Arguments:
        ----
        line_code = parameter should contain integer as a line code key.
        example "line_code = 1" ✅
        To check available line codes launch 'BEALineCodePick.py' in your terminal 💻

        table_name = parameter should contain string as a chosen table name.
        example "table_name = 'SAEMP25N'" ✅
        To check available tables see BEA Doc 📒

        """
        url = 'https://apps.bea.gov/api/data'
        self.params_x.update({'TABLENAME': table_name, 'LINECODE': line_code})
        get = req.get(url, self.params_x).json()['BEAAPI']['Results']['Data']

        return pd.DataFrame(get)


#x = GetRegionalData()
#data = x.bea_frame_return(line_code=10, table_name='SAEMP25N')
