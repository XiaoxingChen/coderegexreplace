import re
import sys
import json
import os
from sys import platform

if(len(sys.argv) < 2):
    tempfile = open('template.json','w')
    template = \
        {
            'targetpath':'/home/chenxx',
            'targetfile': ["surf_display.cpp", "surf_display.h"],
            'targettext': {"Imu":"Surf", "IMU":"SURF"}
        }
    tempfile.write(json.dumps(template, indent=4, ensure_ascii=False))
    tempfile.close()
    print("no input file")
    exit()

jsondata = {}
jsonfile = sys.argv[1]
# print(jsonfile)
with open(jsonfile, 'r', encoding='utf-8') as f:
    jsondata = json.loads(f.read())
    f.close()

replacedict = jsondata['targettext']

for file in jsondata["targetfile"]:
    targetfile = jsondata['targetpath'] + os.sep + file

    f = open(targetfile, 'r')
    targettext = f.read()
    f.close()

    os.rename(targetfile, targetfile + '.bak')

    f = open(targetfile, 'w')

    for key in replacedict:
        targettext = re.sub(key, replacedict[key], targettext)
    f.write(targettext)
    f.close()

