import os
from component_file import ComponentFile


class ComponentManager:
    def __init__(self, directory):
        self.directory = directory
        self.component_files = []

    def load_component_files(self):
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.directory, filename)
                component_file = ComponentFile(file_path)
                self.component_files.append(component_file)

    def process_component_files(self):
        for component_file in self.component_files:
            component_file.process()

    def create_components(self):
        return [component_file.create_component() for component_file in self.component_files]

    def get_components_for_conditions(self, voltage, temperature):
        matching_components = []
        for component_file in self.component_files:
            component = component_file.create_component()
            if component.is_within_ranges(voltage, temperature):
                matching_components.append(component)
        return matching_components
