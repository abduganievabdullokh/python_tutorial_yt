# import math
# print(math.ceil(8.7))
# print(math.floor(9.9))
# print(math.sqrt(100))

###############################################################################
#ikki xil vaqt kiritiladi
#time1 = soat1, minut1, secund1
#time2 = soat2, minut2, secund2

# soat1 = int(input("1-soat: "))
# minut1 = int(input("1-Minut: "))
# secund1 = int(input("1-Secund: "))

# soat2 = int(input("2-soat: "))
# minut2 = int(input("2-Minut: "))
# secund2 = int(input("2-Secund: "))

# secund = abs((soat1 - soat2) * 3600 + (minut1 - minut2) * 60 + (secund1 - secund2))
# print("Secund:{}".format(secund))
# 1 soat 3600 secund, 1 minut 60 secund
# ikkita vaqt oraligida qancha sekund borligini aniqlab beruvchi dastur 👆🏻👆🏻
##############################################################################


#Topshiriq
#3 xonali son kiriting va usha 3ta sonni yegindisini toping
son = input("Uch xonali son kiriting: ")
yegindi = int(son[0]) + int(son[1]) + int(son[2])
print(yegindi)