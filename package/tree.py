import math

from package.functions import *


class Node:
    def __init__(self, dataset, idx):
        self.left = None
        self.right = None
        self.data = Data(dataset, None, idx)


class Data:
    def __init__(self, dataset, line, idx):
        self.dataset = dataset
        self.line = line
        self.idx = idx


class DecisionTreeClassifier:
    def __init__(self, max_depth=10):
        self.max_depth = max_depth
        self.num = 0
        self.node = None
        
        with open("data/node.txt", 'w') as file:
            file.write("")
            file.close

    def fit(self, X_train, y_train, node=None, depth=0):
        # root
        if node is None:
            dataset = [[y_train[i]] + X_train[i] for i in range(len(X_train))]
            self.unique = [
                bubble_sort(
                    ll_to_arr(getUnique([X_train[j][i] for j in range(len(X_train))]))
                )
                for i in range(len(X_train[0]))
            ]
            node = Node(dataset, "1")

        if depth == self.max_depth:
            if len(node.data.dataset) > 0:
                with open("data/node.txt", 'a') as file:
                    file.write(f" {node.data.idx} {round(
                            sum([row[0] for row in node.data.dataset])
                            / len(node.data.dataset)
                        )}!\n")
                    file.close
            return
        if len(node.data.dataset) < 10:
            if len(node.data.dataset) > 0:
                with open("data/node.txt", 'a') as file:
                    file.write(f" {node.data.idx} {round(
                            sum([row[0] for row in node.data.dataset])
                            / len(node.data.dataset)
                        )}!\n")
                    file.close
            return

        node = self.addSmall(node)

        with open('data/node.txt', 'a') as file:
            file.write(f" {node.data.idx} {node.data.line[0]} {node.data.line[1]}\n")
            file.close

        node = self.split(node)

        self.fit(
            [node.left.data.dataset[i][1:] for i in range(len(node.left.data.dataset))],
            [node.left.data.dataset[i][0] for i in range(len(node.left.data.dataset))],
            node.left,
            depth + 1,
        )
        self.fit(
            [
                node.right.data.dataset[i][1:]
                for i in range(len(node.right.data.dataset))
            ],
            [
                node.right.data.dataset[i][0]
                for i in range(len(node.right.data.dataset))
            ],
            node.right,
            depth + 1,
        )
        self.node = node

    def addSmall(self, node):
        dataset = node.data.dataset
        y_train = [dataset[i][0] for i in range(len(dataset))]
        X_train = [dataset[i][1:] for i in range(len(dataset))]
        info_gain = [
            [
                get_info_gain(self.unique[i][j], i, X_train, y_train)
                for j in range(len(self.unique[i]))
            ]
            for i in range(len(self.unique))
        ]
        small = [float("inf"), 0]
        index = [0, 0]
        for i in range(len(info_gain)):
            for j in range(len(info_gain[i])):
                if info_gain[i][j] < small[0]:
                    small = [info_gain[i][j], i]
                    index = [i, j]
        small = [self.unique[index[0]][index[1]], index[0]]

        self.num += 1
        # print(self.num, small)
        node.data.line = small
        return node

    def split(self, node):
        dataset = node.data.dataset
        X_train = [dataset[i][1:] for i in range(len(dataset))]
        y_train = [dataset[i][0] for i in range(len(dataset))]
        small = node.data.line

        left_x, right_x, left_y, right_y = [], [], [], []

        for i in range(len(X_train)):
            if X_train[i][small[1]] <= small[0]:
                left_x.append(X_train[i])
                left_y.append(y_train[i])
            else:
                right_x.append(X_train[i])
                right_y.append(y_train[i])

        node.left = Node([[left_y[i]] + left_x[i] for i in range(len(left_x))], node.data.idx + "0")
        node.right = Node([[right_y[i]] + right_x[i] for i in range(len(right_x))], node.data.idx + "1")
        return node

    def predict(self, X_test):
        return [self.predicting(X_test[i]) for i in range(len(X_test))]

    def predicting(self, x):
        curr = self.node
        while True:
            if x[curr.data.line[1]] <= curr.data.line[0]:
                if curr.left.left is not None:
                    curr = curr.left
                else:
                    return round(
                        sum([row[0] for row in curr.left.data.dataset])
                        / len(curr.left.data.dataset)
                    )
            else:
                if curr.right.right is not None:
                    curr = curr.right
                else:
                    output = round(
                        sum([row[0] for row in curr.right.data.dataset])
                        / len(curr.right.data.dataset)
                    )
                    return output


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
    if total == 0:
        return 1

    prob_l = (left1 + left0) / total
    prob_r = (right1 + right0) / total

    entropy_l = (
        0
        if left1 == 0 or left0 == 0
        else -(left1 / (left1 + left0)) * math.log2(left1 / (left1 + left0))
        - (left0 / (left1 + left0)) * math.log2(left0 / (left1 + left0))
    )
    entropy_r = (
        0
        if right1 == 0 or right0 == 0
        else -(right1 / (right1 + right0)) * math.log2(right1 / (right1 + right0))
        - (right0 / (right1 + right0)) * math.log2(right0 / (right1 + right0))
    )
    # print(f"{unique}, {idx} info_gain: {prob_l * entropy_l + prob_r * entropy_r}")
    return prob_l * entropy_l + prob_r * entropy_r
