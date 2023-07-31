import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
import os
import argparse
import re

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

def check(sentences, words):
	res = [any([k in s for k in words]) for s in sentences]
	return [sentences[i] for i in range(len(res)) if res[i]]

def list_sentences_with_words(sentences, words):
    result = []
    for sentence in sentences:
        clean_sentence = re.sub(r'[^\w\s]', '', sentence.replace('\n', ' ')).strip()
        words_found = [word for word in words if any(word == token for token in clean_sentence.split())]
        if words_found:
            result.append((clean_sentence, words_found))
    return result

result_list = list_sentences_with_words(sentences=sentence_list, words=word_list)
try:
    f = open('sentences_file.txt', 'x', encoding="utf-8")
except FileExistsError:
    print("File already exists")

with open('sentences_file.txt', 'w', encoding='utf-8') as f:
    for item in result_list:
        line = str(item) + '\n'
        f.write(line)



import json

cred_obj = firebase_admin.credentials.Certificate('nil03project.py')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://console.firebase.google.com/project/nil03project/database/nil03project-default-rtdb/data'})

ref = db.reference("/")
with open("nil03project.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
