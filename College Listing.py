from bs4 import BeautifulSoup as soup 

with open('College Listing.txt' , 'r') as file:
	
	list_file = open('list_1.txt' , 'w')

	soup_file = soup(file , 'lxml')
	tag_1 = soup_file.find('div' , class_ = 'content-wrap')

	k = 4
	a = 1

	while k < k+1:
		tag_3 = tag_1.find_all('td')[k]


		k = k + 3

		tag_3_1 = tag_3.text

		tag_0 = f'{tag_3_1}\n\n'

		a = a+1
		print(tag_0)
		list_file.write(tag_0)
