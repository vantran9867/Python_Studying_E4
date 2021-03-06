from plot_graph_2 import CoronaDataService
import datetime

aus_data = CoronaDataService('aus_covid.json')
vn_data = CoronaDataService('vietnam_covid.json')
print(vn_data.get_total_cases_in_country('Viet Nam'))
