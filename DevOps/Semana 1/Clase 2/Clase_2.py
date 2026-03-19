List_data = []
List_name = ["Nombre","Apellido","Interes","Edad","Altura"]
try: 
    print("\n************** Hola dame tus datos **************")
    List_data.append(str(input("Cual es tu nombre?: ")))
    List_data.append(str(input("Tu apellido?: ")))
    List_data.append(str(input("Que te interesa?: ")))
    List_data.append(int(input("Cual es tu edad?: ")))
    List_data.append(float(input("Cual es tu altura?(m): ")))

    print("\n***************** Tu informacion *****************")
    for i in range(len(List_name)):
        print(List_name[i]+": ",List_data[i])
except:
    print("hubo un error")
