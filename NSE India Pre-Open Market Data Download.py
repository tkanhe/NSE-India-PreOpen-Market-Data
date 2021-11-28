import requests
from datetime import datetime, timedelta


def data_download(date_from='11-May-2018'):
    """
    :return: CSV files of F&O Pre-Open market data from a given date (data is available from 11-May-2018) to today's date.
    """

    last_date = datetime.strptime(date_from, '%d-%b-%Y').date()  # datetime.date(2018, 5, 11)
    current_date = datetime.today().date()  # datetime.date(2021, 11, 28)
    no_of_days = (current_date - last_date).days  # 1297

    s = requests.Session()

    for i in range(no_of_days + 1):
        r = s.get(f'https://howutrade.in/snapdata/?data=PreOpen_FO_{(last_date + timedelta(days=i)).strftime("%d%b%Y")}&export=csv')
        if r.status_code == 200:  # On Market holidays you will get 404 status code
            with open(f"df1\\PreOpen_FO_{(last_date + timedelta(days=i)).strftime('%y.%m.%d')}.csv", 'wb') as f:
                f.write(r.content)

    print('Data downloaded!!!')


data_download()
