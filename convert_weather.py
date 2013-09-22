#! /usr/bin/env python

import json
import re

WEATHER_RX = r'public static const ([A-Z_]*):Object = ({[^\}]*})'
PROP_RX = r':([^,\n]*)([,\n])'

# weatherfile = open('Weather.as').read()
# jsonfile = open("weathers.json",'w')

# weathers = {}
# for a in re.findall(WEATHER_RX, weatherfile, re.DOTALL):
#     print a[0]
#     w = re.sub(PROP_RX, r':"\1"\2', a[1])
#     w = w.replace("'",'"')
#     weathers[a[0]] = json.loads(w)
#     
# json.dump(weathers, jsonfile, indent=2)
# 

presets = open('WeatherPresets.as', 'w')

presets.write("// THIS FILE IS AUTOGENERATED, MODIFY weathers.json IN STEAD.\n\n")
presets.write("package {\n")
presets.write("public class WeatherPresets extends Object{\n")

weathers = json.load(open('weathers.json'))

print "Found: \n- " + '\n- '.join(sorted(weathers.keys()))

for weather, content in weathers.items():
    presets.write("\tpublic static const %s:Object = {\n" % (weather))
    presets.write(',\n'.join(["\t\t'%s': %s" % (key,val) for key, val in content.items()]))
    presets.write('\n\t}\n')
    
    
presets.write("}\n}")