import json
import datetime
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt

with open('aus_covid.json') as json_file:
    data = json.load(json_file)
    x = []
    y = []
    y1 = []
    for record in data:
        if record['Province'] == 'Victoria':
            date = datetime.datetime.strptime(record['Date'], '%Y-%m-%dT%H:%M:%SZ')
            x.append(date.date())
            y.append(record['Cases'])

fig, ax = plt.subplots()
ax.plot(x, y, label='Victoria')
plt.xticks(rotation=45)
plt.xlabel('Dates', fontsize=10)
plt.ylabel('Cases', fontsize=10)

months = MonthLocator(bymonthday=22)
monthsFmt = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
plt.show()





