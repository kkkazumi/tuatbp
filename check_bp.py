import glob
from natsort import natsorted
import numpy as np

counts=[45,35,25]

def get_sort_files(path):
    """
    usage:
    (i) :get_sort_files('dir/*')
    (ii):get_sort_files('dir/*.txt')
    """
    files = glob.glob(path)
    return natsorted(files)

print("input user id: MS00")
userid = input()
target_dir = "/home/kazumi/prog/tuatbp/BP/"+userid+"/*.npy"
for npyfile in get_sort_files(target_dir):
    data=np.load(npyfile)
    print(npyfile)
    print(data)
