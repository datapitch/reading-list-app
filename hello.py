### APPEND TO LIST ###
from zlib import decompressobj


healthy = ['pizza', 'frozen custard']

healthy.append('crisp apple')
print(healthy)

healthy.insert(1, 'custard')
print(healthy)

### CHECKING IF ELEMENT IN A LIST ###

### INSERT INTO THE MIDDLE OF A LIST ###

work_days = ['Monday', 'Tuesday', 'Thursday', 'Friday']

work_days.insert(2, 'Wednesday')

print(work_days)

### REMOVE ELEMENT BY VALUE OR INDEX ###


work_days.remove('Friday') #BY VALUE
print(work_days)

del work_days[1]  #BY INDEX
print(work_days)


### REMOVE ELEMENT WITH POP  ###
work_days.pop(0)
print(work_days)

### REMOVE ELEMENT USING DEL AND SLICE ###
data = ['this', 'that', 'does', 'not', 'make', 'sense', 'sense', 'sense']
data_copy = data[:]
data_copy2 = data[:]

del data[0:2]
print(data)

del data_copy[-2:]
print(data_copy)

### REMOVE ALL OCCURENCES IN A LIST ###

while (data_copy2.count('sense') > 0):
    data_copy2.remove('sense')
print(data_copy2)

while('sense' in data):
    data.remove('sense')
print("last one", data)

### REMOVE ITEMS WITH A FOR LOOP ###
fact = ['this', 'that', 'does', 'not', 'make', 'sense', 'sense', 'sense']

for item in fact[:]:
    if item == 'sense':
        fact.remove(item)
print(fact)

### LIST COMPREHENSION SOLUTION ###

fact[:] = [item for item in fact if item != 'sense']

### REVERSE A LIST ###
talking = ['this', 'that', 'does', 'not', 'make', 'sense', 'sense', 'sense']
talking.reverse()
print("This is reversed: ", talking)
print(decompressobj(0).__init__)




### SWAP REVERSE ALGORITHM ###
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print([range(len(letters) // 2)])

#for index in range(len(letters) // 2):
#swap indexes 
#return sorted 

### Search algorithm ###
### sort algorithm ###
