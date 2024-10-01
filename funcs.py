import pandas as pd

def search_icao(icao_code):
    # print(f'Got icao code: {icao_code}')
    # return ['DE','Stutgart']

    result = []
    df = pd.read_csv('iata-icao.csv')
    for index,row in df.iterrows():
        if row["icao"] == icao_code:
            result.append(row["country_code"])
            result.append(row["airport"])

    return result