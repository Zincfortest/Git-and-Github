import mysql.connector as mc
db = mc.connect(host="localhost",
                user="root",
                passwd="Anay",
                database="home")
c = db.cursor()
c.execute("select*from tuesday where Name='Data'")
data = c.fetchone()               # data = [('data', 'Period1', 'Period2', 'Period3', 'Period4', 'Period5')]
c.execute("Select*from tuesday where Name='Clark'")
ab = c.fetchone()                 # ab = [('Clark', 'Class C', None, None, 'Class B', None)]
clss = [x for x in ab[1:] if x is not None] # clss = ['Class C', 'Class B']
cls = {}
for i in clss:                    # loop to add elements in cls(class:teacher) dictionary
    c.execute(f"""select Name from tuesday where '{i}' in (Period1,
                               period2,period3,period4,period5) and Name<>'Clark' """)
    name = c.fetchall() ; N =[]
    for j in name: N.append(j[0])
    cls[i] = N
# cls={'Class C': ['Brown', 'Davis', 'Sophia', 'James'], 'Class B': ['Emma', 'Liam', 'Olivia', 'Sophia']}
for i in ab[1:]: # i = 'Class C'
    if i is not None: # 'Class C' != None
        c.execute(f"""SELECT Name,free from tuesday natural join free 
                  where {data[ab.index(i)]} is NULL order by free desc""") # {Period1}
        almdon = c.fetchall() # [('Emma', 4), ('Smith', 4), ('Isabella', 4),.....]
        for j in almdon:      # j = ('Emma', 4)
            if j[0] not in cls[i] or j[1]<=1: almdon.remove(j) 
        # almdon = [('James', 4), ('Brown', 3), ('Sophia', 3),('Davis',3)]
""" So I have reached here, almdon = almost done , We now have a way to get
teachers along with there number_of_free period in a tuple
we can store it somewhere or directly use it from within the loop, idk I'm taking a break
"""

