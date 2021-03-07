import json
import datetime
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt
from corona_data_service import CoronaDataService

plt.style.use('seaborn')


def get_data_province(data_service: CoronaDataService, province):
    date_list = []
    province_data = data_service.get_record_of_province(province)
    for i in province_data:
        date = datetime.datetime.strptime(i['Date'], '%Y-%m-%dT%H:%M:%SZ')
        date_list.append(date)
    cases = [i['Cases'] for i in province_data]
    return date_list, cases


def get_data_country(data_service: CoronaDataService, country):
    date_list = []
    country_data = data_service.get_record_of_country(country)
    for i in country_data:
        date = datetime.datetime.strptime(i['Date'], '%Y-%m-%dT%H:%M:%SZ')
        date_list.append(date)
    cases = [i['Cases'] for i in country_data]
    return date_list, cases


aus_data = CoronaDataService('aus_covid.json')
vn_data = CoronaDataService('vietnam_covid.json')

vic = get_data_province(aus_data, 'Victoria')
wa = get_data_province(aus_data, 'West Australia')
act = get_data_province(aus_data, 'Australian Capital Territory')
nsw = get_data_province(aus_data, 'New South Wales')
nt = get_data_province(aus_data, 'Northern Territory')
qld = get_data_province(aus_data, 'Queensland')
sa = get_data_province(aus_data, 'South Australia')
tas = get_data_province(aus_data, 'Tasmania')

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.set_title("Australia's Covid-19 cases daily increase")
ax1.plot(vic[0], vic[1], label='Victoria')
ax1.plot(wa[0], wa[1], label='West Australia')
ax1.plot(act[0], act[1], label='Australian Capital Territory')
ax1.plot(nsw[0], nsw[1], label='Australian Capital Territory')
ax1.plot(nt[0], nt[1], label='Northern Territory')
ax1.plot(qld[0], qld[1], label='Queensland')
ax1.plot(sa[0], sa[1], label='South Australia')
ax1.plot(tas[0], tas[1], label='Tasmania')

ax1.legend()

vn = get_data_country(vn_data, 'Viet Nam')
ax2.set_title("VietNam's Covid-19 cases daily increase")
ax2.plot(vn[0], vn[1], color='#444444', linestyle='--', label='VietNam')
ax2.xaxis.set_tick_params(rotation=45)

plt.xlabel('Dates')
ax1.set_ylabel('Cases')
ax2.set_ylabel('Cases')

months = MonthLocator(bymonthday=22)
monthsFmt = DateFormatter("%Y-%m-%d")
ax2.xaxis.set_major_locator(months)
ax2.xaxis.set_major_formatter(monthsFmt)

plt.show()
