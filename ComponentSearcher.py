from component_manager import ComponentManager


class ComponentSearcher:
    def __init__(self, directory):
        self.component_manager = ComponentManager(directory)

    def search_components(self):
        self.component_manager.load_component_files()
        self.component_manager.process_component_files()

        print("Please provide the operating conditions for the components:")

        # Prompt for operating voltage range
        voltage_input = input("For the operating voltage range:\n"
                              "- If the component operates at a specific voltage, enter the voltage value in volts ("
                              "e.g., 5).\n"
                              "- If the component operates within a range of voltages, enter the range in the format "
                              "'min - max' (e.g., 3 to 5): ")

        # Prompt for operating temperature range
        temperature_input = input("For the operating temperature range:\n"
                                  "- If the component operates at a specific temperature, enter the temperature value "
                                  "in degrees Celsius (e.g., 25).\n"
                                  "- If the component operates within a range of temperatures, enter the range in the "
                                  "format 'min - max' (e.g., 20 to 30): ")

        # Parse the input for voltage and temperature
        voltage_range = self.parse_input_range(voltage_input)
        temperature_range = self.parse_input_range(temperature_input)

        matching_components = self.component_manager.get_components_for_conditions(voltage_range, temperature_range)

        if matching_components:
            print("Components that can operate under the provided conditions:")
            for component in matching_components:
                print(component)
                print()
        else:
            print("No components found for the provided conditions.")

    def parse_input_range(self, input_str):
        # If the input contains a single value, return it as a float
        if ' to ' not in input_str:
            return float(input_str.strip())

        # If the input contains a range, split and return as a tuple of floats
        min_value, max_value = map(float, input_str.split(' to '))
        return min_value, max_value
