nota=int(input("ingresa la nota:"))

if(nota>=9 and nota <=10):
    print("promosionado")
elif(nota>=7 and nota <=8):
    print("aprobado")
elif(nota>=1 and nota <=6):
    print("libre")
else:
    print("No son validos")
