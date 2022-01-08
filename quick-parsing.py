import json

# read the file output.json
import os

with open("database.json", 'r') as f:
    data = json.load(f)

audios = {a[2] for a in data.values() if a[2] != ""}

print(audios)

files = os.listdir("audio")
files = {a.replace(".mp3", "") for a in files}

print(files)

print(len(audios.intersection(files)), audios.intersection(files))
print(len(audios - files), audios - files)
print(len(files - audios), files - audios)
