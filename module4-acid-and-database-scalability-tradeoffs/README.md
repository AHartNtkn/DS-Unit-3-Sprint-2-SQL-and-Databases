# ACID and Database Scalability Tradeoffs

Comparing the costs and benefits of relational and non-relational approaches -
can we have the best of both worlds?

## Learning Objectives

- Understand and explain the advantages and disadvantages of traditional SQL
  databases
- Make informed decisions about alternative databases

## Before Lecture

So far in this sprint you've used SQLite, PostgreSQL, and MongoDB. For each of
these, consider the following questions:

- What was easy about using this technology?
- What was hard about using this technology?
- What more would you like to learn about it?

Write a summary in the style of a possible blog post, and bring the
questions/discussion to class. Bonus - later on, follow up and complete a real
blog post about different database technologies!

## Live Lecture Task

We covered a lot of ground this week - today we'll bring it together, both
summarizing and resolving lingering questions. We'll also continue the
discussion from the before lecture activity, and explore the cutting edge
"NewSQL" techniques in active development.

As time allows, we'll go back to practicing good old SQL. It's important to have
a broad awareness of the database universe, but SQL is a time-tested tool that
has and will continue to be useful across a wide range of situations. It will
also be the largest part of the sprint challenge, and likely a component of many
job interviews.

## Assignment

Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:

- How many passengers survived, and how many died?

```
print("Survived: ", len(list(db.test.find({'Survived': 1}))))
print("Died: ", len(list(db.test.find({'Survived': 0}))))
```

```
Survived:  342
Died:  545
```

- How many passengers were in each class?

```
print("First: ", len(list(db.test.find({'Pclass': 1}))))
print("Second: ", len(list(db.test.find({'Pclass': 2}))))
print("Third: ", len(list(db.test.find({'Pclass': 3}))))
```

```
First:  216
Second:  184
Third:  487
```

- How many passengers survived/died within each class?

```
print("First Survivers: ", len(list(db.test.find({'Survived': 1, 'Pclass': 1}))))
print("First NonSurviver: ", len(list(db.test.find({'Survived': 0, 'Pclass': 1}))))
print("Second Survivers: ", len(list(db.test.find({'Survived': 1, 'Pclass': 2}))))
print("Second NonSurviver: ", len(list(db.test.find({'Survived': 0, 'Pclass': 2}))))
print("Third Survivers: ", len(list(db.test.find({'Survived': 1, 'Pclass': 3}))))
print("Third NonSurviver: ", len(list(db.test.find({'Survived': 0, 'Pclass': 3}))))
```

```
First Survivers:  136
First NonSurviver:  80
Second Survivers:  87
Second NonSurviver:  97
Third Survivers:  119
Third NonSurviver:  368
```

- What was the average age of survivors vs nonsurvivors?

```
import numpy as np
print("Surviver average age: ", 
      np.mean([d['Age'] for d in list(db.test.find({'Survived': 1}))])
     )
print("NonSurviver average age: ", 
      np.mean([d['Age'] for d in list(db.test.find({'Survived': 0}))])
     )
```

```
Surviver average age:  28.408391812865496
NonSurviver average age:  30.13853211009174
```

- What was the average age of each passenger class?

```
print("First average age: ", 
      np.mean([d['Age'] for d in list(db.test.find({'Pclass': 1}))])
     )
print("Second average age: ", 
      np.mean([d['Age'] for d in list(db.test.find({'Pclass': 2}))])
     )
print("Third average age: ", 
      np.mean([d['Age'] for d in list(db.test.find({'Pclass': 3}))])
     )
```

```
First average age:  38.78898148148148
Second average age:  29.868641304347825
Third average age:  25.188747433264886
```

- What was the average fare by passenger class? By survival?

```
print("First average fare: ", 
      np.mean([d['Fare'] for d in list(db.test.find({'Pclass': 1}))])
     )
print("Second average fare: ", 
      np.mean([d['Fare'] for d in list(db.test.find({'Pclass': 2}))])
     )
print("Third average fare: ", 
      np.mean([d['Fare'] for d in list(db.test.find({'Pclass': 3}))])
     )
print("Surviver average fare: ", 
      np.mean([d['Fare'] for d in list(db.test.find({'Survived': 1}))])
     )
print("NonSurviver average fare: ", 
      np.mean([d['Fare'] for d in list(db.test.find({'Survived': 0}))])
     )
```

