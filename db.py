import pandas as pd
import os

file = 'data.csv'

def init():
    if not os.path.exists(file):
        df = pd.DataFrame({'id': range(1, 11), 'val': range(10, 110, 10)})
        df.to_csv(file, index=False)

def get_data():
    return pd.read_csv(file)

def delete_last_row():
    df = get_data()
    df = df[:-1]  
    df.to_csv(file, index=False)

def update_data():
    df = get_data()
    max_id = df['id'].max()
    new_data = pd.DataFrame({'id': [max_id + 1], 'val': [df['val'].max() + 10]})
    df = pd.concat([df, new_data], ignore_index=True)  
    df.to_csv(file, index=False)
