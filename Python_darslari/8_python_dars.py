# summa = input("Summani kiritin: ")

# if summa.isdigit() and int(summa) > 0 and int(summa) < 100000:
# 	print("Tashakkur")
# else:
# 	print("Xato bor!")


# ism = input("Ismingizni kiriting: ")
# fam = input("Familyangizni kiritng: ")
# if ism or fam:
# 	print("Tashakkur :)")
# else:
# 	print("Iltimos, ism yoki Familyangizni kiriting")

#8-dastur: 1-dan 30-gacha sonlarni sozlar orqali ifodalash
son = input("1-dan 30-gacha son kiriting: ")
if son.isdigit():
	son = int(son)
	if son > 0 and son < 30:
		qoldiq = son % 10
		letter = '' 
		if son > 9 and son < 20:
			letter = "o'n "
		elif son > 19 and son < 30:
			letter = "yigirma "

		if qoldiq == 1:
			letter += 'bir'
		elif qoldiq == 2:
			letter += 'ikki'
		elif qoldiq == 3:
			letter += 'uch'
		elif qoldiq == 4:
			letter += 'tort'
		elif qoldiq == 5:
			letter += 'besh'
		elif qoldiq == 6:
			letter += 'olti'
		elif qoldiq == 7:
			letter += 'yetti'
		elif qoldiq == 8:
			letter += 'sakkiz'
		elif qoldiq == 9:
			letter += 'toqqiz'
		print(letter)
	else: 
		print("Kiritgan soningiz 1-30 oraligida bolishi kerak.")	
else:
	print("Son kiriting, faqat!")