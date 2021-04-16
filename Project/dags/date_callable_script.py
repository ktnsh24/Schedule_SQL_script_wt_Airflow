import datetime
from datetime import timedelta
from datetime import datetime
import pandas as pd
import requests
import datetime
from datetime import date
import time


def date_callable():
    df = pd.read_csv('users_app_batch_client_data.csv', sep=',')
    today = date.today()
    df = df[df.download_date == str(today.strftime("%Y-%m-%d"))]
    df.to_csv("export_dataframe.csv", index=False)
    print(df)
