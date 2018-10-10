#Connect to our class’s Mongo Database
from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
posts = db['posts']
post = {
    'title':'Chào các bạn!',
    'content':'Các anh chị của Techkids rất nhiệt tình giúp đỡ các vấn đề liên quan đến học tập và các vấn đề trong cuộc sống. Hãy chọn Techkids vì đây là một môi trường thật tuyệt vời ^^',
    'author': 'Lê Hoàng Anh'
}
posts.insert_one(post)
print(post)