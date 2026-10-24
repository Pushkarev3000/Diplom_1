import pytest
from praktikum.bun import Bun

#Проверка корректной инициализации булочки
def test_bun_initialization():
    bun = Bun("Классическая", 99.5)
    assert bun.get_name() == "Классическая"
    assert bun.get_price() == 99.5

#Убеждаемся, что get_name возвращает строку
def test_bun_name_type():
    bun = Bun("Сырная", 120.0)
    assert isinstance(bun.get_name(), str)

#Убеждаемся, что get_price возвращает float
def test_bun_price_type():
    bun = Bun("Пшеничная", 85.0)
    assert isinstance(bun.get_price(), float) 

#Разные объекты могут иметь разные имена и цены
def test_bun_difference():
    bun1 = Bun("Обычная", 100.0)
    bun2 = Bun("Премиум", 200.0)
    assert bun1.get_price() != bun2.get_price()
    assert bun1.get_name() != bun2.get_name()

#Одинаковые экземпляры — допустимо
def test_bun_same_instances():    
    bun1 = Bun("С кунжутом", 110.1)
    bun2 = Bun("С кунжутом", 110.1)
    assert bun1.get_name() == bun2.get_name()
    assert bun1.get_price() == bun2.get_price()

#Пустые значения и нули
@pytest.mark.parametrize('names, prices',[('', None), ('Null',-1), (None, 0), ('0.1', 0.1), (None, None)])
def test_bun_empties_nulls(names, prices):    
    bun = Bun(names, prices)
    assert bun.get_name() == names
    assert bun.get_price() == prices