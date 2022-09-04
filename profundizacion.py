import json
from tkinter import UNDERLINE
import requests
import matplotlib.pyplot as plt


def fetch():
    x=input('ingrese provincia a analizar: ')
    response = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50')
    json_response = response.json()
    dataset = [{"price": x["price"] , "condition": x["condition"]} for x in json_response["results"] if x["currency_id"] 
    == "ARS"]
    return dataset
  
def transform(dataset, min, max):
    menores= [ x for x in dataset if x["price"] < min ]
    total_menores= len(menores)
    en_rango= [ x for x in dataset if x["price"] >= min and x["price"] <= max]
    total_ok= len(en_rango)
    mayores= [ x for x in dataset if x["price"] > max ]
    total_mayores= len(mayores)
    return [total_menores,total_ok, total_mayores]

def report(data):
    fig = plt.figure()
    fig.suptitle("Composición de propiedades segun valores prefijados", fontsize=14)
    rangos = ["Menores","OK","Mayores"]
    plt.pie(data, labels= rangos, autopct='%1.1f%%')
    plt.show()
    return


if __name__ == "__main__":
    

    min= 19000
    max= 45000
    dataset = fetch()
    data = transform(dataset, min, max)
    print('Departamentos por debajo del mínimo: \n', data[0], '\n Departamentos en rango: \n', data[1], '\n Departamentos superiores al máximo: \n', data[2])
    report(data)