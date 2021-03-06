from corona_data_service import CoronaDataService
import datetime

aus_data = CoronaDataService('aus_covid.json')
vn_data = CoronaDataService('vietnam_covid.json')
print(vn_data.get_total_cases_in_country('Viet Nam'))
print(vn_data.get_new_cases_in_date('2021-2-11'))



