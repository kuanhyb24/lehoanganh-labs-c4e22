from gmail import GMail,Message
gmail = GMail('kuanhyb97@gmail.com','hoanganh04')
html_template = '''
<b>{{drink}}</b>
'''
from random import choice
drink_list = ['cafe','bia','nuoc ngot','ruou']
x = choice(drink_list)
html_content=html_template.replace('{{drink}}','ruou')
msg = Message('Le Hoang Anh',to='manhdt53@wru.com',html=html_content)
gmail.send(msg)
