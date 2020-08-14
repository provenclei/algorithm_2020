import glob
import os
import sys
import time
from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize


def find_all_files(src_root, pkg):
    all = []
    m = '/*'
    level = 0
    while True:
        fList = glob.glob(src_root + "/" + pkg + (m * level) + '/*.py')
        if len(fList) == 0:
            break
        all += fList
        level = level + 1
    return all


def file_to_ext(src_root, files):
    ext_list = []
    sr_len = len(src_root)
    for fName in files:
        f = fName[sr_len+1:]
        name = f[0:len(f)-3].replace('/', '.')
        print("fName:" + fName + ",f:" + f + ",name:" + name)
        ext_list.append(Extension(name, [f]))
    return ext_list


def file_rename(dir, pkg):
    m = '/*'
    level = 0
    while True:
        fList = glob.glob(dir + "/" + pkg + (m * level) + '/*.so')
        if len(fList) == 0:
            break
        level = level + 1
        for file in fList:
            fs = file.split("/")
            name = fs[len(fs)-1]
            ns = name.split(".")
            if len(ns) == 3:
                nname = ns[0] + "." + ns[2]
                nfile = file[0: len(file) - len(name)] + nname
                print("rename "+ file + " to " + nfile)
                os.rename(file, nfile)

starttime = time.time()
home = "."
pkg = "algo" # algo/util
build_dir = 'build'
find = False
for arg in sys.argv:
    if find:
        build_dir = arg
        find = False
        break
    if arg == '-b':
        find = True

for arg in sys.argv:
    if find:
        pkg = arg
        break
    if arg == '-pkg':
        find = True

fileList = find_all_files(home, pkg)
extensions = file_to_ext(home, fileList)

try:
    setup(
        ext_modules=cythonize(extensions),
        script_args=["build_ext", "-b", build_dir]  # "-t", build_tmp_dir
    )
except (Exception) as ex:
    print("error! ", ex.message)
else:
    file_rename(build_dir, pkg)

print("complate! time:", time.time()-starttime, 's')

# python setup.py -b ./lib -pkg algo/util
