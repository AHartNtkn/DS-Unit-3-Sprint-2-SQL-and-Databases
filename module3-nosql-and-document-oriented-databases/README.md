# NoSQL and Document-oriented databases

NoSQL, no worries? Not exactly, but it's still a powerful approach for some
problems.

## Learning Objectives

- Identify appropriate use cases for document-oriented databases
- Deploy and use a simple MongoDB instance

## Before Lecture

Sign up for an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas),
the official hosted service of MongoDB with a generous (500mb) free tier. You
can also explore the many [MongoDB tools](http://mongodb-tools.com/) out there,
though none in particular are recommended or required for installation (we're
really just checking out MongoDB as a way to understand document-oriented
databases - it's unlikely to become a core part of your toolkit the way SQLite
and PostgreSQL may).

## Live Lecture Task

Another database, same data? Let's try to store the RPG data in our MongoDB
instance, and learn about the advantages and disadvantages of the NoSQL paradigm
in the process. We will depend on
[PyMongo](https://api.mongodb.com/python/current/) to connect to the database.

Note - the
[JSON](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json)
representation of the data is likely to be particularly useful for this purpose.

## Assignment

Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a MongoDB instance, and add the code you write to do
so here. Then answer the following question (can be a comment in the top of your
code or in Markdown) - "How was working with MongoDB different from working with
PostgreSQL? What was easier, and what was harder?"

```
import sys
print(sys.version)

!pip install pymongo
import pymongo

#Full driver
client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-wpqd5.mongodb.net:27017,cluster0-shard-00-01-wpqd5.mongodb.net:27017,cluster0-shard-00-02-wpqd5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

#insert a document
db.test.insert_one({'x':1})
db.test.count_documents({'x': 1})
db.test.insert_one({'x':1})
db.test.count_documents({'x': 1})

curser = db.test.find({'x':1})

list(curser)

db.test.insert_one({'x':1})

anthony_doc = {
   'favorite_animal' : ['leafy sea dragon', 'dragon']   
}

rudy_doc = {
   'favorite_animal' : 'Koala',
   'favorite_color' : 'Blue'
}

coop_doc = {
   'favorite_animal' : 'Pangolin'
}

db.test.insert_many([anthony_doc, rudy_doc, coop_doc])

list(db.test.find())

more_docs = []

for i in range(10):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

db.test.update_one({'value':3},
                   {'$inc': {'value':5}})
                   
list(db.test.find({'value':3}))

db.test.update_many({'even':True},
                   {'$inc': {'value':100}})
                   
list(db.test.find({'even':True}))

db.test.delete_many({'even':False})

rpg_char = (1, "King Bob", 10)

db.test.insert_one({"rpg_char" : rpg_char})

db.test.insert_one({
    'sql_id': rpg_char[0],
    'name': rpg_char[1],
    'hp' : rpg_char[1]
})

list(db.test.find())
```

In most ways, interacting with the MongoDB is simpler, just shove data in, and take data out. There's little to no structure to it, which makes it simpler, but less useful at the same time. With PostgreSQL, everything was done with SQL queries, which, while being more complex than the MongoDB calls, were generally able to reveal more interesting structural information.

There is no other required tasks to turn in, but it is suggested to then revisit
the first two modules, rework/complete things as needed, and just check out with
fresh eyes the SQL approach. Compare and contrast, and come with questions
tomorrow - the main topic will be database differences and tradeoffs!

## Resources and Stretch Goals

Put Titanic data in Big Data! That is, try to load `titanic.csv` from yesterday
into your MongoDB cluster.

```
df = pd.read_csv("titanic.csv")
data = []

for i in range(len(df)):
    newDict = dict(df.iloc[i])
    newDict['Survived'] = int(newDict['Survived'])
    newDict['Pclass'] = int(newDict['Pclass'])
    newDict['Age'] = float(newDict['Age'])
    newDict['Siblings/Spouses Aboard'] = int(newDict['Siblings/Spouses Aboard'])
    newDict['Parents/Children Aboard'] = int(newDict['Parents/Children Aboard'])
    newDict['Fare'] = float(newDict['Fare'])
    data.append(newDict)

db.test.insert_many(data)
```

Push MongoDB - it is flexible and can support fast iteration. Design your own
database to save some key/value pairs for an application you'd like to work on
or data you'd like to analyze, and build it out as much as you can!