```
First average fare:  84.1546875
Second average fare:  20.662183152173913
Third average fare:  13.707707392197124
Surviver average fare:  48.39540760233918
NonSurviver average fare:  22.208584036697246
```

- How many siblings/spouses aboard on average, by passenger class? By survival?

```
print("First average siblings/spouses: ", 
      np.mean([d['Siblings/Spouses Aboard'] for d in list(db.test.find({'Pclass': 1}))])
     )
print("Second average siblings/spouses: ", 
      np.mean([d['Siblings/Spouses Aboard'] for d in list(db.test.find({'Pclass': 2}))])
     )
print("Third average siblings/spouses: ", 
      np.mean([d['Siblings/Spouses Aboard'] for d in list(db.test.find({'Pclass': 3}))])
     )
print("Surviver average siblings/spouses: ", 
      np.mean([d['Siblings/Spouses Aboard'] for d in list(db.test.find({'Survived': 1}))])
     )
print("NonSurviver average siblings/spouses: ", 
      np.mean([d['Siblings/Spouses Aboard'] for d in list(db.test.find({'Survived': 0}))])
     )
```

```
First average siblings/spouses:  0.4166666666666667
Second average siblings/spouses:  0.40217391304347827
Third average siblings/spouses:  0.6201232032854209
Surviver average siblings/spouses:  0.47368421052631576
NonSurviver average siblings/spouses:  0.5577981651376147
```

- How many parents/children aboard on average, by passenger class? By survival?

```
print("First average parents/children: ", 
      np.mean([d['Parents/Children Aboard'] for d in list(db.test.find({'Pclass': 1}))])
     )
print("Second average parents/children: ", 
      np.mean([d['Parents/Children Aboard'] for d in list(db.test.find({'Pclass': 2}))])
     )
print("Third average parents/children: ", 
      np.mean([d['Parents/Children Aboard'] for d in list(db.test.find({'Pclass': 3}))])
     )
print("Surviver average parents/children: ", 
      np.mean([d['Parents/Children Aboard'] for d in list(db.test.find({'Survived': 1}))])
     )
print("NonSurviver average parents/children: ", 
      np.mean([d['Parents/Children Aboard'] for d in list(db.test.find({'Survived': 0}))])
     )
```

```
First average parents/children:  0.35648148148148145
Second average parents/children:  0.3804347826086957
Third average parents/children:  0.39630390143737165
Surviver average parents/children:  0.4649122807017544
NonSurviver average parents/children:  0.3321100917431193
```

- Do any passengers have the same name?

```
names = db.test.distinct('Name')
len(names) == len(set(names))
```

```
True
```

There are no duplicate names.


- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.

```
import re

# List of Mr. ???
mrs = list(filter(lambda s: re.match('Mr\..*',s),names))
# List of Mrs. ???
mrss = list(filter(lambda s: re.match('Mrs\..*',s),names))

# Filter lists by if they are supposed to have a spouse on board
mrs2 = []
for n in mrs:
    if db.test.find_one({'Name': n})['Siblings/Spouses Aboard'] == 1:
        mrs2.append(n)
mrss2 = []
for n in mrss:
    if db.test.find_one({'Name': n})['Siblings/Spouses Aboard'] == 1:
        mrss2.append(n)

# Get last names
mrs_last = [n.split(" ")[-1] for n in mrs2]
mrss_last = [n.split(" ")[-1] for n in mrss2]

couples = 0

# Count matching last names
for n in mrs_last:
    try:
        i = mrss_last.index(n)
        mrss_last.pop(i)
        couples+=1
    except ValueError:
        pass

print("Number of couples: ", couples)
```

```
Number of couples:  42
```


## Resources and Stretch Goals

The assignment drilled core SQL, but *didn't* review joins - revisit the RPG
data, and do more joins (explicit or implicit) to make sure you understand how
to connect data across tables.

If you got the Titanic data in your MongoDB cluster - see if you can also answer
the above questions using MongoDB!

Read up on [database
normalization](https://en.wikipedia.org/wiki/Database_normalization) - a variety
of formal techniques for reducing the redundancy of data stored in a relational
database.

Keep working on your written summary from the "before lecture" exercise, and
grow it into a proper blog post. Consider focusing it on one particular
technology or technique, and compare/contrast it with the alternatives.

Get more reps in! Check out [SQLBolt](https://sqlbolt.com/) and [w3schools SQL
Tutorial](https://www.w3schools.com/sql/), both of which include interactive
exercises. Mastering SQL is all about practice, so get it down now and you'll be
confident for your job interviews.
