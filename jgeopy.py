import pandas as pd
import numpy as np


data = pd.read_csv('./geoData/01000-10.0b/01_2016.csv', encoding="SHIFT-JIS")
for i in range(2,48):
    filename = './geoData/{0:02d}000-10.0b/{0:02d}_2016.csv'.format(i)
    data = pd.concat([data, pd.read_csv(filename, encoding="shift_jisx0213")])

data = data.reset_index(drop=True)

def reverse_geocoding(latitude, longitude):
    '''
    マンハッタン距離で一番近い住所を返す。ただし、0.2マンハッタン距離以下のものがあったときに限る
    return:{state:県名, city:市区町村名, street:大字町丁目名, code:大字町丁目コード}
    '''
    result = {}
    manhattan = abs(data['緯度'] - latitude) + abs(data['経度'] - longitude)
    argmin = manhattan.argmin()
    if manhattan[argmin] <= 0.2:
        result = {'state':data['都道府県名'][argmin], 'city':data['市区町村名'][argmin],\
                  'street':data['大字町丁目名'][argmin], 'code':data['大字町丁目コード'][argmin],\
                 'manhattan':manhattan[argmin]}
        return result
    else:
        return None