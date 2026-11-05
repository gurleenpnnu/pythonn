# list is mutable

list = ["fruits","apple",5,3.14,False,"Hardik","rehan"]
print(list[0])
list[0]="kiwi"
print(list)
print(list[0:6:3])
list.append("harry")
print(list)



l1= [2,54,3,1,454,345]
l1.insert(4,5)
l1.sort() #ascending order
# l1.reverse()
print(l1.pop(2)) #elmt at 2 will get del
print(l1)