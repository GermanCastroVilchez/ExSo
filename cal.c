#include <stdio.h>
#include <stdlib.h>


int main(){
int *a,*operacion;
printf("=================CALCULADORA============== \n");
printf("Operaciones disponibles \n");
printf("* 1- Suma \n");
printf("* 2- Resta \n");
printf("* 3- Multiplicacion \n");
printf("* 4- Divicion \n");
int operaciones;
scanf("%d",&operaciones);

int b;
a=(int *)malloc(b * sizeof(int));
operacion=(int *)malloc(sizeof(int));

if(operaciones==1){
	printf("===========SUMA===========");

printf("ingrese n numeros :  \n ");
scanf("%d",&b);
for (int c=1;c<=b;c++){
  
printf("ingrese el numero %d :  \n   ", c );
scanf("%d",&a[c]);

*operacion=*operacion+a[c];
}

printf("la suma es de: %d:  \n ",*operacion);
}
else if(operaciones==2){
printf("===========RESTA===========");

printf("ingrese n numeros :  \n ");
scanf("%d",&b);

for (int c=1;c<=b;c++){
   

printf("ingrese el numero %d :  \n   ", c );
scanf("%d",&a[c]);

*operacion=(*operacion)-a[c];
}

printf("la suma es de: %d:  \n ",*operacion);

}
 else if (operaciones==3)
 {
 	printf("===========MULTIPLICACION===========");

printf("ingrese n numeros :  \n ");
scanf("%d",&b);
*operacion=1;
for (int c=1;c<=b;c++){
   

printf("ingrese el numero %d :  \n   ", c );
scanf("%d",&a[c]);

*operacion=*operacion*a[c];
}

printf("la suma es de: %d:  \n ",*operacion);
 }
 else if (operaciones==4)
 {
 	printf("===========DIVISION===========");

printf("ingrese n numeros :  \n ");
*operacion=1;
scanf("%d",&b);
for (int c=0;c<b;c++){
   

printf("ingrese el numero %d :  \n   ", c );
scanf("%d",&a[c]);
*operacion=a[c]/(*operacion);
*operacion=a[c];	
printf("%d",*operacion);
}

printf("la suma es de: %d:  \n ",*operacion);
 }
 else{
 	printf("=========Opcion no encontrada========\n");
 	printf("=========FIN======\n");
 }

}