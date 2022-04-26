import os
import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

no_of_days = 100  # Download the data for the last 100 days

os.makedirs("Preopen_Market_Data", exist_ok=True)
last_date = (datetime.now() - timedelta(days=no_of_days)).date()

urls = (
    (
        f"Preopen_Market_Data\\PreOpen_FO_{(last_date + timedelta(days=i)).strftime('%y.%m.%d')}.csv",
        f"https://howutrade.in/snapdata/?data=PreOpen_FO_{(last_date + timedelta(days=i)).strftime('%d%b%Y')}&export=csv",
    )
    for i in range(no_of_days + 1)
)

s = requests.Session()


def downlaod(url):
    r = s.get(url[1])
    if r.status_code == 200:  # On Market holidays you will get 404 status code
        with open(url[0], "wb") as f:
            f.write(r.content)


with ThreadPoolExecutor() as executor:
    executor.map(downlaod, urls)

print("Data downloaded!!!")
