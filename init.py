from glob import glob
import os
import json
import hashlib

paths = glob('*/*/*/template.prob')

for i in paths:
    if not os.path.isdir(os.path.join(os.path.abspath(os.path.join(i, os.pardir)), ".cph")):
        os.mkdir(os.path.join(os.path.abspath(os.path.join(i, os.pardir)), ".cph"))
        with open(i) as r:
            j = json.loads(r.read())
        j["srcPath"] = os.path.abspath(j["srcPath"]).replace("C:\\", "c:\\")
        with open(i, "w") as w:
            w.write(json.dumps(j))
        os.replace(i, os.path.join(os.path.abspath(os.path.join(i, os.pardir)), ".cph", ".problem.py_" + hashlib.md5(j["srcPath"].encode()).hexdigest() + ".prob"))
