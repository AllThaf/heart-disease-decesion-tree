def read_node():
    arr = []
    with open("data/node.txt", "r") as file:
        for line in file:
            arr.append(line.strip().split(" "))
    return arr


class Node:
    def __init__(self, idx):
        self.left = None
        self.right = None
        self.data = Data(None, idx)


class Data:
    def __init__(self, line, idx):
        self.line = line
        self.idx = idx


class DecisionTreeClassifierFast:
    def __init__(self, max_depth=10):
        self.arr = read_node()
        idx = "1"
        threshold, column = None, -1
        for i in range(len(self.arr)):
            if idx == str(self.arr[i][0]):
                threshold = self.arr[i][1]
                if len(self.arr[i]) == 3:
                    column = int(self.arr[i][2])
                break
        self.node = Node(idx)
        self.node.data.line = [threshold, column]
        self.max_depth = max_depth
        self.split(self.node)

    def split(self, node, current_depth=0):
        if current_depth == self.max_depth or node is None:
            return

        # Split right
        idx = node.data.idx + "1"
        threshold, column = None, -1
        for i in range(len(self.arr)):
            if idx == str(self.arr[i][0]):
                threshold = self.arr[i][1]
                if len(self.arr[i]) == 3:
                    column = int(self.arr[i][2])
                break
        if threshold is not None:
            node.right = Node(idx)
            node.right.data.line = [threshold, column]
            self.split(node.right, current_depth + 1)

        # Split left
        idx = node.data.idx + "0"
        threshold, column = None, -1
        for i in range(len(self.arr)):
            if idx == str(self.arr[i][0]):
                threshold = self.arr[i][1]
                if len(self.arr[i]) == 3:
                    column = int(self.arr[i][2])
                break
        if threshold is not None:
            node.left = Node(idx)
            node.left.data.line = [threshold, column]
            self.split(node.left, current_depth + 1)

    def predict(self, X_test):
        return [self.predicting(X_test[i]) for i in range(len(X_test))]

    def predicting(self, x):
        curr = self.node
        while True:
            if curr.data.line[0][-1] != "!":
                if x[curr.data.line[1]] <= float(curr.data.line[0]):
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        for i in range(len(self.arr)):
                            if str(self.arr[i][0]) == str(curr.data.idx) + "0":
                                return int(str(self.arr[i][1])[0])
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        for i in range(len(self.arr)):
                            if str(self.arr[i][0]) == str(curr.data.idx) + "1":
                                return int(str(self.arr[i][1])[0])
            else:
                return int(curr.data.line[0][:-1])
