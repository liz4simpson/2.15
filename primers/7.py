#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtledemo.penrose import f

if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as fileptr:
        sentences = f.readlines()

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            print(sentence)
