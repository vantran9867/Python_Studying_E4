from plot_graph_2 import CoronaDataService
from date import Date

#vnCovidDataService = CoronaDataService('vietnam_covid', '')
#vnCovidDataService.open_json_file('vietnam_covid')
#print(vnCovidDataService.get_total_cases_in_country('vietnam_covid'))
aus_data = CoronaDataService('aus_covid.json')
vn_data = CoronaDataService('vietnam_covid.json')
d1 = Date(12, 3, 2029)
print(d1)