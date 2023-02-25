x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 > 0 and x2 > 0) and (y1 > 0 and y2 > 0): #точки находятся в I четверти
    print('YES')
elif (x1 < 0 and x2 < 0) and (y1 > 0 and y2 > 0): #точки находятся в II четверти
    print('YES')
elif (x1 < 0 and x2 < 0) and (y1 < 0 and y2 < 0): #точки находятся в III четверти
    print('YES')
elif (x1 > 0 and x2 > 0) and (y1 < 0 and y2 < 0): #точки находятся в IV четверти
    print('YES')
else:
    print('NO')