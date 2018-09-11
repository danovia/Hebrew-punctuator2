# coding: utf-8

from __future__ import division, print_function
from nltk.tokenize import word_tokenize

import nltk
import os
from io import open
import re
import sys

nltk.download('punkt')

NUM = '<NUM>'

EOS_PUNCTS = {".": ".PERIOD", "?": "?QUESTIONMARK", "!": "!EXCLAMATIONMARK"}
INS_PUNCTS = {",": ",COMMA", ";": ";SEMICOLON", ":": ":COLON", "-": "-DASH"}

forbidden_symbols = re.compile(r"[\[\]\(\)\/\\\>\<\=\+\_\*]")
numbers = re.compile(r"\d")
multiple_punct = re.compile(r'([\.\?\!\,\:\;\-])(?:[\.\?\!\,\:\;\-]){1,}')

is_number = lambda x: len(numbers.sub("", x)) / len(x) < 0.6

def untokenize(line):
    return line.replace(" '", "'").replace(" n't", "n't").replace("can not", "cannot")

def skip(line):

    if line.strip() == '':
        return True

    last_symbol = line[-1]
    if not last_symbol in EOS_PUNCTS:
        return True

    if forbidden_symbols.search(line) is not None:
        return True

    return False

def process_line(line, to_concat_morphmemes):

    tokens = word_tokenize(line)
    output_tokens = []

    prev_morphemes = []
    for token in tokens:

        delete_morphemes = True

        if token in INS_PUNCTS:
            output_tokens.append(INS_PUNCTS[token])
        elif token in EOS_PUNCTS:
            output_tokens.append(EOS_PUNCTS[token])
        elif is_number(token):
            output_tokens.append(NUM)
        elif to_concat_morphmemes and len(token) == 1:
            prev_morphemes.append(token.lower())
            delete_morphemes = False
        else:
            full_word = "".join(prev_morphemes) + token.lower()
            output_tokens.append(full_word)

        if delete_morphemes:
            prev_morphemes = []

    return untokenize(" ".join(output_tokens) + " ")

skipped = 0

with open(sys.argv[2], 'w', encoding='utf-8') as out_txt:
    with open(sys.argv[1], 'r', encoding='utf-8') as text:

        for line in text:

            line = line.replace("\"", "").strip()
            line = multiple_punct.sub(r"\g<1>", line)

            if skip(line):
                skipped += 1
                continue

            line = process_line(line, bool(int(sys.argv[3])))

            out_txt.write(line + '\n')

print("Skipped %d lines" % skipped)
