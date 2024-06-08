from User import User as user
from menu import Interface as menu
from package.datasets import load_heart_disease
from package.model_selection import train_test_split
from package.tree import DecisionTreeClassifier
from package.metrics import accuracy_score
import msvcrt
import os
import time

menu.welcome()
menu.loading()
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

while True:
    os.system("cls")
    menu.menu()
    pilihan = int(input("Pilihan: "))
    if pilihan == 1:
        os.system("cls")
        print("Program ini hanya dapat digunakan jika anda berusia 18 tahun atau lebih")
        X_test = user().input_user()
        print(X_test)
        for i in range(len(X_test)):
            X_test[i] = user().conv(i + 1, X_test[i])

        # Make predictions on the testing set
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
        y_pred = clf.predict(X_test_copy)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)
        print("\nPress any key to continue...")
        msvcrt.getch()

    elif pilihan == 3:
        menu.about()

    elif pilihan == 4:
        exit()
    else:
        print("Pilihan tidak tersedia")
        time.sleep(3)
        continue
