"""
A program to display the letter frequencies
across the years.

letter_freq.py
author: Mondi Mulya
"""

import collections
import sys
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np

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

def letter_freq(words_collect):
    """
    to find the frequency of each letter and store it into a dictionary.
    :param words_collect: a list from read_test
    :return: a dictionary (freq), key: letter (a-z) , value: frequency of each letter
    """
    sum = 0
    freq = dict([(chr(i),0) for i in range(ord('a'),ord('z')+1)])
    for data in words_collect:
        for char in data[0]:
            if char in freq:
                freq[char] += data[2]
            sum += data[2]
    for letter in freq:
        freq[letter] /= sum
    return freq

def draw_plot(frequency,filename):
    """
    to draw bar graph of letter frequencies.
    :param frequency: a dictionary, keys: a-z, values: frequency
    :param filename: name of file used
    :return:
    """
    data = {"x": [], "y": []}
    for coord in frequency.items():
        data["x"].append(coord[0])
        data["y"].append(coord[1])
    ypos = np.arange(len(data["x"]))
    plt.figure(figsize=(10, 8))
    plt.title('Letter Frequencies: ' + filename, fontsize=20)
    plt.xticks(ypos, data["x"])
    plt.xlabel('Letter', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.bar(ypos, data["y"], color='pink')
    plt.show()

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Letter Frequency')
    parser.add_argument('-o','--output', action='store_true', help='display letter frequencies to standard output')
    parser.add_argument('-p','--plot', action='store_true', help='plot letter frequencies using matplotlib')
    parser.add_argument('filename', type=str, help='a comma separated value unigram file')
    args = parser.parse_args()
    try:
        os.stat(args.filename)
    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!")
    else:
        if args.output:
            frequency = letter_freq(read_test(args.filename))
            for k, v in frequency.items():
                print(k + ": " + str(v))
        if args.plot:
            draw_plot(frequency, args.filename)

if __name__ == '__main__':
    main()
