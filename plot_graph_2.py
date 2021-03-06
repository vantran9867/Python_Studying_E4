import json
import datetime
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt
from corona_data_service import CoronaDataService

plt.style.use('seaborn')

aus_data = CoronaDataService('aus_covid.json')
vn_data = CoronaDataService('vietnam_covid.json')

VIC = aus_data.get_cases_list_in_province('Victoria')
WA = aus_data.get_cases_list_in_province('West Australia')
ACT = aus_data.get_cases_list_in_province('Australian Capital Territory')
NSW = aus_data.get_cases_list_in_province('New South Wales')
NT = aus_data.get_cases_list_in_province('Northern Territory')
QLD = aus_data.get_cases_list_in_province('Queensland')
SA = aus_data.get_cases_list_in_province('South Australia')
TAS = aus_data.get_cases_list_in_province('Tasmania')
date_aus = aus_data.date_list()

VN = vn_data.get_total_cases_in_country('Viet Nam')
vn_date = vn_data.date_list()

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