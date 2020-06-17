"""
Tarea 1 Ordenamiento Burbuja
PADTS 2020
Python
Daniel Fernandez Ramon
"""
from ValidaNumero import ValidaDato
from FuncionCrearLista import CrearLista
from FuncionOrdenar import MetodoBurbuja

elemetos = ValidaDato()
Lista = CrearLista(elemetos)
Resultado = MetodoBurbuja(Lista)
print(f"Lista ordenada = {Resultado}")
