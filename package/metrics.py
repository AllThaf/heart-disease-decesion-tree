def accuracy_score(y_test, y_pred):
    print(f"Hasil prediksi: \n{y_pred[:10]}")
    print(f"\nHasil sesunguhnya: \n{[int(y_test[:10][i]) for i in range(10)]}")
    output = sum(
        [1 if y_test[i] == y_pred[i] else 0 for i in range(len(y_test))]
    ) / len(y_test)

    with open("data/accuracy.txt", "w") as file:
        file.write(str(output))
        file.close
    return output
