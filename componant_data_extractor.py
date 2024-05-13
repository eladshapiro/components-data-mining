import re


class ComponentExtractor:
    @staticmethod
    def get_operating_temperature_range(text):
        """Extracts the operating temperature range from the given text."""
        pattern = r"(-?\d+(\.\d+)?)\s*°?[CcFfKk]?\s*to\s*(-?\d+(\.\d+)?)\s*°?[CcFfKk]?"
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Unpack the match into separate groups
            min_temp, _, max_temp, _ = matches[0]
            # Convert extracted temperatures to floats
            min_temp = float(min_temp)
            max_temp = float(max_temp)
            # Ensure the min temperature is less than the max temperature
            if min_temp <= max_temp:
                return f"{min_temp}°C to {max_temp}°C"
        # Return None if no valid range found
        return None

    @staticmethod
    def get_operating_voltage_range(text):
        """Extracts the operating voltage range from the given text."""
        pattern = r"(\d+(\.\d+)?)\s*[Vv]?\s*to\s*(\d+(\.\d+)?)\s*[Vv]?"
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Take the first match as the voltage range
            min_volt, _, max_volt, _ = matches[0]
            # Convert extracted voltages to floats
            min_volt = float(min_volt)
            max_volt = float(max_volt)
            # Ensure the min voltage is less than the max voltage
            if min_volt <= max_volt:
                return f"{min_volt}V to {max_volt}V"
        # Return None if no valid range found
        return None

    @staticmethod
    def process_file(file_path):
        """Processes a single text file and extracts operating ranges."""
        with open(file_path, 'r') as file:
            text = file.read()
        operating_temperature_range = ComponentExtractor.get_operating_temperature_range(text)
        operating_voltage_range = ComponentExtractor.get_operating_voltage_range(text)
        return operating_temperature_range, operating_voltage_range

    @staticmethod
    def parse_range(range_str):
        """Parses the extracted range string into a tuple of floats."""
        if range_str is None:
            return None
        # Remove unit symbols and split the range string
        range_cleaned = range_str.replace('V', '').replace('°C', '')
        range_values = list(map(float, range_cleaned.split(' to ')))
        if len(range_values) == 1:
            return range_values[0], range_values[0]
        elif len(range_values) == 2:
            return range_values[0], range_values[1]
        else:
            raise ValueError("Invalid range format")
