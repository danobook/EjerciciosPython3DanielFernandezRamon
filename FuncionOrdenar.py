def MetodoBurbuja(Lista):
    #Lista = [6, 2, 3, 9, 8, 7]
    for i in range(len(Lista)-1):
        for i in range(len(Lista)-1):
            if Lista[i] > Lista[i+1]:
                Lista[i],Lista[i+1]=Lista[i+1],Lista[i]
    return Lista

