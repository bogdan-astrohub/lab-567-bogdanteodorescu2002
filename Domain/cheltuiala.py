def creeaza_cheltuiala(id_cheltuiala, nr_apartament: int, suma, data, tipul):
    """
    Creeaza un dictionar care reprezinta o cheltuiala.
    :param id_cheltuiala: id-ul apartamentului, trebuie sa fie unic.
    :param nr_apartament: Numarul apartamentului.
    :param suma: Suma de cheltuit.
    :param data: Data cheltuielii.
    :param tipul: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    :return: O cheltuiala.
    """

    return [id_cheltuiala, nr_apartament, suma, data, tipul]


def get_id_cheltuiala(cheltuiala):
    """
    Getter pentru id-ul cheltuielii.
    :param cheltuiala: Cheltuiala.
    :return: Id-ul cheltuielii.
    """
    return cheltuiala[0]


def get_nr_apartament(cheltuiala):
    """
    Getter pentru numarul apartamentului.
    :param cheltuiala: Cheltuiala.
    :return: Nr de apartament al cheltuielii.
    """
    return cheltuiala[1]


def get_suma(cheltuiala):
    """
    Getter pentru suma.
    :param cheltuiala: Cheltuiala.
    :return: Suma cheltuita.
    """
    return cheltuiala[2]


def get_data(cheltuiala):
    """
    Getter pentru data.
    :param cheltuiala: Cheltuiala.
    :return: Data cheltuielii.
    """
    return cheltuiala[3]


def get_tipul(cheltuiala):
    """
    Getter pentru tip.
    :param cheltuiala: Cheltuiala.
    :return: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    """
    return cheltuiala[4]


def get_str(cheltuiala):
    return f'Cheltuiala cu id-ul {get_id_cheltuiala(cheltuiala)} a apartamentului cu numarul {get_nr_apartament(cheltuiala)}, din data de {get_data(cheltuiala)} ' \
           f'are o suma totala de {get_suma(cheltuiala)}, fiind o cheltuiala de tipul {get_tipul(cheltuiala)}'