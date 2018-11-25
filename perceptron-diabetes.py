# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:56:36 2018

@author: 7
"""

from random import seed
from random import randrange
from csv import reader

# fungsi load file CSV
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# evaluasi algoritma
n_folds = 5
l_rate = 0.01
n_epoch = 1000
scores = evaluate_algorithm(dataset, perceptron, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))