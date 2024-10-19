mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],'emails':['actor.gmail.com','movie.gmail.com']}
count=0
for key, value in mydictionary1.items():
    if isinstance(value, list):
        count += len(value)
print(count)
