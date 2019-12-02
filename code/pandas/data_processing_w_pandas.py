import pandas as pd
pd.read_csv('pandas_tutorial_read.csv', delimiter=';')

pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

