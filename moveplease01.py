#!/usr/bin/env python3

import shutil
import os

# chang dir
os.chdir('/home/student/mycode-110722/')

# move file
shutil.move('raynor.obj', 'ceph_storage/')

# user input
xname = input('What is the new name for kerrigan.obj? ')

# rename
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


