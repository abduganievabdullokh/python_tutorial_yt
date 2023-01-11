# til = input("Tilni tanlang: uz/en ?   ")

# if til == "uz":
# 	print("Siz ozbek tilini tanladingiz.")
# elif til == "en":
# 	print("You chose english language.")
# else:
# 	print("Kechirasiz boshqattan urunib ko'ring:(")

#############################################################
#ikkita tasodifiy son yigindisini toping
# from random import randint
# a = randint(1, 500)
# b = randint(1, 500)
# c = int(input("{} + {} = ".format(a, b)))

# if c == a + b:
# 	print("To'g'ri")
# else:
# 	print("Xato")
##############################################################

#Kabisa yil ekanligini aniqlovchi dastur
yil = int(input("Yilni kiriting: "))
if yil % 4 == 0:
	print("Kabisa yili")
else:
	print("Kabisa yili emas")