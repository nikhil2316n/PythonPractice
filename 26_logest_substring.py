st='Nikhil'.lower()

lt=[]

for i in st:
    if i not in lt:
        lt.append(i)

    elif i in lt:
        break

print(lt)
