slovar = {
    0 : 'Е',
    1 : 'Ж',
    2 : 'И',
}


def main():
    word = ['', '', '', '', '']
    count = 0
    for i in range(3):
        word[0] = slovar[i]
        for j in range(3):
            word[1] = slovar[j]
            for k in range(3):
                word[2] = slovar[k]
                for m in range(3):
                    word[3] = slovar[m]
                    for n in range(3):
                        word[4] = slovar[n]
                        count += 1
                        if count == 238:
                            print("".join(word))
                            return


if __name__ == '__main__':
    main()

