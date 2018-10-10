import datetime
from gmail import GMail, Message
from random import choice
gmail = GMail('kuanhyb97@gmail.com','hoanganh04')
html_template = '''
<p>em chào sếp,</p>
<p>sáng nay em ngủ dậy thấy trong người bị{{sick}}, ẽm xin sếp cho em xin nghỉ 1 buổi.</p>
<p>em xin cảm ơn ạ!</p>
'''
sick_list = ["mệt, đau đầu, chóng mặt"]
x = choice(sick_list)
html_content=html_template.replace('{{sick}}',x)
currentDT = datetime.datetime.now()
msg = Message('Le Hoang Anh',to='manhtd53@wru.vn',html=html_content)
while True:
    if currentDT.hour > 7:
        gmail.send(msg)
        break
    

