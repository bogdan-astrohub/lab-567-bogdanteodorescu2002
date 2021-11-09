from Domain.cheltuiala import get_nr_apartament, get_suma


def get_sum_per_apartament(cheltuieli):
    '''
     Afișarea sumelor lunare pentru fiecare apartament.
    :param cheltuieli: lista cheltuieli
    :return: un dictionar in care cheia este numarul apartamentului si valorile
            sunt sumele de plata a cheltuielilor acelui apartament
    '''
    result = {}
    for c in cheltuieli:
        apartment = get_nr_apartament(c)
        suma = get_suma(c)
        if apartment not in result:
            result[apartment] = suma
        else:
            result[apartment] += suma
    return result