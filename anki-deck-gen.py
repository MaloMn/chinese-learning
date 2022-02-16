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
    return output


characters = ["我", "你"]

# Reading lexical data
dict_data = filter_characters_from_file("initial-db/dictionary.txt", characters)
graph_data = filter_characters_from_file("initial-db/graphics.txt", characters)

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