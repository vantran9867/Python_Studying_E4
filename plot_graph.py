import json
import datetime
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt

plt.style.use('seaborn')

with open('aus_covid.json') as aus_file:
    aus_data = json.load(aus_file)
    date_aus = []
    VIC = []
    WA = []
    ACT = []
    NSW = []
    NT = []
    QLD = []
    SA = []
    TAS = []
    for record in aus_data:
        if record['Province'] == 'Victoria':
            date = datetime.datetime.strptime(record['Date'], '%Y-%m-%dT%H:%M:%SZ')
            date_aus.append(date.date())
            VIC.append(record['Cases'])
        elif record['Province'] == 'Western Australia':
            WA.append(record['Cases'])
        elif record['Province'] == 'Australian Capital Territory':
            ACT.append(record['Cases'])
        elif record['Province'] == 'New South Wales':
            NSW.append(record['Cases'])
        elif record['Province'] == 'Northern Territory':
            NT.append(record['Cases'])
        elif record['Province'] == 'Queensland':
            QLD.append(record['Cases'])
        elif record['Province'] == 'South Australia':
            SA.append(record['Cases'])
        elif record['Province'] == 'Tasmania':
            TAS.append(record['Cases'])

with open('vietnam_covid.json') as vn_file:
    vn_date = []
    VN = []
    data2 = json.load(vn_file)
    for record in data2:
        date = datetime.datetime.strptime(record['Date'], '%Y-%m-%dT%H:%M:%SZ')
        vn_date.append(date.date())
        VN.append(record['Cases'])

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.set_title("Australia's Covid-19 cases daily increase")
ax1.plot(date_aus, VIC, label='Victoria')
ax1.plot(date_aus, WA, label='Western Australia')
ax1.plot(date_aus, ACT, label='Australian Capital Territory')
ax1.plot(date_aus, NSW, label='New South Wales')
ax1.plot(date_aus, NT, label='Northern Territory')
ax1.plot(date_aus, QLD, label='Queensland')
ax1.plot(date_aus, SA, label='South Australia')
ax1.plot(date_aus, TAS, label='Tasmania')
ax1.legend()

ax2.set_title("Vietnam's Covid-19 cases daily increase")
ax2.plot(vn_date, VN, color='#444444', linestyle='--', label='Viet Nam')
ax2.legend()


ax2.xaxis.set_tick_params(rotation=45)

plt.xlabel('Dates')
ax1.set_ylabel('Cases')
ax2.set_ylabel('Cases')

months = MonthLocator(bymonthday=22)
monthsFmt = DateFormatter("%Y-%m-%d")
ax2.xaxis.set_major_locator(months)
ax2.xaxis.set_major_formatter(monthsFmt)

plt.show()





