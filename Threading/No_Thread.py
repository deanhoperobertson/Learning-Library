import pandas as pd
import math
from multiprocessing import Pool

files = list(range(0,10))

def add_dean(x):
    return(str(math.sqrt(2)) +" Dean")

def execute(files):
    output_list=[]
    for file in files:
        print(file)
        output_list.append(add_dean(file))
    return(output_list)


if __name__ == '__main__':
    
    no_files = 10000
    files = list(range(0,no_files))

    lib = execute(files)

    print("Total files processed: %d\nNumber of unique values are:" %(len(lib)))