import pandas as pd
import math
from multiprocessing import Pool

files = list(range(0,10))

def add_dean(x):
    return(str(math.sqrt(2)) +" Dean")

def execute(file):

    output_list=[]
    print(file)
    output_list.append(add_dean(file))
    return(output_list)
    
if __name__ == '__main__':
    p = Pool(10)


    no_files = 5000
    files = list(range(0,no_files))

    lib = p.map(execute,files)

    print("Total files processed: %d\nNumber of unique values are:" %(len(lib)))