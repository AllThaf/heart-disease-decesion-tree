import math

from package.functions import *

class DecisionTreeClassifier:
  def __init__(self):
    self.X_train = None
    self.y_train = None

  def fit(self, X_train, y_train):
    self.X_train = X_train
    self.y_train = y_train

    # root
    self.unique = [bubble_sort(ll_to_arr(getUnique(X_train[i]))) for i in range(17)]
    dataset = [y_train[i]+X_train[i] for i in range(len(X_train))]
    btree = BinaryTree(dataset)

    # Set small
    
    # berikut adalah langkah untuk setiap node
    y_train = [dataset[i][0] for i in range(len(dataset))]
    X_train = [dataset[i][1:] for i in range(len(dataset))]
    info_gain = [[get_info_gain(self.unique[i][j], j, X_train, y_train) for j in range(len(self.unique[i]))] for i in range(len(self.unique))]
    # print(info_gain)

    small = [1, 0]
    for i in range(len(info_gain)):
      for j in range(len(info_gain[i])):
        if info_gain[i][j] < small[0]: small = [info_gain[i][j], i]
    print(small)
    curr = btree.root
    curr.data.line = small


    # split data
    left_x, right_x, left_y, right_y = [], [], [], []

    for i in range(len(X_train)):
      if X_train[i][small[1]] <= small[0]: left_x.append(X_train[i]); left_y.append(y_train[i])
      else: right_x.append(X_train[i]); right_y.append(y_train[i])

    curr.left = Node([left_y[i]+left_x[i] for i in range(len(left_x))])
    curr.right = Node([right_y[i]+right_x[i] for i in range(len(right_x))])

    # left
    curr_l = curr.left # Node
    
    # curr_l.data.dataset

    # right
    curr_r = curr.right

  def predict(self, X_test):
    pass

def get_info_gain(unique, idx, x, y):
  left1, left0, right1, right0 = 0, 0, 0, 0
  for i in range(len(y)):
    if x[i][idx] <= unique:
      if y[i] == 0: 
        left0 += 1
      else: 
        left1 += 1
    else:
      if y[i] == 0: 
        right0 += 1
      else: 
        right1 += 1

  total = left1 + left0 + right1 + right0

  prob_l = (left1 + left0) / total
  prob_r = (right1 + right0) / total

  entropy_l = 0 if left1 == 0 or left0 == 0 else -(left1 / (left1 + left0)) * math.log2(left1 / (left1 + left0)) - (left0 / (left1 + left0)) * math.log2(left0 / (left1 + left0))
  entropy_r = 0 if right1 == 0 or right0 == 0 else -(right1 / (right1 + right0)) * math.log2(right1 / (right1 + right0)) - (right0 / (right1 + right0)) * math.log2(right0 / (right1 + right0))

  return prob_l * entropy_l + prob_r * entropy_r

class Data:
  def __init__(self, dataset, line):
    self.dataset = dataset
    self.line = line

class Node:
  def __init__(self, dataset):
    self.left = None
    self.right = None
    self.data = Data(dataset, None)

class BinaryTree:
  def __init__(self, dataset):
    self.root = Node(dataset, None)

def forNode(node):
  pass