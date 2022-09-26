from datetime import datetime, date, time, timedelta
import pytz
from pytz import timezone



def datetimes(datei, datef):
    formato= "%d-%m-%Y %H:%M:%S.%f"
    diference = 0
    m = 0 
    t = 0
    w = 0
    th= 0
    f = 0
    sa = 0
    su= 0

    timezone_newyork= pytz.timezone('America/New_York')
    timezone_london = pytz.timezone("Europe/London")
              
    datei = datetime.strptime(datei, '%d/%m/%Y %H:%M:%S+%f')
    date_auxi = datei
#
    datef = datetime.strptime(datef, '%d/%m/%Y %H:%M:%S+%f') 
    date_auxf = datef  

    if datei > datef:
        print('La primera fecha debe ser menor que la final')
    while datei <= datef:
        if datetime.weekday(datei) == 0: 
            m +=1
            datei = datei + timedelta(days=1)
        if datetime.weekday(datei) == 1:
            t += 1
            datei = datei + timedelta(days=1)
        if datetime.weekday(datei) == 2:
            w += 1
            datei = datei + timedelta(days=1)   
        if datetime.weekday(datei) == 3:
            th += 1
            datei = datei + timedelta(days=1)
        if datetime.weekday(datei) == 4:
            f += 1

            datei = datei + timedelta(days=1)
        if datetime.weekday(datei) == 5:
            datei = datei + timedelta(days=1)
        if datetime.weekday(datei) == 6:
            su += 1
            datei = datei + timedelta(days=1)


    diference = date_auxf - date_auxi #Difrencia en las fechas con misma zona horaria
  
    working_hours = (m*8) + (t*8)+ (w*8)+ (th*8)+ (f*8) #Cantidad de Horas laborales entre las dos fechas

    date_newyork = timezone_newyork.localize(date_auxi)

    date_london = timezone_london.localize(date_auxf)
  

    diference_zones = date_london - date_newyork  #Diferencia en la fecha entre dos zonas horarias distintas, ej: London, NY

    print("La cantidad de Lunes es:", m,
            "\n""La cantidad de Martes es:", t,
            "\n""La cantidad de Miercoles es:", w,
            "\n""La cantidad de Jueves es:", th,
            "\n""La cantidad de Viernes es:", f,
            "\n""La cantidad de Sabado es:", sa,
            "\n""La cantidad de Domingo es:", su, 
            "\n""En este periodo de tiempo la cantidad de horas laborales es:", working_hours,
            "\n""La diferencia entre las dos fechas ingresadas es:", diference,
            "\n""La diferencia entre las dos fechas ingresadas es:", diference_zones
        )
    

fecha1= "15/09/2022 18:54:55+099"
fecha2= "25/09/2022 18:54:55+099"

datetimes(fecha1, fecha2)

