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
        print("| 3. About                |")
        print("| 4. Exit                 |")
        print("+-------------------------+")


class TampilTree:
    def tampil(clf):
        return 0
