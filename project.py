import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
import os
import argparse

sentence_list = []
word_list = []

parser = argparse.ArgumentParser(description='Read a text file and word list file and find sentences')
parser.add_argument('--book_name', required=True, help='Name of the book to read')
parser.add_argument('--word_list_file_name', required=True, help='Name of the word list to use')

args = parser.parse_args()

book_name = args.book_name 
word_list_file_name = args.word_list_file_name

with open(args.book_name, 'r', encoding="utf-8") as f:
    book_content = f.read()

    for sentence in sent_tokenize(book_content):
        sentence_list.append(sentence)

with open(args.word_list_file_name, 'r', encoding="utf-8") as f:
    vocab_content = f.read()

    for words in word_tokenize(vocab_content):
        word_list.append(words)

def check(sentence, words):
	res = [any([k in s for k in words]) for s in sentence]
	return [sentence[i] for i in range(len(res)) if res[i]]

result_list = check(sentence=sentence_list, words=word_list)

f = open('sentences_file.txt', 'x', encoding="utf-8")
with open('sentences_file.txt', 'w',  encoding="utf-8") as f:
    for n in result_list:
         f.write(n + "\n")
