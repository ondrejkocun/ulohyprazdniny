subor=open('skok_do_dialky.txt','r')
krajin=[]
hocico=[]
najdalej=0
dialka=[]
p=0
mena=[]
for riadok in subor:
    riadok=riadok.strip()
    riadok=riadok.split(' ')
    krajin.append(riadok[1])
    dialka.append(riadok[2:])
    mena.append(riadok[0])

krajiny=[*set(krajin)]    
hocico.append(krajin.count('CAN'))
hocico.append(krajin.count('RUS'))
hocico.append(krajin.count('ITA'))
print(hocico)
for i in range(len(krajiny)):
    print(krajiny[i],'=',hocico[i])

for i in (dialka):
    for j in range(5):
        if int(i[j])>najdalej:
            najdalej=int(i[j])
            p+=1
print(mena[p],' ',najdalej)


