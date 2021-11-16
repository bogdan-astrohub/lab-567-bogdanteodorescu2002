from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_suma, get_tipul, get_id_cheltuiala
from Logic.CRUD import create, read, update, delete


def get_datas():
    return [
        creeaza_cheltuiala(101, 3, 111, 2019 - 4 - 21, 'intretinere'),
        creeaza_cheltuiala(102, 14, 45, 2021 - 7 - 14, 'alte cheltuieli'),
        creeaza_cheltuiala(103, 5, 645, 2019 - 12 - 15, 'alte cheltuieli'),
        creeaza_cheltuiala(104, 2, 255, 2020 - 1 - 26, 'canal')
    ]


def test_create():
    cheltuieli = get_datas()
    params = (105, 6, 265, 2021 - 10 - 28, 'canal', [], [])
    c_nou = creeaza_cheltuiala(*params[:-2])
    nou_cheltuieli = create(cheltuieli, *params)

    assert c_nou in nou_cheltuieli
    assert len(nou_cheltuieli) == len(cheltuieli) + 1
    assert get_id_cheltuiala(read(cheltuieli, 102)) == 102
    assert get_nr_apartament(read(cheltuieli, 101)) == 3
    assert get_suma(read(cheltuieli, 104)) == 255
    assert get_tipul(read(cheltuieli, 103)) == 'alte cheltuieli'


def test_read():
    cheltuieli = get_datas()
    un_c = cheltuieli[2]
    assert read(cheltuieli, get_id_cheltuiala(un_c)) == un_c
    assert read(cheltuieli, None) == cheltuieli


def test_update():
    cheltuieli = get_datas()
    c_updated = creeaza_cheltuiala(101, 3, 149, 2021 - 9 - 23, 'intretinere')
    updated = update(cheltuieli, 101, 3, 149, 2021 - 9 - 23, 'intretinere', [], [])
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(cheltuieli) == len(updated)


def test_delete():
    cheltuieli = get_datas()
    to_delete = 103
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete, [], [])
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1
