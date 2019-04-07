list=[]
list.append("mary,love,hate")
list.append("colo,love,hate")
list.append("chris,love,hate")
list.append("nacr,love,hate")
print(list)
print("enter position to be deleted")
print("enter contact to be deleted")
search=input()
for i in list:
    if search in i:
        print(list.index(i))
        posi=list.index(i)
list.remove(list[int(posi)])
print(list)
