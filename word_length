"""
A program to calculate the average length of words
of a particular year.

word_length.py
author: Mondi Mulya
"""

import collections
import sys
import argparse
import matplotlib.pyplot as plt
import os

Word = collections.namedtuple('Dictionary',
                              ('word', 'year', 'counting'))

def read_test(filename):
    """
    to read the file
    :param filename:
    :return:
    """
    words = list()
    with open(filename) as f:
        for line in f:
            fields = line.split(',')
            words.append(Word(word=fields[0], year=int(fields[1]), counting=int(fields[2])))
    return words

def length_avg(words_collect):
    """
    one step to find the length average by using two dictionaries
    :param words_collect: a list from read_test
    :return: words: a dictionary, keys: year, values: total lengths of words over the years,
             sum: a dictionary, keys: year, values: total words over the years
    """
    sum = {}
    words = {}
    for data in words_collect:
        if data[1] not in words:
            words[data[1]] = data[2]*len(data[0])
        else:
            words[data[1]] += data[2] * len(data[0])
        if data[1] not in sum:
            sum[data[1]] = data[2]
        else:
            sum[data[1]] += data[2]
    return words, sum

def plot(dictionary, start, end, filename):
    """
    to plot the average word lengths over years
    :param dictionary: a dictionary, keys: year, values: average length of each word
    :param start: start year
    :param end: end year
    :param filename: name of file used
    :return: a line graph
    """
    data = {"x": [], "y": []}
    for coord in dictionary.items():
        data["x"].append(coord[0])
        data["y"].append(coord[1])
    plt.plot(data["x"],data["y"])
    plt.title("Average word lengths from "+ str(start)+ " to " + str(end)+ ": " + filename, fontsize=20)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Average word length', fontsize=12)
    plt.show()

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Word Average Length')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o', '--output', action='store_true', help='display the average word lengths over the years')
    parser.add_argument('-p', '--plot', action='store_true',
                        help='plot the average word lengths over years')
    parser.add_argument('start', type=int, help='the starting year range')
    parser.add_argument('end', type=int, help='the ending year range')
    parser.add_argument('filename', type=str, help='a comma separated value unigram file')
    args = parser.parse_args()
    try:
        os.stat(args.filename)
    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!")
    else:
        if args.start > args.end:
            sys.stderr.write("Error: start year must be less than or equal to end year!")
        else:
            words_collect = read_test(args. filename)
            dictionary, sum = length_avg(words_collect)
            finalAvgDict = {}
            if args.output:
                for i in range (args.start, args.end+1, 1):
                    if i in dictionary:
                        print(str(i) + ": " + str(dictionary[i]/sum[i]))
                        finalAvgDict[i] = dictionary[i]/sum[i]
            if args.plot:
                plot(finalAvgDict, args.start, args.end, args.filename)

if __name__ == '__main__':
    main()
