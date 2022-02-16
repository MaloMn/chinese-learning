"""
Objective: Building a simple example anki deck containing two chinese characters
wo and ni.
"""

import genanki


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

    output = "<svg viewBox=\"0 0 1024 1024\"><g transform=\"scale(1, -1) translate(0, -900)\">"
    for g in data["strokes"]:
        output += "<path d=\"" + g + "\"></path>"
    output += "</g></svg>"

    return output


def save_svg(filename, svg):
    with open(filename, "w+") as f:
        f.write(svg)


characters = ["我", "你"]

# Reading lexical data
dict_data = filter_characters_from_file("initial-db/dictionary.txt", characters)
graph_data = filter_characters_from_file("initial-db/graphics.txt", characters)

for c in characters:
    save_svg("initial-db/svg/" + c + ".svg", generate_svg(graph_data, c))

"""
Needs a custom model id :
import random; random.randrange(1 << 30, 1 << 31)
"""


"""
main_model = genanki.Model(
  1463873326,
  'Chinese PinYin Audio',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
"""