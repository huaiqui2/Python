print("-----------------------------")
print("Creditos Mandell")
print("-----------------------------")

varNombre = input("ingrese su Nombre: ")
varApellido = input("ingrese su Apellido: ")
varEdad = input("ingrese su Edad: ")
varMontoSolicitud = input("ingrese su monto credito: ")
varSalario = input("ingrese su Sueldo Mensual: ")

if varMontoSolicitud > varSalario:
    print ("Credito supera su sueldo")
else:
    print ("Credito aprobado")
    print ("si no paga")
    print ("se le embargara su casa")