import json
import datetime
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt

with open('aus_covid.json') as json_file:
    data1 = json.load(json_file)
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    for record in data1:
        if record['Province'] == 'Victoria':
            date = datetime.datetime.strptime(record['Date'], '%Y-%m-%dT%H:%M:%SZ')
            x1.append(date.date())
            y1.append(record['Cases'])
        elif record['Province'] == 'Western Australia':
            y2.append(record['Cases'])
        elif record['Province'] == 'Australian Capital Territory':
            y3.append(record['Cases'])
        elif record['Province'] == 'New South Wales':
            y4.append(record['Cases'])
        elif record['Province'] == 'Northern Territory':
            y5.append(record['Cases'])
        elif record['Province'] == 'Queensland':
            y6.append(record['Cases'])
        elif record['Province'] == 'South Australia':
            y7.append(record['Cases'])
        elif record['Province'] == 'Tasmania':
            y8.append(record['Cases'])

fig, (ax1, ax2) = plt.subplots()
ax1.plot(x1, y1, label='Victoria')
ax1.plot(x1, y2, label='Western Australia')
ax1.plot(x1, y3, label='Australian Capital Territory')
ax1.plot(x1, y4, label='New South Wales')
ax1.plot(x1, y5, label='Northern Territory')
ax1.plot(x1, y6, label='Queensland')
ax1.plot(x1, y7, label='South Australia')
ax1.plot(x1, y8, label='Tasmania')

plt.xticks(rotation=45)
plt.xlabel('Dates', fontsize=10)
plt.ylabel('Cases', fontsize=10)

months = MonthLocator(bymonthday=22)
monthsFmt = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
plt.show()





