with open('list_2.txt' , 'r') as file:
	list_3 = open('list_3.txt' , 'w')
	email_1 = file.readlines()
	for email_2 in email_1:
		email_3 = f'admissions@{email_2}'
		list_3.write(email_3)
		print(email_3)