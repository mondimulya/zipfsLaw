"""
A program to count the total number of occurrences
of a word across the years.

word_freq.py
author: Mondi Mulya
"""

import collections
import sys
import argparse
import os
import matplotlib.pyplot as plt
from collections import OrderedDict

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

def word_freq(words_collect):
    """
    to find the frequencies of each word, then sort it in descending order based on values
    :param words_collect: a list from read_test
    :return: a descending-order dictionary, keys: word, values = frequency
    """
    freq = {}
    for word in words_collect:
        if word[0] not in freq:
            freq[word[0]] = word[2]
        else:
            freq[word[0]] += word[2]
    sorted_freq = OrderedDict(sorted(freq.items(), key=lambda v: v[1], reverse=True))
    return sorted_freq

def plot(word, dictionary, xPos, yPos, filename):
    """
    to plot the word rankings from top to bottom based on occurences
    :param word: the assigned word
    :param dictionary: the sorted dictionary from word_freq
    :param xPos: x-Position of the word assigned
    :param yPos: y-Position of the word assigned
    :param filename: name of file used
    :return: a graph of word frequencies
    """
    data = {"x": [], "y": []}
    count = 1
    for i in range(0, len(dictionary), 1):
        data["y"].append(dictionary[(list(dictionary)[i])])
        data["x"].append(count)
        count+=1
    plt.scatter(data["x"], data["y"], color="brown")
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(data["x"], data["y"], color="pink")
    plt.plot(xPos, yPos, marker=r'$\clubsuit$', markersize=16, color="green")
    plt.text(xPos, yPos+70000, word, fontsize=12)
    plt.title('Word Frequencies: ' + filename, fontsize=20)
    plt.xlabel('Rank of word("'+word+'" is rank '+ str(xPos)+')', fontsize=12)
    plt.ylabel('Total number of occurrences', fontsize=12)
    plt.show()


def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Counting words')
    parser.add_argument('-o', '--output', type=int, help='display the top OUTPUT (#) ranked words by number of occurrences')
    parser.add_argument('-p', '--plot', action= 'store_true', help='plot the word rankings from top to bottom based on occurences')
    parser.add_argument('word', type=str, help='a word to display the overall ranking')
    parser.add_argument('filename', type=str, help='a comma separated value unigram file')
    args = parser.parse_args()
    try:
        os.stat(args.filename)
    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!")
    else:
        words_collect = read_test(args.filename)
        sorted_freq = word_freq(words_collect)
        if args.word not in sorted_freq.keys():
            sys.stderr.write("Error: " + args.word + " does not appear in " + args.filename)
        else:
            standing = list(sorted_freq.keys()).index(args.word) + 1
            print(args.word + " is ranked #" + str(standing))
            if args.output:
                for i in range (0, args.output, 1):
                    print("#" + str(i+1) + ": " + str(list(sorted_freq)[i]) + " -> " + str(sorted_freq[(list(sorted_freq)[i])]))
            if args.plot:
                plot(args.word, sorted_freq, standing, sorted_freq[args.word], args.filename)

if __name__ == '__main__':
    main()
