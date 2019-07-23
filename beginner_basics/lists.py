#Biwott
#Lists
mycars = ['audi', 'bentley', 'corolla', 'suzuki']
print ('I would like to drive {} cars'.format(len(mycars)))

print  ('The cars are:')
for cars in mycars:
        print(cars, end=' ,')

print ('\nOh, I forgot toyota')
mycars.append ('toyoya')
print ('The cars are now:')        #appending
for cars in mycars:
    print (cars, end=' ,')

print('\nLet\'s sort the vehicles')
mycars.sort()

for cars in mycars:
    print(cars, end=', ')

print ('\nI have already driven :' ,mycars[2])
print ('The cars I have not driven yet are now:')
mycars.remove(mycars[2])           #using remove to delete an entry
for cars in mycars:
    print (cars, end = ' ,')

print ("Since corolla is a Toyota too, I'm left with:")
del mycars[3]
for cars in mycars:                #using del to remove an entry
    print (cars, end = ' ,')
