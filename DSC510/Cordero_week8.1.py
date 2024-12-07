# DSC 510
# Week 8
# Programming Assignment Week 8
# Auther: Joaquin Cordero
# 5/4/2024
# This program will calculate the total words, and output the number of occurrences of each word in the file.
# ---------------------------------------------------
import string


def Process_line(line, word_count):
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        add_word(word, word_count)
    # This function will clean up the text


def add_word(word, word_count):
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
    # This function will add the word in the dictionary and add a count to duplicated words


def Pretty_print(word_count):
    print("Length of the dictionary:", len(word_count))
    print(f"{"Word"}           {"Count"}")
    print("_____________________")

    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    for key, value in sorted_word_count:
        print(f"{key: <17}{value}")
    # This function will print out the dictionary in a neat format


def main():
    word_count = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line, word_count)

    del word_count['']
    Pretty_print(word_count)


if __name__ == '__main__':
    main()