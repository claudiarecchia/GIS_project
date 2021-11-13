
from pygeos_and_shapely.init_folders_and_files import *

if __name__ == "__main__":
    create_folders()
    create_all_values()
    create_trials_folder()
    create_trials()

    polygons, linestrings, points = [], [], []
    points_strings = read_nodes_file(global_variables.trials_folder, global_variables.points_file)
    points = get_int_values(points_strings)

    for file in global_variables.linestrings:
        points_strings = read_nodes_file(global_variables.trials_folder, file)
        linestrings.extend(get_int_values(points_strings))

    for file in global_variables.polygons:
        points_strings = read_nodes_file(global_variables.trials_folder, file)
        polygons.extend(get_int_values(points_strings))

    exit_if_not_JEPD(points, linestrings, polygons)
    calculate_composition_tables(points, linestrings, polygons)

