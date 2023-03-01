import pandas as pd
import json


def refactor_values(data):
    def transform_value(value):
        if isinstance(value, str) and '<' in value:
            return int(value.split('<')[1])
        else:
            return value

    return {key: transform_value(value) for key, value in data.items() if value != ''}


def process_data(src, dist):
    f = open(src, 'r', encoding='utf-8')
    raw = json.load(f)
    f.close()

    df = pd.DataFrame()

    print('Transforming dataframe...')
    for i in range(len(raw)):
        jdata = json.loads(raw[i]['json'])
        station = jdata['arsopodatki']['postaja']
        for i in range(len(station)):
            data = station[i]
            data = refactor_values(data)
            df = pd.concat([df, pd.json_normalize(data)])

    print('Filling, transorming and dropping data...')
    num_cols = df.select_dtypes(exclude=['object']).columns
    df = df.assign(**{col: df[col].fillna(df[col].mean()) for col in num_cols})

    df_location = pd.get_dummies(df['merilno_mesto'])
    df = pd.concat([df, df_location], axis=1).reindex(df.index)

    df.drop(columns=['merilno_mesto', 'sifra', 'datum_od', 'datum_do'], inplace=True)

    print('Saving new data...')
    df_sorted = df.sort_index(axis=1)
    df = df_sorted
    df.to_csv(dist, index=False)

    print('OK!')


if __name__ == '__main__':
    import os

    root_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../..'))

    src = os.path.join(root_dir, 'data', 'raw.json')
    dist = os.path.join(root_dir, 'data', 'processed.csv')

    process_data(src, dist)