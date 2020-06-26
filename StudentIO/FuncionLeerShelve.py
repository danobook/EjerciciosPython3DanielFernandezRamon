import shelve

def leerDatos(s):

    with shelve.open('test_shelf.db') as s:
        existing = s['key1']
    print(".::Imprimiendo datos con formato Shelve::.")
    print(existing)
