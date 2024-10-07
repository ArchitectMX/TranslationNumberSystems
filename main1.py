numb = list(input("Введите число из которого будете переводить: "))
base = int(input("Введите основание этого числа: "))
newBase = int(input("Введите основание новой системы счисления: "))
newNumb10 = 0
newNumbNewBase = ""
for i in range(len(numb)):
    newNumb10 += int(numb[-1 - i]) * (base ** i)
print("Число", ''.join(numb), "в системе счисления с основанием", 10,"-", newNumb10)
while True:
    newNumbNewBase += str(newNumb10 % newBase)
    newNumb10 //= newBase
    if newNumb10 < newBase:
        newNumbNewBase += str(newNumb10 % newBase)
        newNumbNewBase = '0' * (len(newNumbNewBase) // 4) + newNumbNewBase[::-1]
        break
print("Число", ''.join(numb), "в системе счисления с основанием", newBase,"-", newNumbNewBase)
