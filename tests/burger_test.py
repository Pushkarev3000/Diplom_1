import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

#Проверяем расчёт цены только для булок без ингридиентов
#Все зависимости замоканы — тестируем только логику Burger
def test_burger_price_with_mocked_bun_and_ingredient():
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "test bun"
    mock_bun.get_price.return_value = 100.0

    burger = Burger()
    burger.set_buns(mock_bun)

    expected_price = 100.0 * 2
    assert burger.get_price() == expected_price

#Проверяем, что get_receipt() формирует корректный текст.
def test_burger_receipt_format_with_mocks():
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "special bun"
    mock_bun.get_price.return_value = 100.0 

    mock_ingredient = MagicMock()
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient.get_name.return_value = "spicy sauce"
    mock_ingredient.get_price.return_value = 30.0

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()
    assert receipt.startswith("(==== special bun ====)")
    assert "= sauce spicy sauce =" in receipt.lower()
    assert receipt.endswith(f"Price: {2 * 100.0 + 30.0}")

#Несколько ингредиентов: проверяем, что суммируются все
def test_burger_multiple_ingredients_price():
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "base bun"
    mock_bun.get_price.return_value = 80.0

    mocks = []
    prices = [10.0, 20.0, 30.0]
    for p in prices:
        m = MagicMock()
        m.get_type.return_value = INGREDIENT_TYPE_FILLING
        m.get_name.return_value = f"ingredient-{p}"
        m.get_price.return_value = p
        mocks.append(m)

    burger = Burger()
    burger.set_buns(mock_bun)
    for m in mocks:
        burger.add_ingredient(m)

    expected_price = 80.0 * 2 + sum(prices)
    assert burger.get_price() == expected_price

#move_ingredient: проверяем, что порядок меняется.
def test_burger_move_ingredient_with_mocks():
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "bun"
    mock_bun.get_price.return_value = 100.0

    i1 = MagicMock()
    i1.get_name.return_value = "a"
    i1.get_price.return_value = 10.0

    i2 = MagicMock()
    i2.get_name.return_value = "b"
    i2.get_price.return_value = 20.0

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(i1)
    burger.add_ingredient(i2)

    burger.move_ingredient(1, 0)
    assert burger.ingredients == [i2, i1]

# remove_ingredient: проверяем удаление по индексу.
def test_burger_remove_ingredient_with_mocks():
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "bun"
    mock_bun.get_price.return_value = 100.0

    i1 = MagicMock()
    i1.get_name.return_value = "first"
    i1.get_price.return_value = 10.0

    i2 = MagicMock()
    i2.get_name.return_value = "second"
    i2.get_price.return_value = 20.0

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(i1)
    burger.add_ingredient(i2)

    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] is i2

#Если булочка не установлена, get_price падает (None.get_price())
#Мы не мокаем булочку — это проверка на отсутствие зависимости
def test_burger_get_price_raises_if_bun_is_none():
    burger = Burger()
    with pytest.raises(AttributeError):
        burger.get_price()

#Аналогично: без булочки get_receipt падает
def test_burger_get_receipt_raises_if_bun_is_none():
    burger = Burger()
    with pytest.raises(AttributeError):
        burger.get_receipt()
