from pymongo import MongoClient
uri = "mongodb://kuanhyb24:hoanganh04@ds225253.mlab.com:25253/lab_c4e"

#connect to database
client = MongoClient(uri)
db = client.get_default_database()

#collection
posts = db['posts'] #insert_one(C), find(R)

post_list = posts.find()
for p in post_list:
    print(p['author'])
    print(p['title'])
    print(p['content'])

#document
#create a document
# post = {
#     'title':'kuanh',
#     'content':'cao 1m75',
#     'author': 'me'
# }
# #insert created document
# posts.insert_one(post)

