

import random
import csv
import math
ruta = 'reporte_sueldos.csv'


trabajadores = ['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez','Miguel Sanchez','Isabel Gomez','Francisco Díaz','Elena Fernández']

sueldo = []

# Asignar sueldos de forma aleatoria 

def sueldos_aleatorios():
    
    for empleado in trabajadores:
        sueldo=[random.randint(300000, 2500000) ]
        
        print('sueldo asignado de forma aleatoria ')
        
        
        
# clasificar sueldo 
def clasificar_sueldo():
    
    global sueldo   
    print(f'sueldos menores a $800.000 Total :',len(sueldo for sueldo in trabajadores if sueldo < 800000))
    for empleado in trabajadores:
        if sueldo < 800000 :
            empleado['nomble empleado','sueldo']
            
    print(f'sueldo entre 800.000 y 2.000.000 Total :',len(sueldo for sueldo in trabajadores if  800000 < sueldo < 2000000 ))
    for empleado in trabajadores :
        if 800.000 < sueldo < 2000000 :
             empleado['nomble empleado','sueldo']
             
    print(f'sueldos mayores a 2.000.000  Total:',len(sueldo for sueldo in trabajadores if sueldo > 2000000))         
    for empleado in trabajadores :
        if sueldo > 2000000 :
            empleado['nomble empleado','sueldo']
           
    
    total_sueldos = sum(sueldo)

    print (f'TOTAL SUELDOS :${total_sueldos}')
    
    

# ver estadisticas 
def ver_estadisticas():
  
 sueldo_min = min(sueldo)
 sueldo_max = max(sueldo)
 sueldo_promedio = sueldo_max /sueldo_min
 
 print(f'sueldo minimo :{sueldo_min}')
 print(f'sueldo maximo :{sueldo_max}')
 print(f'sueldo promedio :{sueldo_promedio}')




# Reporte de sueldos 

def reporte_sueldos():
    sueldo_base = empleado[sueldo]
    desct_salud = sueldo_base * 0.7
    desct_afp = sueldo_base * 0.12
    sueldo_liquido = sueldo_base - desct_salud - desct_afp
    with open(ruta,'w') as file:
        for empleado in trabajadores:
            empleado['nombre empleado','sueldo Base',{sueldo_base}, 'Descuento salud',{desct_salud}, 'Descuento AFP',{desct_afp}, 'sueldo Liquido',{sueldo_liquido}]

# salir del programa 

def salir_del_programa():
    
     print('finalizando programa.....')
     print('Desarrollado por Guerben Cajuste')
     print('Rut 26.792.130-k')
     
      
     

# menu 
def menu():
    
    while True :
        
        print('1. Asignar sueldos aleatorios')
        print('2. Clasificar sueldos')
        print('3. Ver estadísticas')
        print('4. Reporte de sueldos')
        print('5. Salir del programa')
        
        opcion = int(input('Elige una opcion :'))
        
        if opcion == 1 :
            sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldo()
        elif opcion == 3 :
            ver_estadisticas()
        elif opcion == 4 :
            reporte_sueldos()
        elif opcion == 5:
            salir_del_programa()
            break
        else :
            print('ingrese una opcion valida ')
             
             
             
if __name__ == '__main__':
    menu()          