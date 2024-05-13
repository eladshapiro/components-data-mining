from ComponentSearcher import ComponentSearcher
from component_manager import ComponentManager


def main():
    directory = "Task example files"

    component_manager = ComponentManager(directory)
    component_manager.load_component_files()
    component_manager.process_component_files()
    components = component_manager.create_components()

    # Print components
    for component in components:
        print(component)
        print()

    searcher = ComponentSearcher(directory)
    searcher.search_components()


if __name__ == "__main__":
    main()
