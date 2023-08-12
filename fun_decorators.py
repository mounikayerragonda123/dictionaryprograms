#function decorators
def decor(func):
    def inner(name):
        if name=='sunny':
            print("hello sunny bad mrng")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name,"good mrng")

wish("sunny")
wish('durga')

#funcion generators
import random
import time
names=['sunny','Bunny','chinni','vinni']
subjects=['python','java','block chain']
def people_list(num_people):
    results=[]
    for i in range(num_people):
        person= {
                'id':i,
                'name':random.choice(names),
                'major':random.choice(subjects)
               }
        results.append(person)
    return results
def people_generator(num_people):
    results=[]
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(subjects)
        }
    yield person
"""t1=time.clock()
people=people_list(10000000)
t2=time.clock()"""

t1=time.clock()
people=people_generator(10000000)
t2=time.clock()

print('took{}'.format(t2-t1))



