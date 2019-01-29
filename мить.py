a=str(input('Введите аеропорт вылета:'))
b=str(input('Введите аеропорт прилета:'))

First=['KBP','FRA',105]
Second=['KBP','LON',130]


F=open('routes.csv','w')
F.write=(First+Second)
F.close 

FileWithRoads=open('routes.csv')
roads=FileWithRoads.readlines()

for line in roads:
    if (a==First[0] and b==First[1]):
        print(First[2])
    elif (a==Second[0] and b==Second[1]):
        print(Second[2])
    else:
        print('Заданого маршрута не существует')
        
        
    
