#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на
# экран только предложения, не содержащие запятых.


if __name__ == '__main__':
    with open('ind_1.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    sentences = text.split('.')
    del sentences[sentences.index('')]

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if ',' not in sentence:
            string = sentence
            print(string.strip())
            