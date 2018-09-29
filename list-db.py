import dataset

db = dataset.connect('sqlite:///sgtalk.db')

authors = db['authors'].all()
num = 1

#for a in authors:
#   print("%5d" % num, "%25s" % a['name'],a['article'])
#   num = num+1

#num=1
# result = db.query('SELECT * FROM authors ORDER BY name')
# for a in result:
#   print("%5d" % num, "%25s" % a['name'],a['article'])
#   num = num+1
#
summary = []
result = db.query('SELECT COUNT(*) total FROM authors')
for row in result:
    total = row['total']
result = db.query('SELECT name , count(article) c FROM authors GROUP BY name')
for a in result:
#   print("%5d" % a['c'], "%25s" % a['name'])
   summary.append([a['c'],a['name']])
   num = num+1
# print(summary)
summary.sort(key=lambda x: x[0], reverse=True)
for i in range(20):
    print("%5.2f" % (summary[i][0]/total*100), summary[i][1])