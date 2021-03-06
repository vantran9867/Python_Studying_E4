import json_utilities
import datetime


class CoronaDataService:
    def __init__(self, data_file: str):
        self.country_data = json_utilities.open_json_file(data_file)

    def get_total_cases_in_country(self, country: str) -> int:
        total_cases = 0
        for record in self.country_data:
            if record['Country'] == country:
                total_cases += record['Cases']
        return total_cases

    def get_total_cases_in_province(self, province: str) -> int:
        total_cases = 0
        for record in self.country_data:
            if record['Province'] == province:
                total_cases += record['Cases']
        return total_cases

    def get_cases_list_in_country(self, country: str) -> list:
        cases_list = []
        for record in self.country_data:
            if record['Country'] == country:
                cases_list.append(record['Cases'])
        return cases_list

    def get_cases_list_in_province(self, province: str) -> list:
        cases_list = []
        for record in self.country_data:
            if record['Province'] == province:
                cases_list.append(record['Cases'])
        return cases_list

    def date_list(self) -> list:
        date_list = []
        for record in self.country_data:
            date = datetime.datetime.strptime(record['Date'], '%Y-%m-%dT%H:%M:%SZ')
            date_list.append(date.date())
        return date_list










