print("ASIGNACION DE MEMORIA");
print("Ingrese Total de Memoria")
totalM=int(input())
print("Defina Sistema Operativo")
SistemaO=int(input())
Trabajos={};
Trabajos["SO"]=SistemaO;
print(Trabajos)
totalM=totalM-SistemaO
def opcionesF():
	print("Opciones")
	print("1- Agregar Trabajo");
	print("2- Ver estado");
	opciones=int(input())
	addt=0;

	if opciones==1:
		print("Agregue otro trabajo")
		addt=int(input())
		Trabajos["T"+str(len(Trabajos))]=addt;
		opcionesF()
	elif opciones==2:
		print("===========ESTADO===========")
		#totalM=totalM-addt
		print(Trabajos)
		#print("Espacion Disponible",totalM)
		print("============================")
		opcionesF()

opcionesF()




