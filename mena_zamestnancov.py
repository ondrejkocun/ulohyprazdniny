subor=open('mena_zamestnancov.txt','r')
mena=[]
priezviska=[]
p=-1
nm=0
np=0
naj=[]
for riadok in subor:
    p+=1
    riadok=riadok.strip()
    if p<4:
        mena.append(riadok)
    else:
        priezviska.append(riadok)
for i in range(len(mena)):
    if len(mena[i])>nm:
        nm=len(mena[i])
    if len(priezviska[i])>np:
           np=len(priezviska[i])
           
for i in range(len(mena)):
    if len(mena[i])==nm:
        naj.append(mena[i])
    if len(priezviska[i])==np:
        npr=priezviska[i]
print(naj,'=',nm)
print(np,'=',npr)
subor1=open('vystup.txt','w')
for i in range(len(mena)):
    subor1.write(mena[i]+' '+priezviska[i]+'\n')
subor.close()
subor1.close()
