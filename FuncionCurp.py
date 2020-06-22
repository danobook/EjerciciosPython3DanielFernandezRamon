#FERD860728HMCNRM68
#[PrimeraLetraApellidoPaterno][SegundaLetraApellidoPaterno][PrimeraLetraApellidoMaterno][PrimeraLetraNombre][UltimosdosDigitosdelAnio][Mes][Dia][Sexo][EntidadFederativa][PrimerasConsonatesDeNombreyAplellidos][Entero][Entero]
def ValidarCurp():

    import re
    RFC = input("Digita tu CURP:").upper()
    # Se determina el formato a encontrar
    coincidencia1 = re.match(r"^([A-Z][A-Z][A-Z][A-Z]\d\d\d\d\d\d[A-Z][A-Z][A-Z][A-Z^AEIOU][A-Z^AEIOU][A-Z^AEIOU]\d\d)$",RFC)
    print(RFC)
    if coincidencia1:
        print(f"El RFC es correcto:{RFC}")
    else:
        print("EL RFC no es valido")
