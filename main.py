from electrical_component import ElectricalComponent
from componant_data_extractor import ComponentExtractor
import os


def main():
    directory = "Task example files"

    components = []  # List to store instances of ElectricalComponent

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            temperature_range, voltage_range = ComponentExtractor.process_file(file_path)
            component_name = os.path.splitext(filename)[0]  # Extract component name from file name
            component = ElectricalComponent(component_name, voltage_range, temperature_range)
            components.append(component)

    # Print components
    for component in components:
        print(component)
        print()


if __name__ == "__main__":
    main()
