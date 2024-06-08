import time
import os


class User:
    def option(self, x):
        with open("data/unique.csv", "r") as file:
            for line in file:
                if str(line)[:2] == f"{x}," or str(line)[:2] == f"{x}":
                    return str(line)[3:]
            file.close

    def input_user(self):
        X_test = ["" for i in range(17)]
        # 1
        while True:
            print(
                "Program ini hanya dapat digunakan jika anda berusia 18 tahun atau lebih"
            )
            try:
                X_test[0] = input("12.02 - 94.85\n1. BMI: ")
                if 12.02 <= float(X_test[0]) <= 94.85:
                    break
                else:
                    print("\nMohon masukkan input yang benar")
                    time.sleep(3)
                    os.system("cls")
            except:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")

        os.system("cls")

        # 2
        while True:
            X_test[1] = input(f"{self.option(2)}\n2. Smoking: ")
            if X_test[1] in self.option(2):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 3
        while True:
            X_test[2] = input(f"{self.option(3)}\n3. AlcoholDrinking: ")
            if X_test[2] in self.option(3):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 4
        while True:
            X_test[3] = input(f"{self.option(4)}\n4. Stroke: ")
            if X_test[3] in self.option(4):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 5
        while True:
            X_test[4] = input("0.0 - 30.0\n5. PhysicalHealth: ")
            try:
                if 0.0 <= float(X_test[4]) <= 30.0:
                    break
                else:
                    print("\nMohon masukkan input yang benar")
                    time.sleep(3)
                    os.system("cls")
            except:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 6
        while True:
            try:
                X_test[5] = input("0.0 - 30.0\n6. MentalHealth: ")
                if 0.0 <= float(X_test[5]) <= 30.0:
                    break
                else:
                    print("\nMohon masukkan input yang benar")
                    time.sleep(3)
                    os.system("cls")
            except:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 7
        while True:
            X_test[6] = input(f"{self.option(7)}\n7. DiffWalking: ")
            if X_test[6] in self.option(7):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 8
        while True:
            X_test[7] = input(f"{self.option(8)}\n8. Sex: ")
            if X_test[7] in self.option(8):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 9
        while True:
            try:
                X_test[8] = input("18 >\n9. AgeCategory: ")
                if 18.0 <= float(X_test[8]):
                    break
                else:
                    print("\nMohon masukkan input yang benar")
                    time.sleep(3)
                    os.system("cls")
            except:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 10
        while True:
            X_test[9] = input(f"{self.option(10)}\n10. Race: ")
            if X_test[9] in self.option(10):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 11
        while True:
            X_test[10] = input(f"{self.option(11)}\n11. Diabetic: ")
            if X_test[10] in self.option(11):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 12
        while True:
            X_test[11] = input(f"{self.option(12)}\n12. PhysicalActivity: ")
            if X_test[11] in self.option(12):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 13
        while True:
            X_test[12] = input(f"{self.option(13)}\n13. GenHealth: ")
            if X_test[12] in self.option(13):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 14
        while True:
            try:
                X_test[13] = input("1.0 - 24.0\n14. SleepTime: ")
                if 1.0 <= float(X_test[13]) <= 24.0:
                    break
                else:
                    print("\nMohon masukkan input yang benar")
                    time.sleep(3)
                    os.system("cls")
            except:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 15
        while True:
            X_test[14] = input(f"{self.option(15)}\n15. Asthma: ")
            if X_test[14] in self.option(15):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 16
        while True:
            X_test[15] = input(f"{self.option(16)}\n16. KidneyDisease: ")
            if X_test[15] in self.option(16):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        # 17
        while True:
            X_test[16] = input(f"{self.option(17)}\n17. SkinCancer: ")
            if X_test[16] in self.option(17):
                break
            else:
                print("\nMohon masukkan input yang benar")
                time.sleep(3)
                os.system("cls")
        os.system("cls")

        return X_test

    def getColumn1(self, line):
        line = str(line)
        i = 0
        while line[i] != " ":
            i += 1
        j = i
        if line[:2] != "11":
            while line[j] + line[j + 1] != ", " and j + 1 != len(line):
                j += 1
        if line[:2] == "11":
            while line[j] + line[j + 1] + line[j + 2] != '", ' and j + 2 != len(line):
                j += 1
                # print()
            return line[i + 2 : j], float(line[j + 2 :])

            # print(line[i+1:j])
            # print(line[j+2:])

        return line[i + 1 : j], float(line[j + 2 :])

    def conv(self, x, value):
        with open("data/converter.csv", "r") as file:
            for line in file:
                if str(line)[:2] == f"{x}," or str(line)[:2] == f"{x}":
                    # print(str(line)[3:])
                    column1, ans = self.getColumn1(line)
                    if x in [0, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17]:
                        if str(value) == str(column1) or f'"{value}"' == str(column1):
                            # print(column1, value)
                            return ans
                        else:
                            continue
                    else:
                        return (float(value) - float(column1)) / (
                            float(ans) - float(column1)
                        )

                    # return str(line)[3:]
            file.close
