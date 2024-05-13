class ElectricalComponent:
    def __init__(self, name, operating_voltage_range, operating_temperature_range):
        self.name = name
        self.operating_voltage_range = operating_voltage_range
        self.operating_temperature_range = operating_temperature_range

    def __str__(self):
        return f"Component: {self.name}\nOperating Voltage Range: {self.operating_voltage_range}\nOperating " \
               f"Temperature Range: {self.operating_temperature_range}"

    def is_within_ranges(self, voltage, temperature):
        voltage_min, voltage_max = map(int, self.operating_voltage_range.split(' - '))
        temperature_min, temperature_max = map(int, self.operating_temperature_range.split(' - '))

        if voltage_min <= voltage <= voltage_max and temperature_min <= temperature <= temperature_max:
            return True
        else:
            return False
