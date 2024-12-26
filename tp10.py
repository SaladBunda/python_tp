def compter_occurences(Palist,val):
    occ = 0
    i = 0
    for item in Palist:
        if(item == val):
            occ+=1
    return occ


list1 = ["test",1 ,2 ,3,3,6,"test","test2",3,3,3]

print(compter_occurences(list1,3))