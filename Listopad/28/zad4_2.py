import math

data = []

with open("pierwsze.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        flag=True
        for i in range(2, int(math.sqrt(number)+1)):
                if number % i == 0:
                    flag=False
                    break
        if flag:
            number = int((str(number)[::-1]))
            for i in range(2, int(math.sqrt(number)+1)):
                if number % i == 0:
                    flag=False
                    break
        if flag:
            data.append(int((str(number)[::-1])))

print(data)