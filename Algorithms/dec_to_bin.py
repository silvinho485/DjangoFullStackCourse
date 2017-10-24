# dec_num = raw_input()
# while not dec_num.isdigit():
#     print("Deve conter somente digitos!")
#     dec_num = raw_input()
dec_num = 141
dec_num = int(dec_num)
bin = ""

def toBin(dec_num):
    bin = ""
    while dec_num > 0:
        bin = str(dec_num % 2) + bin
        dec_num = dec_num/2
    return bin

if dec_num != 0:
    bin = toBin(dec_num)
elif dec_num < 0:
    bin = toBin(abs(dec_num))
else:
    bin = "Eh 0!"

if __name__ == "__main__":
    print bin
