import pandas as pd
from datetime import datetime, timedelta
from urllib.error import HTTPError

data_available_from_date = '11-May-2018'
# Covert above date to datetime format
last_date = datetime.strptime(data_available_from_date, '%d-%b-%Y').date()  # datetime.date(2018, 5, 11)
current_date = datetime.today().date()  # datetime.date(2021, 7, 17)
no_of_days = (current_date - last_date).days  # 1163


def data_download():
    for i in range(no_of_days + 1):
        day = (last_date + timedelta(days=i)).strftime("%d%b%Y")  # i=0 >> '11May2018'
        url = 'https://howutrade.in/snapdata/?data=PreOpen_FO_' + str(day) + '&export=csv'
        try:
            df = pd.read_csv(url)
            file_date = (last_date + timedelta(days=i)).strftime("%y.%m.%d")  # i=0 >> '18.05.11'
            df.to_csv("Preopen_FO\\PreOpen_FO_" + file_date + ".csv", index=False)
        except HTTPError:  # On Market holidays you will get an HTTPError
            pass

    print('Data downloaded !!!')


data_download()
