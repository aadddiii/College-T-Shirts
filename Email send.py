import smtplib
from email.message import EmailMessage

file_1 = open('Sent--Mails.txt' , 'w')

with open('list 3.txt' , 'r') as file:
	email_list = file.readlines()

msg_c = f'''
Dear representative,

My name is {NAME}, i am an {AGE} years old student from Meerut, India.

I recently finished my schooling and was about to attend a college.

For as long as i remember i wanted to do my further studies in the states, 
but i have been bounded by my financial condition, and also the 
CoronaVirus Pandemic this year.

So instead I have started collecting posters flags and T-Shirts of different colleges.

If possible, I kindly request you to send me your institution's Poster, Flag or T-Shirt
for my collection.

It would really mean a lot to me.

My address is-
{ADDRESS}

Hope you are having a pleasent day.

Hoping to hear from you soon.

Yours respectfully.'''

for emails in email_list:
	msg = EmailMessage()
	msg['subject'] = 'An Unconventional Request'
	msg['to'] = emails
	msg['from'] = {EMAIL}
	msg.set_content(msg_c)
	
	with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp:
		smtp.login({EMAIL} , {PASSWORD})
		smtp.send_message(msg)
	
	msg_sent = f'{emails} email sent\n'	
	file_1.write(msg_sent)
	print(msg_sent)