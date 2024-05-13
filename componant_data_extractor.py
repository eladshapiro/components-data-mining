import re


class ComponentExtractor:
    @staticmethod
    def get_operating_temperature_range(text):
        """Extracts the operating temperature range from the given text."""
        pattern = re.compile(r"Temperature\s*range\s*:\s*(-?\d+\s*°?C)\s*to\s*(-?\d+\s*°?C)", re.IGNORECASE)
        match = pattern.search(text)
        if match:
            return f"{match.group(1)} to {match.group(2)}"
        return None

    @staticmethod
    def get_operating_voltage_range(text):
        """Extracts the operating voltage range from the given text."""
        pattern = re.compile(r"Input\s*voltage\s*range\s*:\s*(\d+\s*V)\s*to\s*(\d+\s*V)", re.IGNORECASE)
        match = pattern.search(text)
        if match:
            return f"{match.group(1)} to {match.group(2)}"
        return None
    @staticmethod
    def process_file(file_path):
        """Processes a single text file and extracts operating ranges."""
        with open(file_path, 'r') as file:
            text = file.read()
            operating_temperature_range = ComponentExtractor.get_operating_temperature_range(text)
            operating_voltage_range = ComponentExtractor.get_operating_voltage_range(text)
            return operating_temperature_range, operating_voltage_range
