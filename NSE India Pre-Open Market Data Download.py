import os
import requests
from datetime import datetime, timedelta


def data_download():
    """
    Get F&O Pre-Open market data from the first day of the current month to today's date.
    CSV files are saved in the "Preopen_Market_Data" folder in the current path.
    """

    last_date = datetime.now().replace(day=1).date()
    current_date = datetime.today().date()
    no_of_days = (current_date - last_date).days

    s = requests.Session()
    os.makedirs("Preopen_Market_Data", exist_ok=True)

    for i in range(no_of_days + 1):
        r = s.get(f'https://howutrade.in/snapdata/?data=PreOpen_FO_{(last_date + timedelta(days=i)).strftime("%d%b%Y")}&export=csv')
        if r.status_code == 200:  # On Market holidays you will get 404 status code
            with open(f"Preopen_Market_Data\\PreOpen_FO_{(last_date + timedelta(days=i)).strftime('%y.%m.%d')}.csv", 'wb') as f:
                f.write(r.content)

    print('Data downloaded!!!')


data_download()
