

#FERD860728HMCNRM45
#[PrimeraLetraApellidoPaterno][SegundaLetraApellidoPaterno][PrimeraLetraApellidoMaterno][PrimeraLetraNombre][UltimosdosDigitosdelAnio][Mes][Dia]
def ValidarRFC():
    import re
    RFC = input("Digita tu RFC:").upper()
    # Se determina el formato a encontrar
    coincidencia1 = re.match(r"^([A-Z][A-Z][A-Z][A-Z]\d\d\d\d\d\d)$",RFC)
    print(RFC)
    if coincidencia1:
        print(f"El RFC es correcto:{RFC}")
    else:
        print("EL RFC no es valido")