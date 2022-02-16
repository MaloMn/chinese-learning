"""
Objective: Building a simple example anki deck containing two chinese characters
wo and ni.
"""

import genanki

"""
Needs a custom model id :
import random; random.randrange(1 << 30, 1 << 31)
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