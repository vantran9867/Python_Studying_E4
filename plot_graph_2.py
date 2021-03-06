import datetime
import json


class CoronaDataService:
    province: str

    def __init__(self, data_file: str, province: str):
        self.province = '{}'.format(province)
        self.country_data = self.open_json_file(data_file)

    def open_json_file(self, path):
        with open(path) as file:
            data = json.load(file)
        return data

    def get_total_cases_in_country(self, country) -> int:
        total_cases = 0
        for record in CoronaDataService.open_json_file(self):
            total_cases += record['Cases']
        return total_cases

    def get_total_cases_in_province(self, country_data: str, province: str) -> int:
        total_cases = 0
        for record in CoronaDataService.open_json_file(self):
            if record['Province'] == self.province:
                total_cases += record['Cases']
        return total_cases











