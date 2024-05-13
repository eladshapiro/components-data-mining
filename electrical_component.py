def parse_input_range(input_str):
    # Remove 'V' or 'C' characters from the input string
    input_str = input_str.replace('V', '').replace('C', '').replace('°', '')

    # If the input contains a single value, return it as a float
    if ' to ' not in input_str:
        return float(input_str.strip())

    # If the input contains a range, split and return as a tuple of floats
    min_value, max_value = map(float, input_str.split(' to '))
    return min_value, max_value


class ElectricalComponent:
    def __init__(self, name, operating_voltage_range, operating_temperature_range):
        self.name = name
        self.operating_voltage_range = operating_voltage_range
        self.operating_temperature_range = operating_temperature_range if operating_temperature_range else "Not " \
                                                                                                           "specified"

    def __str__(self):
        voltage_range_str = f"{self.operating_voltage_range[0]} to {self.operating_voltage_range[1]}" if isinstance(
            self.operating_voltage_range,
            tuple) else f"{self.operating_voltage_range}" if self.operating_voltage_range else "Not specified"
        temperature_range_str = f"{self.operating_temperature_range[0]} to {self.operating_temperature_range[1]}" if isinstance(
            self.operating_temperature_range,
            tuple) else f"{self.operating_temperature_range}" if self.operating_temperature_range else "Not specified"
        return f"Component: {self.name}\nOperating Voltage Range: {voltage_range_str}\nOperating Temperature Range: {temperature_range_str}"

    def is_within_ranges(self, voltage, temperature):
        if voltage is None or temperature is None:
            return False

        if self.operating_voltage_range is not None and self.operating_voltage_range is not 'Not specified':
            voltage_min, voltage_max = parse_input_range(self.operating_voltage_range)

            if self.operating_temperature_range is not None and self.operating_temperature_range is not 'Not specified':
                temperature_min, temperature_max = parse_input_range(self.operating_temperature_range)

                return (voltage_min <= voltage[0]) and (voltage[1] <= voltage_max) and (
                            temperature_min <= temperature[0]) and (temperature[1] <= temperature_max)
        else:
            return False
