import json_utilities
import datetime


class CoronaDataService:
    def __init__(self, data_file: str):
        self.country_data = json_utilities.open_json_file(data_file)

    def get_record_of_province(self, province: str) -> list:
        records = []
        for record in self.country_data:
            if record['Province'] == province:
                records.append(record)
        return records

    def get_record_of_country(self, country: str) -> list:
        records = []
        for record in self.country_data:
            if record['Country'] == country:
                records.append(record)
        return records










