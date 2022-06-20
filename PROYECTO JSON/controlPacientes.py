import json
import controlMedicos as medico
import funciones_utiles
persona = {}
persona['atributos'] = []
persona['historia clinica'] = []


def id_maximo():
    persona = leer_json()
   # historias= list(persona[1])
    historias = list(persona['historia clinica'])

    lista_de_ides = []
    for historia in historias:
        id = historia['id_historia']
        valor_id = int(id)
        lista_de_ides.append(valor_id)
    return max(lista_de_ides)


def crear_primer_paciente():
    persona_base = leer_json()
    with open("Personas.json", "w") as Arch:
        inicial = list(persona_base['atributos'])
        profesional_cero = {'Documento': "0", 'Nombre': '',
                            'Apellido': '', 'Fecha': '00/00/0000', 'Nacionalidad': ''}
        inicial.append(profesional_cero)
        persona_base['atributos'] = inicial
        json.dump(persona_base, Arch)


def crear_primer_historia():
    persona_base = leer_json()
    with open("Personas.json", "w") as Arch:
        inicial = list(persona_base['historia clinica'])
        profesional_cero = {
            'id_historia': '0', 'Fecha': '20/20/2000', 'Nombre': '', 'Especialidad': ''}
        inicial.append(profesional_cero)
        persona_base['historia clinica'] = inicial
        json.dump(persona_base, Arch)


def crear_json(nombre_archivo):
    try:
        with open(str(nombre_archivo)+".json", "r") as Archivo:
            print()  # INTENTAR
    except:
        with open(str(nombre_archivo)+".json", "w") as Archivo:  # SI NO SE PUDO
            json.dump(persona, Archivo, indent=4)
        crear_primer_paciente()
        crear_primer_historia()


def leer_json():
    with open("Personas.json", "r") as Archivo:
        persona = json.load(Archivo)
    return(dict(persona))


def agregar_persona():
    idocumento = input("Ingrese un documento")
    inombre = funciones_utiles.valida(input("Ingrese un nombre"))
    iapellido = funciones_utiles.valida(input("Ingrese un apellido"))
    ifecha = input("Ingrese una fecha de nacimiento")
    inacionalidad = funciones_utiles.valida(input("Ingrese nacionalidad"))
    ifecha_historia = input("Ingrese una fecha de ingreso")
    ienfermedad = funciones_utiles.valida(input("Ingrese su enfermedad"))
    iobservaciones = funciones_utiles.valida(input("Ingrese una observacion"))

    persona = leer_json()  # DICCIONARIO Y SUS FUNCIONES
    atributos = list(persona['atributos'])

    caracteristicas = {'Documento': idocumento, 'Nombre': inombre,
                       'Apellido': iapellido, 'Fecha': ifecha, 'Nacionalidad': inacionalidad}
    atributos.append(caracteristicas)
    persona['atributos'] = atributos

    persona['historia clinica'] = historia(
        ifecha_historia, ienfermedad, iobservaciones)
    actualizar_json(persona)


def actualizar_json(diccionario):
    with open("Personas.json", "w") as Archivo:
        json.dump(diccionario, Archivo)


def historia(fecha, enfermedad, observaciones):
    persona = leer_json()  # DICCIONARIO Y SUS FUNCIONES
    atributos = list(persona['historia clinica'])  # LISTA VACIA
    medico.lista_medicos()
    input('Toca enter para ver los medicos ...')
    nombre_medico = funciones_utiles.valida(input('Que medico desea?'))
    caracteristicas = {'id_historia': str(id_maximo()+1), 'Fecha': fecha, 'Enfermedad': enfermedad,
                       'Medico': medico.existe_medico(nombre_medico), 'Observaciones': observaciones}
    atributos.append(caracteristicas)
    return atributos


def obtener_fechas_json(campo):
    persona = list(leer_json()[campo])
    lista_fechas = []
    for p in persona:
        lista_fechas.append(p['Fecha'])
    return lista_fechas


def buscar_paciente():
    persona = list(leer_json()['atributos'])
    dni = input('Ingrese un dni')

    for p in persona:
        if p['Documento'] == dni:
            print(p['Nombre'], funciones_utiles.devuelve_edad(p['Fecha']))


def buscar_por_atributo():
    personas = list(leer_json()['atributos'])
    
    atributo = funciones_utiles.valida(input('Ingrese un atributo'))
    if atributo != 'Fecha':
        valor = funciones_utiles.valida(input('Ingrese un' + atributo))
        for persona in personas:
            if persona[atributo] == valor:
                print(persona[atributo],
                      funciones_utiles.devuelve_edad(persona['Fecha']))

    if atributo == 'Fecha':
        print(funciones_utiles.calcula_rango_fechas())


def modificar_por_atributo():
    persona_json = leer_json()

    dni = input('Ingrese un dni')
    valor = funciones_utiles.valida(input('Que quieres cambiar?'))
    nuevo_valor = funciones_utiles.valida(input('Ingrese el nuevo valor'))

    for p in (persona_json['atributos']):
        if p['Documento'] == dni:
            p[valor] = nuevo_valor

    actualizar_json(persona_json)


def eliminar_por_atributo():
    persona_json = leer_json()

    dni = input('Ingrese un dni')

    for p in (persona_json['atributos']):
        if p['Documento'] == dni:
            indice = list(persona_json['atributos']).index(p)
            (persona_json['atributos']).pop(indice)
            (persona_json['historia clinica']).pop(indice)

    actualizar_json(persona_json)