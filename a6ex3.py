import os
from os import walk

def get_abs_paths(root_path: str, ext_filter: str = None) -> list:
    
    if os.path.isdir(root_path) == False: 
        return "ValueError"
    else:
        if ext_filter == None:
            file = [f for f in os.listdir(root_path)]
            return file
        elif ext_filter[0] == ".":
            file = [f for f in os.listdir(root_path) if f.endswith(ext_filter)]
            return file
        else:
            return "ValueError"
            
get_abs_paths('/Users/tomi/Documents/jku/jelenlegi feladat/Programing in Python I/Assigments/6')
