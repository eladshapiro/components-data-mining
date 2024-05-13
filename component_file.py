import os
from electrical_component import ElectricalComponent
from componant_data_extractor import ComponentExtractor


class ComponentFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.name = os.path.splitext(os.path.basename(file_path))[0]
        self.temperature_range = None
        self.voltage_range = None

    def process(self):
        temperature_range, voltage_range = ComponentExtractor.process_file(self.file_path)
        self.temperature_range = temperature_range
        self.voltage_range = voltage_range

    def create_component(self):
        return ElectricalComponent(self.name, self.voltage_range, self.temperature_range)
