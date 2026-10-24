import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

#Позитивный тест: конструктор корректно сохраняет тип, имя и цену
def test_ingredient_initialization():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Бекон", 85.0)
    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
    assert ingredient.get_name() == "Бекон"
    assert ingredient.get_price() == 85.0

#Проверяем, что геттеры возвращают ожидаемые типы данных
def test_ingredient_types_returned():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Чесночный", 45.5)
    assert isinstance(ingredient.get_type(), str)
    assert isinstance(ingredient.get_name(), str)
    assert isinstance(ingredient.get_price(), float)

#Разные экземпляры не должны влиять друг на друга
def test_different_ingredients_isolation():
    ing1 = Ingredient(INGREDIENT_TYPE_FILLING, "Сыр", 60.0)
    ing2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Барбекю", 35.05)
    assert ing1.get_type() != ing2.get_type()
    assert ing1.get_name() != ing2.get_name()
    assert ing1.get_price() != ing2.get_price()

#Одинаковые названия и цены — допустимы
@pytest.mark.parametrize('type_1, type_2, name, price',[(INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE, "Лук", 30.1),
                                                        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE,"Чеснок", 0.1),
                                                        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING,"Перец", 100.12)])
def test_same_name_different_instances(type_1, type_2, name, price):
    ing1 = Ingredient(type_1, name, price)
    ing2 = Ingredient(type_2, name, price)
    assert ing1.get_name() == ing2.get_name()
    assert ing1.get_price() == ing2.get_price()

@pytest.mark.parametrize('type_1, name, price',[(INGREDIENT_TYPE_SAUCE, "", 1),
                                                (INGREDIENT_TYPE_FILLING, None, 0),
                                                (INGREDIENT_TYPE_SAUCE,"Чеснок", None),
                                                (None,"Чеснок", 2),
                                                (None, None, None),
                                                (INGREDIENT_TYPE_FILLING, "Чеснок", -1),
                                                (INGREDIENT_TYPE_SAUCE,"Чеснок", 0.123)])

#Пустые значения, нули, границы
def test_bun_empties_nulls(type_1, name, price):
    ing = Ingredient(type_1, name, price)
    assert ing.get_type() == type_1
    assert ing.get_name() == name
    assert ing.get_price() == price
