from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the decision tree classifier
clf = DecisionTreeClassifier()

# Train the decision tree classifier
clf.fit(X_train, y_train)

# # Make predictions on the testing set
# y_pred = clf.predict(X_test)

# # Calculate the accuracy of the model
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# Assume you have new data stored in a variable called 'new_data'
new_data = [[5.1, 3.5, 1.4, 0.2],   # Sample 1
            [4.9, 3.0, 1.4, 0.2],   # Sample 2
            [6.7, 3.1, 4.4, 1.4],   # Sample 3
            [5.6, 2.8, 4.9, 2.0]]   # Sample 4

predicted_classes = clf.predict(new_data)

# Print the predicted classes
print("Predicted Classes:", predicted_classes)
