from pathlib import Path
import sys

initial_path = Path("spam") / "bacon" / "eggs"

print(initial_path)

joining_2_path_objects = Path("spam") / Path("bacon/eggs")

print(joining_2_path_objects)

joining_path_obj_to_contructed_path_obj = Path("spam") / Path("bacon", "eggs")

print(joining_path_obj_to_contructed_path_obj)

print(sys.platform)

home_folder = Path("C:/Users/Al")

sub_folder = Path("spam")

print(home_folder / sub_folder)

# either first or second MUST be a Path object
