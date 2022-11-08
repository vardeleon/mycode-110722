#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/ """

import shutil  #shell utilities will be used to move files
import os      # OS operation

def main():
    # chang dir
    os.chdir('/home/student/mycode-110722/')

    # move file
    shutil.move('raynor.obj', 'ceph_storage/')

    # user input
    xname = input('What is the new name for kerrigan.obj? ')

    # rename
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if  __name__ == "__main__":
    main()
