from glob import glob
import os
import json
import hashlib

paths = glob('*/*/*/template.prob')

for i in paths[:1]:
    os.mkdir(os.path.join(os.path.abspath(os.path.join(i, os.pardir)), ".cph"))
    with open(i) as r:
        srcPath = json.loads(r.read())["srcPath"]
    os.replace(i, os.path.join(os.path.abspath(os.path.join(i, os.pardir)), ".cph", ".problem.py_" + hashlib.md5(srcPath.encode()).hexdigest() + ".prob"))

        