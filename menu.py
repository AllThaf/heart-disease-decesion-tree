import msvcrt
import os
import time


class Interface:
    def welcome():
        os.system("cls")
        print(" _       __     __                             __ ")
        print("| |     / /__  / /________  ____ ___  ___     / / ")
        print("| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / /  ")
        print("| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  /_/   ")
        print("|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/  (_)    ")
        print("                                                  ")
        print("  Welcome to the Heart Disease Prediction System  ")
        print("==================================================")
        print("          Press anything to continue....          ")
        msvcrt.getch()

    def loading():
        os.system("cls")
        print("Loading...")
        time.sleep(1)
        print("Please wait...")
        time.sleep(1)
        print("This may take a while...")

    def about():
        os.system("cls")
        print("=======================================================")
        print("  Heart Disease Prediction System v1.0                 ")
        print("  Created by: 1. Fredy Kurniadi             231524010  ")
        print("              2. Thafa Fadillah Ramdani     231524027  ")
        print("  Tujuan dibuatnya program ini adalah untuk memenuhi   ")
        print("  tugas besar mata kuliah Struktur Data dan Algoritma  ")
        print()
        print("  Program ini dibuat menggunakan bahasa pemrograman    ")
        print("  Python dengan konsep OOP                             ")
        print("=======================================================")
        print("\nPress any key to continue...")
        msvcrt.getch()

    def menu():
        print("+-------------------------+")
        print("|        Main Menu        |")
        print("+-------------------------+")
        print("| 1. Predict              |")
        print("| 2. Tes Akurasi          |")
        print("| 3. Lihat tree           |")
        print("| 4. About                |")
        print("| 5. Exit                 |")
        print("+-------------------------+")


class TampilTree:
    def tampil(self, node, max_depth, depth=0):
        if node is None or depth > max_depth:
            return

        if node.data.idx == "1":
            print("Root")
            print(
                "{} if x[{}] <= {}:".format(
                    node.data.idx, node.data.line[1], node.data.line[0]
                )
            )
        elif node.data.idx[-1] == "1":
            # print("Right")
            print(
                "|    " * depth
                + "Right\n"
                + "|    " * depth
                + "{} if x[{}] <= {}:".format(
                    node.data.idx, node.data.line[1], node.data.line[0]
                )
            )
        else:
            # print("Left")
            print(
                "|    " * depth
                + "Left\n"
                + "|    " * depth
                + "{} if x[{}] <= {}:".format(
                    node.data.idx, node.data.line[1], node.data.line[0]
                )
            )
        self.tampil(node.left, max_depth, depth + 1)
        self.tampil(node.right, max_depth, depth + 1)

    def traversal(self, node, max_depth):
        print("Traversal: ")
        print("Post Order: ", end=" ")
        self.postOrder(node, max_depth)
        print("\nPre Order: ", end=" ")
        self.preOrder(node, max_depth)
        print("\nIn Order: ", end=" ")
        self.inOrder(node, max_depth)
        print("\nLevel Order: ", end=" ")
        self.levelOrder(node, max_depth)

    def postOrder(self, node, max_depth, depth=0):
        if node is not None and depth <= max_depth:
            self.postOrder(node.left, max_depth, depth + 1)
            self.postOrder(node.right, max_depth, depth + 1)
            print(node.data.idx, end=" ")

    def preOrder(self, node, max_depth, depth=0):
        if node is not None and depth <= max_depth:
            print(node.data.idx, end=" ")
            self.preOrder(node.left, max_depth, depth + 1)
            self.preOrder(node.right, max_depth, depth + 1)

    def inOrder(self, node, max_depth, depth=0):
        if node is not None and depth <= max_depth:
            self.inOrder(node.left, max_depth, depth + 1)
            print(node.data.idx, end=" ")
            self.inOrder(node.right, max_depth, depth + 1)

    def levelOrder(self, node, max_depth):
        if node is None:
            return
        queue = []
        queue.append((node, 0))
        while len(queue) > 0:
            current_node, depth = queue.pop(0)
            if depth < max_depth + 1:
                print(current_node.data.idx, end=" ")
            if depth < max_depth:
                if current_node.left is not None:
                    queue.append((current_node.left, depth + 1))
                if current_node.right is not None:
                    queue.append((current_node.right, depth + 1))
