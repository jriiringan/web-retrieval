from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from heapq import nlargest
from operator import itemgetter
from nltk import*
import re
import collections
import trigram
import contraction
from string import digits
import time


class Graph(object):

    def plot_word(self, word):
        start_time = time.time()
        #words = re.sub(r'[^a-zA-Z]', r'', word)
        #words = ' '.join(words)
        word = re.sub('[^A-Za-z0-9]+', ' ', word)
        word = str(word).translate(None, digits)
        word_l = trigram.get_ngrams(str(word), 3)
        for nc in word_l:
            word += ''.join(contraction.expand_contractions(nc))
        words = dict(Counter(word.split()))
        
        words = sorted(words.items(), key=lambda x: x[1])
        words = dict(words)
        words = nlargest(10, words.iteritems(), key=itemgetter(1))
        words = dict(words)



        counter = words
        word_name = counter.keys()
        word_pos = word_tokenize(' '.join(word_name))
        
        word_pos = pos_tag(word_pos)
        word_name[:] = []
        for word,pos in word_pos:
            word_name.append(word)
        word_counts = counter.values()



        # Plot histogram using matplotlib bar().
        indexes = np.arange(len(word_name))
        width = 0.4
        plt.bar(indexes, word_counts, width)
        plt.xticks(indexes + width * 0.5, word_name, rotation = 'vertical',fontsize = 9)
        plt.xlabel('')
        plt.ylabel('Frequency')
        plt.title('Word Occurrence')
        #plt.savefig("image.png")
        print("Elapsed Time : %s seconds " % (time.time() - start_time))
        plt.show()
    def plot_pos(self, word):
        start_time = time.time()
        #word = re.sub(r'[^a-zA-Z]', ' ', word)
        word = re.sub('[^A-Za-z0-9]+', ' ', word)
        word = re.sub(r'\w*\d\w*', '', word).strip()
        word = str(word).translate(None, digits)
        word_l = trigram.get_ngrams(str(word), 3)
        for nc in word_l:
            word += ''.join(contraction.expand_contractions(nc))
        ps = word.split()
        pos_list = pos_tag(ps)
        pos_counts = collections.Counter((subl[1] for subl in pos_list))
        
        word_name = pos_counts.keys()
        word_counts = pos_counts.values()
        indexes = np.arange(len(word_name))

        
        width = 0.4
        plt.bar(indexes, word_counts, width)
        plt.xticks(indexes + width * 0.5, word_name, rotation = 'vertical', fontsize = 10)
        plt.xlabel('')
        plt.ylabel('Frequency')
        plt.title('Part Of Speech')
        #plt.savefig("image.png")
        print("Elapsed Time : %s seconds " % (time.time() - start_time))
        plt.show()
        
