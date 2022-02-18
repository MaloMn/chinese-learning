"""
Objective: Building a simple example anki deck containing two chinese characters
wo and ni.
"""

import genanki
import json

characters = ["我", "你"]

"""
Generate SVG files for wanted characters
"""


def filter_characters_from_file(file_name, characters):
    output = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            try:
                parsed = eval(line)
                if parsed["character"] in characters:
                    output.append(parsed)
            except NameError:
                pass
            except SyntaxError:
                pass
    return output


def generate_svg(graphics, character):
    data = next(filter(lambda x: x["character"] == character, graphics))

    output = "<svg viewBox=\"0 0 1024 1024\"><g color=\"white\" transform=\"scale(1, -1) translate(0, -900)\">"
    for g in data["strokes"]:
        output += "<path fill=\"currentcolor\" d=\"" + g + "\"></path>"
    output += "</g></svg>"

    return output


def save_svg(filename, svg):
    with open(filename, "w+") as f:
        f.write(svg)


"""
# Reading lexical data
dict_data = filter_characters_from_file("initial-db/dictionary.txt", characters)
graph_data = filter_characters_from_file("initial-db/graphics.txt", characters)

for c in characters:
    save_svg("initial-db/svg/" + c + ".svg", generate_svg(graph_data, c))
"""

images = {c: "initial-db/svg/" + c + ".svg" for c in characters}

"""
Find corresponding audio files, pinyins & translations
"""

with open("initial-db/output.json", "r") as f:
    data_audios = json.load(f)

audios = {c: "initial-db/deck/" + data_audios[c][2] for c in characters}
pinyins = {c: data_audios[c][0] for c in characters}
translations = {c: data_audios[c][1] for c in characters}

"""
Needs a custom model id :
import random; random.randrange(1 << 30, 1 << 31)
"""


class MyNote(genanki.Note):
  @property
  def guid(self):
    return genanki.guid_for(self.fields[0], self.fields[1])


my_deck = genanki.Deck(
  2059400110,
  'Chinese HSK 1')

"""
List of cards to be generated:
 - drawn character to english translation
 - drawn character to pinyin
 - pinyin to translation
 - english translation to pinyin
 - audio to translation
 - translation to audio
"""


my_model = genanki.Model(
  1091735104,
  'Main Model',
  fields=[
    {'name': 'Audio'},
    {'name': 'DrawnCharacters'},
    {'name': 'PinYin'},
    {'name': 'Translation'},
  ],
  templates=[
    {
      'name': 'CharactersToEnglish',
      'qfmt': '{{Question}}<br>{{MyMedia}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires'])

my_deck.add_note(my_note)

my_package = genanki.Package(my_deck)
my_package.media_files = ['sound.mp3', 'images/image.jpg']


