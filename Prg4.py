# Non-primitive data structure
'''declare : [ ]
rollnumber = 10
print(type(rollnumber)) 
student_rollnumber = [1,2,3,4,5,6,7,8,9,10]
print(type(student_rollnumber))

L1 = [10,20,30,40,50,60,70,80,90,100]
print("number of student is:", len(L1))

print("Roll number of 5th student is:", (len(L1)- 1)) #L1(9)

print(L1[1:6])
print(L1[9:1:-2])

for i in range(0,len(L1),2):
    print(L1[i])

for value in L1:
    print(value)

#L1.insert(1,10)
#print(L1)

#L1.append(L1)
#print(L1)

#L1.remove(10)
#print(L1)

L1.pop(7)
print(L1)'''

L2 = [10,20,30,40,50,60,70] #list mutable= make the changes in L2

#L3 = (10,20,30,40,50,60,70,80,90,100) #tuple Immmutable= can't make the chnages in L3
#slicing function
print (L2[-3:99])
'''L3 = L2[2:9]
print(type(L3))

L4 = list(L2[2:9])
print(type(L4))

car = {"Model" : "Ford", "Color": "Red", "Make" : 1975, 4 :"New"}
print(type(car))
print(len(car))

print(car[4])
print(car["Make"])'''

#for k in car.keys():
    #print(k)
    #print(k.values())

#for v in car.values():
  #  print(v)







