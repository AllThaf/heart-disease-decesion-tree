from package.functions import *
from package.linkedList import LL
import random

def train_test_split(X, y, test_size):
  datas = shuffling(X, y)
  train = [datas[i] for i in range(round(len(datas)*(1-test_size)))]
  val = [datas[i] for i in range(len(train), len(datas))]

  X_train = [train[i][1:] for i in range(len(train))]
  X_test = [val[i][1:] for i in range(len(val))]
  y_train = [train[i][0] for i in range(len(train))]
  y_test = [val[i][0] for i in range(len(val))]

  return X_train, X_test, y_train, y_test

def shuffling(X, y):
  # combine
  datas = [[0.0 for j in range(18)] for i in range(len(X))]
  for i in range(len(datas)):
    datas[i][1:] = X[i]
    datas[i][0] = y[i]

  # search for least number of same label
  nol, satu = 0, 0
  # ones, zeros = LL(), LL()
  ones, zeros = [], []
  for i in range(len(y)):
    if y[i] == 1.0: satu += 1; ones.append(datas[i])
    else: nol += 1; zeros.append(datas[i])

  # ones = ll_to_arr(ones)
  # zeros = ll_to_arr(zeros)

  random.shuffle(ones)
  random.shuffle(zeros)

  # small is the largest amount of data where the label 1 and 0 have the same amount
  small = min(nol, satu)

  # equals 
  equals = [[0.0 for i in range(18)] for j in range(small*2)]
  equals[:small] = zeros[:small]
  equals[small:] = ones[:small]

  random.shuffle(equals)

  return equals

