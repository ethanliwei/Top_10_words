# This scrip is use to list top 10 frequency words in a txt file 
from sys import argv
from os.path import exists

scrip, input_file = argv

# First, you should copy all words of a file to input.txt
print "Dose the input.txt exist? %r" % exists(input_file)
print "if false then you should creat a input.txt"

in_file = open(input_file)
all_words = in_file.read()

words_list = all_words.split()

word_freq = [words_list.count(w) for w in words_list]

print("Words:\n {} \n".format(all_words))
print("List:\n {} \n".format(str(words_list)))
print("Frequencies:\n {} \n".format(str(word_freq)))
print("Pairs:\n {}".format(str(dict(zip(words_list, word_freq)))))
