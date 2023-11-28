import math

data = []

with open("liczby.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number > 100 and number < 5000:
            flag=True
            for i in range(2, int(math.sqrt(number)+1)):
                if number % i == 0:
                    flag=False
            if flag:
                data.append(number)
print(data)