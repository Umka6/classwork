colors = ['Red','\n' 'Green','\n' 'White','\n' 'Black','\n' 'Pink','\n' 'Yellow']
with open('text.txt','w') as a:
    a.writelines(colors)
    print(a)