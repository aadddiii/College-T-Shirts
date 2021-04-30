email_list = []
with open('list_1.txt' , 'r') as file:
	list_2 = open('list_2.txt' , 'w')
	email_1 = file.readlines()
	for email_2 in email_1:
		email_3 = email_2.split('//')
		del email_3[0]
		print(email_3)
		for email_4 in email_3:
			list_2.write(email_4)
