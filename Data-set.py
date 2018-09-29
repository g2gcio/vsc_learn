import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
table.insert(dict(name='Jane Doe', age=34, gender='female'))

john = table.find_one(name='John Doe')

#print(john)
#john.gender="male"
#print(table)

table.insert(dict(name='Ken Doe', age=46, country='China'))

# dataset will create "missing" columns any time you insert a dict with an unknown key
table.insert(dict(name='Alex Doe', age=37, country='France', gender='female'))

users = db['sometable'].all()
for user in db['sometable']:
   print(user['age'],user['name'])
