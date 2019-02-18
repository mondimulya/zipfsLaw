"""
CSAPX - Project 1 (Python)
A program to count the total number of occurrences
of a word across the year.

word_count.py
author: Mondi Mulya
"""

import collections
import argparse
import sys
import os

Word = collections.namedtuple('Dictionary',
                              ('word', 'year', 'counting'))

def read_test(filename):
    """
    to read the file and store it into a list
    :param filename: name of a file
    :return: a list Word with the following values: word, year, number of appearances
    """
    words = list()
    with open(filename) as f:
        for line in f:
            fields = line.split(',')
            words.append(Word(word=fields[0], year=int(fields[1]), counting=int(fields[2])))
    return words

def word_counting(words_collect):
    """
    To count the total occurrences of each word and store it into a dictionary.
    :param words_collect: a list from read_test
    :return: a dictionary, key: word, value: total occurrences
    """
    counting = {}
    for data in words_collect:
        if data[0] not in counting:
            counting[data[0]] = data[2]
        else:
            counting[data[0]] += data[2]
    return counting

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Counting words')
    parser.add_argument('word', type=str, help='a word to display a total occurrences of')
    parser.add_argument('filename', type=str, help='a comma separated value unigram file')
    args = parser.parse_args()
    try:
        os.stat(args.filename)
    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!")
    else:
        words_collect = read_test(args.filename)
        new_word = word_counting(words_collect)
        if args.word in new_word.keys():
            print(args.word + ': ' + str(new_word[args.word]))
        else:
            sys.stderr.write("Error: " + args.word + " does not appear!")

if __name__ == '__main__':
    main()
