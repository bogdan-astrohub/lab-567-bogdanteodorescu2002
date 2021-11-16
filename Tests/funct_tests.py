import datetime

from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tipul, get_id_cheltuiala
from Logic.CRUD import read
from Logic.funct1 import delete_all_costs_for_apartement
from Logic.funct2 import add_sum_to_all_expense_by_date
from Logic.funct3 import the_biggest_expense_for_every_type
from Logic.funct4 import ordering_expenses_descending_by_amount
from Logic.funct5 import get_sum_per_apartament


def get_datas():
    return [
        creeaza_cheltuiala(101, 3, 111, datetime.date(2019, 4, 21), 'intretinere'),
        creeaza_cheltuiala(102, 14, 45, datetime.date(2021, 7, 14), 'alte cheltuieli'),
        creeaza_cheltuiala(103, 5, 645, datetime.date(2019, 12, 15), 'alte cheltuieli'),
        creeaza_cheltuiala(104, 2, 255, datetime.date(2020, 1, 26), 'canal')
    ]


def test_delete_all_costs_for_apartement():
    cheltuieli = get_datas()
    cheltuieli = delete_all_costs_for_apartement(cheltuieli, 5, [], [])
    assert len(cheltuieli) == 3
    assert get_suma(read(cheltuieli, 104)) == 255
    assert get_data(read(cheltuieli, 102)) == datetime.date(2021, 7, 14)


def test_add_sum_to_date():
    cheltuieli = get_datas()
    cheltuieli = add_sum_to_all_expense_by_date(cheltuieli, datetime.date(2019, 12, 15), 24, [], [])
    cheltuiala_noua = read(cheltuieli, 103)
    assert get_nr_apartament(cheltuiala_noua) == 5
    assert get_suma(cheltuiala_noua) == 669
    assert get_data(cheltuiala_noua) == datetime.date(2019, 12, 15)
    assert get_tipul(cheltuiala_noua) == 'alte cheltuieli'


def test_the_biggest_expense_for_every_type():
    cheltuieli = get_datas()
    result = the_biggest_expense_for_every_type(cheltuieli)
    assert len(result) == 3
    assert result['intretinere'] == 111
    assert result['alte cheltuieli'] == 645
    assert result['canal'] == 255


def test_ordering_expenses_descending_by_amount():
    cheltuieli = get_datas()
    result = ordering_expenses_descending_by_amount(cheltuieli, [], [])
    assert get_id_cheltuiala(result[0]) == 103
    assert get_id_cheltuiala(result[1]) == 104
    assert get_id_cheltuiala(result[2]) == 101
    assert get_id_cheltuiala(result[3]) == 102


"""
def test_show_montly_amount_for_each_apartament():
    cheltuieli = get_datas()
    result = get_sum_per_apartament(cheltuieli)
    assert result[2][2020][1] == 255
    assert result[5][2019][12] == 645
    assert result[14][2021][7] == 45
"""
