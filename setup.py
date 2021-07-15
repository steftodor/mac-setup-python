import sys
import os
import json

with open('./config.json') as configFile:
    config = json.load(configFile)


for b in config["brew"]:
    os.system("brew install " + b)

for c in config["cask"]:
    os.system("brew install --cask " + c)


for e in config["codeExtension"]:
    os.system("code --install-extension " + e)

for d in config["defaultsWrite"]:
    os.system(d)
for other in config["other"]:
    os.system(other)