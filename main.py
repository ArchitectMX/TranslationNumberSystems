print(str(bin(4 ** 511 + 2 ** 511 - 511)).count("1"))
print(4 ** 511 + 2 ** 511 - 511)
"Сколько единиц содержится в двоичной записи значения выражения: 44942328371557897693232629769725618340449424473557664318357520289433168951375240783177119330601884005280028469967848339414697442203604155623211857659868537798345938327514921106088054003234587269546181034217940303990259531467630757141966678572355892742551472687075667803012238361561335049493812299230559075841?"
number = 44942328371557897693232629769725618340449424473557664318357520289433168951375240783177119330601884005280028469967848339414697442203604155623211857659868537798345938327514921106088054003234587269546181034217940303990259531467630757141966678572355892742551472687075667803012238361561335049493812299230559075841
binary_representation = bin(number)  # переводим в двоичную систему
count_of_ones = binary_representation.count('1')  # считаем единицы
print(count_of_ones)
