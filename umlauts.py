#!/usr/bin/python2
# -*- coding: utf-8 -*-


def translate(text):
    new_text=""
    for char in text:
        if translation_table.get(char):
            new_text += translation_table.get(char)
        else:
            new_text += char
    return new_text

translation_table={"�":"Ae", "�":"ae", "�":'Oe', "�":"oe", "�":"Ue", "�":"ue", "�":"ss"}
print translate("�sterreich ist �usserst fu�lastig")
