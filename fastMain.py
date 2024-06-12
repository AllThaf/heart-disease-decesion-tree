from user import User as user
from menu import Interface as menu
from menu import TampilTree as tampilkan
from package.datasets import load_heart_disease
from package.model_selection import train_test_split
from package.tree import DecisionTreeClassifier
from package.metrics import accuracy_score as asCreate
from Fastpackage.tree import DecisionTreeClassifierFast
from Fastpackage.metrics import accuracy_score


import msvcrt
import os
import time

menu.welcome()
menu.loading()

if os.path.exists("data/node.txt"):
    # Initialize the decision tree classifier
    clf = DecisionTreeClassifierFast()
    clf.split(clf.node)
else:
    print("Data tree tidak ditemukan, mohon tunggu sebentar...")
    time.sleep(3)
    print("Mebuat data tree...")
    time.sleep(3)
    # Load the heart disease dataset
    heart_disease = load_heart_disease()
    X = heart_disease.data
    y = heart_disease.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    X_test_copy = X_test

    # Initialize the decision tree classifier
    clf = DecisionTreeClassifier()

    # Train the decision tree classifier
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test_copy)
    asCreate(y_test, y_pred)

while True:
    os.system("cls")
    menu.menu()
    pilihan = int(input("Pilihan: "))
    if pilihan == 1:
        os.system("cls")
        X_test = user().input_user()
        # X_test = [16.6,"Yes","No","No",3.0,30.0,"No","Female",55,"White","Yes","Yes","Very good",5.0,"Yes","No","Yes"]
        # X_test = [28.87,"Yes","No","No",6.0,0.0,"Yes","Female",75,"Black","No","No","Fair",12.0,"No","No","No"]
        print(X_test)
        for i in range(len(X_test)):
            X_test[i] = user().conv(i + 1, X_test[i])

        # Make predictions on the testing set
        # print(X_test)
        y_pred = clf.predict([X_test])

        if y_pred[0] == 0:
            print("Hasil prediksi: Tidak ada penyakit jantung")
        else:
            print("Hasil prediksi: Ada penyakit jantung")
        print("\nPress any key to continue...")
        msvcrt.getch()
    elif pilihan == 2:
        # Calculate the accuracy of the model
        os.system("cls")
        accuracy = accuracy_score()
        print("Accuracy:", accuracy)
        print("\nPress any key to continue...")
        msvcrt.getch()

    elif pilihan == 3:
        os.system("cls")
        while True:
            try:
                maxdepth = int(input("Masukkan kedalaman maksimal (max 10): "))
                if maxdepth > 0 and maxdepth <= 10:
                    break
                else:
                    print("Kedalaman harus lebih dari 0 atau tidak lebih dari 10")
                    time.sleep(3)
            except:
                print("Masukkan angka yang benar")
                time.sleep(3)
                os.system("cls")
        tampilkan().tampil(clf.node, maxdepth)
        tampilkan().traversal(clf.node, maxdepth)
        print("\n\nPress any key to continue...")
        msvcrt.getch()

    elif pilihan == 4:
        menu.about()

    elif pilihan == 5:
        exit()
    else:
        print("Pilihan tidak tersedia")
        time.sleep(3)
        continue
