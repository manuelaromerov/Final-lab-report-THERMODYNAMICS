from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series

ruta1=r"C:\Users\manny\OneDrive\Documents\Enes\3er semestre\Termo\experimento1.csv"
data1= pd.read_csv(ruta1)
ruta2=r"C:\Users\manny\OneDrive\Documents\Enes\3er semestre\Termo\Copia de lab termo1.csv"
data2=pd.read_csv(ruta2)

ce=data1["ce"]
m=data1["masa"]
e=data1["espesor"]
ti=data1["Tinicial"]
t=data1["Tfinal"]
tc=data1["Tcaliente"]
tf=data1["Tfrio"]
d_t=data1["deltat"]

a=0.0064

number_to_word = {
    0: "MDF",
    1: "Cartón",
    2: "Unicel",
    3: "Aluminio",
    4: "Plástico",
}

numbers = [0, 1, 2, 3, 4]

for number in numbers:
    word = number_to_word[number]

Q_dot=(m*ce*(t-ti))/(d_t)

k=(Q_dot*e)/(a*(tc-tf))
round_k = round(k, 6)
values = round_k

for index, value in enumerate(values):
    word = number_to_word[index]
    print(f"{word} = {value} W/mK")

#graficar las temperaturas calientes y frías de un material, en contra del tiempo, en la misma gráfica, por cada material

mtiempo=data2["mtime"]
mtempcal=data2["mT_C"]
mtempfrio=data2["mT_F"]

ctiempo=data2["ctime"]
ctempcal=data2["cT_C"]
ctempfrio=data2["cT_F"]

utiempo=data2["utime"]
utempcal=data2["uT_C"]
utempfrio=data2["uT_F"]

atiempo=data2["atime"]
atempcal=data2["aT_C"]
atempfrio=data2["aT_F"]

ptiempo=data2["ptime"]
ptempcal=data2["pT_C"]
ptempfrio=data2["pT_F"]

# Crear una figura con 2 subplots (uno para cada material)
fig, axs = plt.subplots(5, 1, figsize=(15, 30))

# Gráfica para el Material 1
axs[0].plot(mtiempo, mtempfrio, label="Temperatura Fría")
axs[0].plot(mtiempo, mtempcal, label="Temperatura Caliente")
axs[0].set_xlabel("Tiempo (s)")
axs[0].set_ylabel("Temperatura (°C)")
axs[0].set_title("MDF")
axs[0].legend()

# Gráfica para el Material 2
axs[1].plot(ctiempo, ctempfrio, label="Temperatura Fría")
axs[1].plot(ctiempo, ctempcal, label="Temperatura Caliente")
axs[1].set_xlabel("Tiempo (s)")
axs[1].set_ylabel("Temperatura (°C)")
axs[1].set_title("Cartón")
axs[1].legend()

axs[2].plot(utiempo, utempfrio, label="Temperatura Fría")
axs[2].plot(utiempo, utempcal, label="Temperatura Caliente")
axs[2].set_xlabel("Tiempo (s)")
axs[2].set_ylabel("Temperatura (°C)")
axs[2].set_title("Unicel")
axs[2].legend()

axs[3].plot(atiempo, atempfrio, label="Temperatura Fría")
axs[3].plot(atiempo, atempcal, label="Temperatura Caliente")
axs[3].set_xlabel("Tiempo (s)")
axs[3].set_ylabel("Temperatura (°C)")
axs[3].set_title("Aluminio")
axs[3].legend()

axs[4].plot(ptiempo, ptempfrio, label="Temperatura Fría")
axs[4].plot(ptiempo, ptempcal, label="Temperatura Caliente")
axs[4].set_xlabel("Tiempo (s)")
axs[4].set_ylabel("Temperatura (°C)")
axs[4].set_title("Plástico")
axs[4].legend()

plt.tight_layout()  # Ajusta el espacio entre subplots
plt.show()