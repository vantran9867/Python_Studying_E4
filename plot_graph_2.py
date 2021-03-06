import datetime
import json_utilities


class CoronaDataService:
    def __init__(self, data_file: str):
        self.country_data = json_utilities.open_json_file(data_file)

    def get_total_cases_in_country(self, country: str) -> int:
        total_cases = 0
        for record in self.country_data:
            if record['Country'] == '{}'.format(country):
                total_cases += record['Cases']
        return total_cases

    def get_total_cases_in_province(self, province: str) -> int:
        total_cases = 0
        for record in self.country_data:
            if record['Province'] == province:
                total_cases += record['Cases']
        return total_cases

    










