import datetime
import json


def open_json_file(path):
    with open(path) as file:
        data = json.load(file)
    return data


class CoronaDataService:
    def __init__(self, data_file: str):
        self.country_data = open_json_file(data_file)

    def get_total_cases_in_country(self, country) -> int:
        total_cases = 0
        for record in self.country_data:
            if record['Country'] == self.country:
                total_cases += record['Cases']
        return total_cases

    def get_total_cases_in_province(self, province: str) -> int:
        total_cases = 0
        for record in self.country_data:
            if record['Province'] == self.province:
                total_cases += record['Cases']
        return total_cases











