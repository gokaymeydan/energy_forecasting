import pandas as pd

def load_and_preprocess(path="data/processed/hourly_power_consumption.csv"):
    df = pd.read_csv(path, parse_dates=['Datetime'])
    df.set_index('Datetime', inplace=True)
    df = df.dropna(subset=['Global_active_power'])

    df['hour'] = df.index.hour
    df['day'] = df.index.day
    df['weekday'] = df.index.weekday
    df['month'] = df.index.month

    X = df[['hour', 'day', 'weekday', 'month']]
    y = df['Global_active_power']
    return df, X, y