print("*********************** Bienvenidos ********************** :"'\n'
      "Por favor ingresar 5 notas con un valor que va desde el 0 hasta el 100"'\n'
      "si el resultado te da mayor o igual a 60 estas APROBADO"'\n'
      "si te da entre 40 y 59 estas en RECUPERACION"'\n'
       "si te da menos de 40 estas REPROBADO")
# not1= int(input("por favor ingresar nota 1: "))
# not2= int(input("por favor ingresar nota 2: "))
# not3= int(input("por favor ingresar nota 3: "))
# not4= int(input("por favor ingresar nota 4: "))
# not5= int(input("por favor ingresar nota 5: "))

# suma = (not1 + not2 + not3 + not4 + not5) / 5
# if(suma >= 60):print("APROBADO")
# elif(suma >= 40 and suma < 59):print("RECUPERANDO")
# else:print("perdiste")
# print(suma)



total_notes = 0
number_of_notes = 5
counter = 0
while counter < number_of_notes:
    note = float(input(f"Ingrese la nota {counter + 1}: "))
    counter += 1
    total_notes += note
procentaje = total_notes / number_of_notes
if(procentaje >=60):print("Aprobado")
elif(procentaje >=40 and procentaje <= 59): print("Recuperacion")
else: print("perdiste")
print(procentaje)