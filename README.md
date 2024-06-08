# Analisis :
1. Deskripsi Fitur
2. Struktur Menu
3. Struktur Data
4. Simlulasi Penggunaan Struktur Data

# Deskripsi Program:
Decision Tree untuk prediksi Heart Disease adalah algoritma Machine Learning yang dirancang untuk dapat mengkategorikan/labeling apakah seseorang itu sakit atau tidak berdasarkan data dirinya. 

# Metode yang digunakan
Decision Tree ini menggunakan struktur data Binary Tree sebagai pengkondisian terhadap suatu garis untuk masing-masing node nya. 

# 1. Deskripsi Fitur:
- load_heart_disease:
Merupakan class yang memiliki instance data dan target. Pada bagian ini, program membaca data dari file csv, kemudian diolah supaya semua data menjadi float dengan cara normalisasi.

- train_test_split:
Merupakan program yang dapat membagi data untuk dilatih dan validasi. Output dari program ini berupa X_train, X_test, y_train, y_test.

- DecisionTreeClassifier:
Merupakan class yang digunakan untuk melatih data. Class ini memiliki beberapa method.

- fit:
Merupakan method dari class DecisionTreeClassifier. fit ini digunakan untuk melatih data train. Input dari method ini adalah X_train dan y_train. Dengan menggunakan data tersebut, dibuat model Decision Tree. Model Decision Tree ini dibentuk dengan mencari garis-garis split terbaik yang menghasilkan Information Gain terbanyak. Untuk tiap perulangan, daerah yang belum memiliki label semakin sedikit hingga pada akhirnya sebagian besar data berhasil dimodelkan.

- predict:
Merupakan method dari class DecisionTreeClassifier. predict digunakan untuk mendapatkan y_pred untuk data X_test.

- accuracy_score:
Merupakan function yang menghitung seberapa akurat hasil prediksi (y_pred) terhadap nilai sesungguhnya (y_test).

# 2. 

# 3. 

# 4. Simlulasi Penggunaan Struktur Data
```python
from package.datasets import load_heart_disease
from package.model_selection import train_test_split
from package.tree import DecisionTreeClassifier
from package.metrics import accuracy_score

# Load the heart disease dataset
heart_disease = load_heart_disease()
X = heart_disease.data
y = heart_disease.target

print(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the decision tree classifier
clf = DecisionTreeClassifier()

# Train the decision tree classifier
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
Code diatas adalah kerangka akhir program. Berikutnya akan dilakukan perubahan yaitu dengan melakukan prediksi dari data seseorang yang diinput.

```python
number_of_people = int(input("Number of people: "))

# Assume you have new data stored in a variable called 'new_data'
new_data = [["" for j in range(18)] for i in range(number_of_people)]

# Fill the data
for i in range(len(number_of_people)):
  for j in range(17):
    new_data[i][j] = input(f"param{j+1}: ")

# convert the data into float
new_data = converting(new_data)

# Use the trained classifier to predict the classes of the new data
predicted_classes = clf.predict(new_data)

# Print the predicted classes
print("Predicted Classes:", predicted_classes)

```

Masing-masing array dalam new_data merupakan data seseorang yang mau diprediksi. 
---
Berikut adalah gambaran ketika program dijalankan:
```
Number of people: 1

person 1:
BMI: 16.6
Smoking: Yes
AlcoholDrinking: No
Stroke: No
PhysicalHealth: 3.0
MentalHealth: 30.0
DiffWalking: No
Sex: Female
AgeCategory: 55-59
Race: White
Diabetic: Yes
PhysicalActivity: Yes 
GenHealth: Very good
SleepTime: 5.0
Asthma: Yes
KidneyDisease: No
SkinCancer: Yes

Predicted Classes:
No
```