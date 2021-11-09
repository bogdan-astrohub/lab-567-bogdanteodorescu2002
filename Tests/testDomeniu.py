from Domain.cheltuiala import creeaza_cheltuiala, get_id_cheltuiala, get_nr_apartament, get_suma, get_data, get_tipul


def testCheltuiala():
    cheltuiala = creeaza_cheltuiala(1, 103, 200, "28.10.2002", "intretinere")

    assert get_id_cheltuiala(cheltuiala) == 1
    assert get_nr_apartament(cheltuiala) == 103
    assert get_suma(cheltuiala) == 200
    assert get_data(cheltuiala) == "2019-10-28"
    assert get_tipul(cheltuiala) == "intretinere"