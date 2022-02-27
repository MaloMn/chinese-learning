# Load the sqlite module and create a cursor to the database
import sqlite3
import json

conn = sqlite3.connect('deck/collection.sqlite')
c = conn.cursor()

# Loading audio files links

with open("deck/media") as f:
    data = json.load(f)

audio_to_nb = {}
for (key, val) in data.items():
    audio_to_nb[val] = key

print(audio_to_nb)

output = dict()

# Query columns of interest and print each row
# You can query all columns using `*` in place of field names
for row in c.execute('SELECT id, guid, flds, sfld FROM notes ORDER BY sfld'):
    # Each `row` will be a tuple with as many entries as field queried
    # print(row)
    # Voluntarily ignoring ids
    # id = row[0]
    # guid = row[1]
    flds = row[2]
    chinese = row[3]
    pinyin, english, audio = flds.split("\x1f")[1:]
    audio = audio.replace("[sound:", "")
    audio = audio.replace("]", "")
    print(flds)

    try:
        audio = audio_to_nb[audio]
    except KeyError:
        pass

    print(chinese, pinyin, english, audio)

    output[chinese] = [pinyin, english, audio]

    # (You cannot manipulate the database directly here)

with open('output.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False)
