# -*- coding: utf-8 -*-
"""#7 Basic techniques to process texts

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MdpnezKl4LXAh9f6bQYjnc3WJSMSdsB9?usp=sharing

# **Basic techniques to process texts**

"""

pip install polyglot pyicu pycld2 morfessor

from polyglot.text import Text

# Enter a text and process it
text = u"""Francoise Sagan de la France: Sur ce sentiment inconnu dont l'ennui, 
la douceur m'obsèdent, j'hésite à apposer le nom, le beau nom grave de tristesse. 
C'est un sentiment si complet, si égoïste que j'en ai presque honte alors que 
la tristesse m'a toujours paru honorable."""
ptext = Text(text)

# Detect language, sentences and words
print(ptext.language)
print(ptext.sentences)
print(ptext.words)
print('There are %.u words in this text' % len(ptext.words))

# Download language specific data
%%bash
polyglot download pos2.fr ner2.fr morph2.fr embeddings2.fr transliteration2.fr transliteration2.ar

# Detect parts of speech and named entities
print(ptext.pos_tags)
print(ptext.entities)

# Morphological analysis
words = ptext.words
for w in words:
  print("{:<20}{}".format(w, w.morphemes))

# Transliterate into Arabic ligature
for fr, ar in zip(ptext.words, ptext.transliterate('ar')):
  print('{:<15}{}'.format(fr, ar))
