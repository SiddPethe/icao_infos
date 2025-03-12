import pandas as pd

def search_icao(icao_code):
    # print(f'Got icao code: {icao_code}')
    # return ['DE','Stutgart']

    result = []
    df = pd.read_csv('airports.csv')
    for index,row in df.iterrows():
        if row["icao_code"] == icao_code:
            result.append(row["iso_country"])
            result.append(row["municipality"])
            result.append(row["name"])

    return result