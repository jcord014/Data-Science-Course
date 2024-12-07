# DSC 510
# Week 9
# Programming Assignment Week 9
# Auther: Joaquin Cordero
# 5/10/2024
# This program will calculate the total words, and output the number of occurrences of each word in the file.

# Change Control Log:
# Change#1
# Change(s) Made:
#   Added new function called 'process_file', it will generate a new file using the file name the user wishes to use
#   lines(48-61)
# Date of change: 5/10/2024
# Author: Joaquin Cordero
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


# def Pretty_print(word_count):
#     print("Length of the dictionary:", len(word_count))
#     print(f"{"Word"}           {"Count"}")
#     print("_____________________")
#
#     sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
#
#     for key, value in sorted_word_count:
#         print(f"{key: <17}{value}")
    # This function will print out the dictionary in a neat format


def process_file(word_count, new_file_name):

    with open('gettysburg.txt', 'r') as gba_file:

        with open(new_file_name, 'w') as new_file:

            new_file.write("Length of the dictionary: " + str(len(word_count)) + "\n")
            new_file.write(f"{"Word"}           {"Count"}" + "\n")
            new_file.write("_____________________" + "\n")

            sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

            for key, value in sorted_word_count:
                new_file.write(f"{key: <17}{value}" + "\n")
    # This function will write the output to a new file instead


def main():
    word_count = {}
    try:
        with open('gettysburg.txt', 'r') as gba_file:
            for line in gba_file:
                Process_line(line, word_count)

            del word_count['']

            new_file_name = input("Please enter a name for the report: ")

            process_file(word_count, new_file_name)

    except FileNotFoundError:
        print("This file does not exist")


if __name__ == '__main__':
    main()