from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

#Проверяем, что при создании БД уже есть данные
def test_database_initializes_with_predefined_data():
    db = Database()
    assert len(db.available_buns()) == 3
    assert len(db.available_ingredients()) == 6

#Проверяем конкретные булочки из дефолтной базы
def test_available_buns_returns_correct_items():    
    db = Database()
    buns = db.available_buns()
    black_bun = next((b for b in buns if b.get_name() == "black bun"), None)
    white_bun = next((b for b in buns if b.get_name() == "white bun"), None)
    red_bun = next((b for b in buns if b.get_name() == "red bun"), None)
    assert black_bun.get_price() == 100
    assert white_bun.get_price() == 200
    assert red_bun.get_price() == 300

#Проверяем соусы из дефолтной базы
def test_available_ingredients_returns_correct_sauces():
    db = Database()
    ingredients = db.available_ingredients()

    sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
    assert len(sauces) == 3

    hot_sauce = next((i for i in sauces if i.get_name() == "hot sauce"), None)
    sour_cream = next((i for i in sauces if i.get_name() == "sour cream"), None)
    chili_sauce = next((i for i in sauces if i.get_name() == "chili sauce"), None)

    assert hot_sauce.get_price() == 100
    assert sour_cream.get_price() == 200
    assert chili_sauce.get_price() == 300

#Проверяем начинки из дефолтной базы
def test_available_ingredients_returns_correct_fillings():
    db = Database()
    ingredients = db.available_ingredients()

    fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
    assert len(fillings) == 3

    cutlet = next((i for i in fillings if i.get_name() == "cutlet"), None)
    dinosaur = next((i for i in fillings if i.get_name() == "dinosaur"), None)
    sausage = next((i for i in fillings if i.get_name() == "sausage"), None)

    assert cutlet.get_price() == 100
    assert dinosaur.get_price() == 200
    assert sausage.get_price() == 300

#Метод должен возвращать список
def test_available_buns_returns_list():
    db = Database()
    result = db.available_buns()
    assert isinstance(result, list)

#Метод должен возвращать список
def test_available_ingredients_returns_list():
    db = Database()
    result = db.available_ingredients()
    assert isinstance(result, list)

#Изменение списка снаружи может повлиять на состояние БД
def test_lists_are_not_shared_accidentally_by_reference_trap():
    db = Database()
    original_len = len(db.available_buns())
    external_list = db.available_buns()
    external_list.append(Bun("new bun", 999))
    assert len(db.available_buns()) == original_len + 1

