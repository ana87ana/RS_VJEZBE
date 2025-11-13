studenti = [{"ime" :"pero", "godina":"2002", "uplata": True},
            {"ime" : "ja", "godina":"1999", "uplata": False}]

#print(list(map(lambda student: student["jmbag"],studenti)))

print(list(filter(lambda student : student["godina"] < "2001", studenti)))


lista = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x%2 == 0, lista)))

print(all(list(map(lambda x : x%2 == 0, lista))))

print(all(list(map(lambda student: student["uplata"] == True, studenti))))
