# Variables globales
v_a = "altosfre"
v_e = "erfsotle"
powers = ["flaying", "invisibility", "strength", "through walls"]
c_power = "strength"
in_power = ["flaying", "invisibility", "through walls"]
weapons = ["gun", "axe", "grenade", "knives"]
c_weapons = "gun"
in_weapons = ["axe", "grenade", "knives"]


# Función para comenzar la historia
def begin_story():
    print("""Hace quince siglos, hubo un conflicto entre dos grandes aldeas (Altosfre y Erfsotla). Habían sido rivales durante más de dos siglos. Era tan lejano que ya no recordaban la causa original.""")
    print("Debes investigar y encontrar una solución para acabar con los conflictos entre estas aldeas.")
    village()


# Función para elegir la aldea
def village():
    while True:
        cav = str(input("Elige la aldea en la que quieres investigar (Altosfre o Erfsotla). ")).strip().lower()
        if cav == v_a.lower():
            print("Has decidido investigar en Altosfre.")
            print("Altosfre es una aldea llena de personas amables entre sí, pero egoístas con la aldea enemiga. La familia Trillon es la única que ha permanecido desde el inicio de la guerra entre Altosfre y Erfsotla. Han sido los que han dado la versión de la guerra, pero con los años, la versión ha cambiado. Investiga a fondo. Para llegar a la casa de los Trillon, debes superar algunos obstáculos.")
            r_powers()
            r_weapons()
            next_step("Altosfre")
        elif cav == v_e.lower():
            print("Has decidido investigar en Erfsotla.")
            print("Erfsotla es una aldea llena de personas amables, pero egoístas hacia la aldea enemiga." \
            " En la cima de la montaña vive una anciana que tiene más de 200 años. Nadie en la aldea cree " \
            "que sea capaz de tal cosa. Debes descubrir si es cierto y así poder llegar a la verdad de todo.")
            r_powers()
            r_weapons()
            next_step("Erfsotla")
        else:
            print("Esa opción no es válida. Intenta de nuevo.")


# Función para elegir poderes
def r_powers():
    print("Debes elegir un poder que te ayude en tu investigación.")
    correct_powers(c_power, in_power)


def correct_powers(c_power, in_power):
    cp = str(input(f"Estos son tus opciones de poder: {powers}\n¿Cuál eliges? ")).strip().lower()
    if cp == c_power.lower():
        print("Excelente elección! La fuerza es crucial para superar obstáculos.")
    elif cp in [p.lower() for p in in_power]:
        if cp == "flaying":
            print("La capacidad de desollar puede ser útil en ciertas situaciones.")
        elif cp == "invisibility":
            print("La invisibilidad te permitirá espiar sin ser visto.")
        elif cp == "through walls":
            print("Poder atravesar paredes te dará acceso a áreas ocultas.")
    else:
        print("Esa opción no es válida. Intenta de nuevo.")
        correct_powers(c_power, in_power)


# Función para elegir armas
def r_weapons():
    print("Para continuar avanzando, debes elegir un arma que te ayude a defenderte.")
    correct_weapons(c_weapons, in_weapons)


def correct_weapons(c_weapons, in_weapons):
    cw = str(input(f"Estas son tus opciones de arma: {weapons}\n¿Cuál prefieres? ")).strip().lower()
    if cw == c_weapons.lower():
        print("Excelente elección! Un arma de fuego es ideal para la defensa a distancia.")
    elif cw in [w.lower() for w in in_weapons]:
        if cw == "axe":
            print("Un hacha es útil para combates cuerpo a cuerpo.")
        elif cw == "grenade":
            print("Una granada puede ser devastadora en situaciones de emergencia.")
        elif cw == "knives":
            print("Cuchillos son silenciosos y efectivos en combates cercanos.")
    else:
        print("Esa opción no es válida. Intenta de nuevo.")
        correct_weapons(c_weapons, in_weapons)


# Función para el siguiente paso
def next_step(village_name):
    print(f"\nAhora que has elegido tu poder y arma, puedes proceder a {village_name}.")
    if village_name == "Altosfre":
        print("Para llegar a la casa de los Trillon, debes superar un laberinto.")
        action = input("¿Quieres intentar resolver el laberinto o buscar otra ruta? (resolver/buscar) ").strip().lower()
        if action == "resolver":
            print("Has resuelto el laberinto y llegaste a la casa de los Trillon.")
            print("Allí descubriste un diario antiguo que revelaba la verdad sobre el conflicto.")
            print("La guerra comenzó por un malentendido entre los líderes de las aldeas.")
            print("Con esta información, puedes ahora intentar reconciliar a las aldeas.")
        elif action == "buscar":
            print("Encontraste una ruta alternativa que te llevó a un río.")
            print("Allí conociste a un anciano que te contó sobre un puente secreto.")
            print("El puente te permitió cruzar al otro lado y llegar a la casa de los Trillon.")
            print("Allí descubriste un diario antiguo que revelaba la verdad sobre el conflicto.")
            print("La guerra comenzó por un malentendido entre los líderes de las aldeas.")
            print("Con esta información, puedes ahora intentar reconciliar a las aldeas.")
        else:
            print("Opción no válida.")
    elif village_name == "Erfsotla":
        print("Para llegar a la cima de la montaña, debes subir por un sendero empinado.")
        action = input("¿Quieres subir por el sendero o buscar una ruta más segura? (subir/buscar) ").strip().lower()
        if action == "subir":
            print("Has subido por el sendero y llegaste a la cima de la montaña.")
            print("Allí encontraste a la anciana, quien te contó sobre un secreto oculto.")
            print("El secreto revelaba que la guerra fue causada por un malentendido entre las aldeas.")
            print("Con esta información, puedes ahora intentar reconciliar a las aldeas.")
        elif action == "buscar":
            print("Encontraste una ruta más segura que te llevó a un valle.")
            print("Allí conociste a un grupo de personas que te ayudaron a subir a la cima.")
            print("En la cima, encontraste a la anciana, quien te contó sobre un secreto oculto.")
            print("El secreto revelaba que la guerra fue causada por un malentendido entre las aldeas.")
            print("Con esta información, puedes ahora intentar reconciliar a las aldeas.")
        else:
            print("Opción no válida.")


# Iniciar el juego
begin_story()

