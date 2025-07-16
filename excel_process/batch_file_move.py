"""
Version: 1.5

Summary: Process all skeleton graph data in each individual folders

Author: suxing liu

Author-email: suxingliu@gmail.com

USAGE:

    python3 batch_file_move.py -i /input/ -o /output/

"""

import subprocess, os
import sys
import argparse
import numpy as np 
import pathlib
import os
import glob
import shutil

import pathlib


# generate foloder to store the output results
def mkdir(path):
    # import module
    import os
 
    # remove space at the beginning
    path=path.strip()
    # remove slash at the end
    path=path.rstrip("\\")
 
    # path exist?   # True  # False
    isExists=os.path.exists(path)
 
    # process
    if not isExists:
        # construct the path and folder
        #print path + ' folder constructed!'
        # make dir
        os.makedirs(path)
        return True
    else:
        # if exists, return 
        #print path+' path exists!'
        #shutil.rmtree(path)
        #os.makedirs(path)
        return False
        



# execute script inside program
def execute_script(cmd_line):
    
    try:
        #print(cmd_line)
        #os.system(cmd_line)

        process = subprocess.getoutput(cmd_line)
        
        print(process)
        
        #process = subprocess.Popen(cmd_line, shell = True, stdout = subprocess.PIPE)
        #process.wait()
        #print (process.communicate())
        
    except OSError:
        
        print("Failed ...!\n")




# execute pipeline scripts in order
def file_move(source_file_path, target_file_path):
    
    
    batch_cmd = "cp " + source_file_path + " " + target_file_path
    
    print(batch_cmd)
    
    execute_script(batch_cmd)




# execute pipeline scripts in order
def folder_delete(file_path):
    
    isExists = os.path.exists(file_path)
    
    if isExists:
        
        shutil.rmtree(file_path)
    else:
        print("Path {} not exist!\n".format(file_path))
        

def create_folders(genotype_list):
    
    for item in genotype_list:
        
        folder_path = current_path + item + '/'
        
        mkdir(folder_path)


def fast_scandir(dirname):
    
    subfolders= sorted([f.path for f in os.scandir(dirname) if f.is_dir()])
    
    return subfolders
    



# get file information from the file path using python3
def get_file_info(file_full_path):
    
    p = pathlib.Path(file_full_path)

    filename = p.name

    basename = p.stem

    file_path = p.parent.absolute()

    file_path = os.path.join(file_path, '')

    return file_path, filename, basename


if __name__ == '__main__':
    
    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path", required = True, help = "path to individual folders")
    ap.add_argument("-o", "--target_path", required = False, help = "path to target folders")
    args = vars(ap.parse_args())
    
    
   
    
    #parameter sets
    # path to individual folders
    current_path = args["path"]
    
    target_path = args["target_path"]
    
    subfolders = fast_scandir(current_path)
    
    #print("Processing folder in path '{}' ...\n".format(subfolders))

    
    #loop execute
    for subfolder_id, subfolder_path in enumerate(subfolders):

        #######################################################
        #folder_name = os.path.basename(subfolder_path)
        
        (file_path, filename, basename) = get_file_info(subfolder_path)
        
        source_file = subfolder_path + '/' + basename + '_aligned_trait.xlsx'

        target_file = target_path + basename + '.xlsx'
        
        print("Moving file '{}' to '{}'\n".format(source_file, target_file))
        
        file_move(source_file, target_file)
        
        
        

    

