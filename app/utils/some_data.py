"""Some db data."""

recipes = [
    {
        "name": "Сэндвич",
        "description": "Вкусный сэндвич с тунцом. \
            Одной банки тунца хватает на 4 сэндвича",
        "cooking_time": 5,
        "views_qty": 10,
    },
    {
        "name": "Яичница",
        "description": "Яичница с томатами. Легкий способ приготовления.",
        "cooking_time": 15,
        "views_qty": 5,
    },
    {
        "name": "Простой бутерброд",
        "description": "Хлеб с маслом. Ничего лишнего.",
        "cooking_time": 2,
        "views_qty": 3,
    },
    {
        "name": "Бутерброд с салатом",
        "description": "Хлеб с маслом и салатом.",
        "cooking_time": 3,
        "views_qty": 3,
    },
]

ingridients = [
    {
        "name": "Хлеб",
        "description": "Кусок свежего хлеба",
    },
    {
        "name": "Тунец",
        "description": "Четверть банки законсервированного тунца",
    },
    {
        "name": "Листья салата",
        "description": "Свежие листья",
    },
    {
        "name": "Лук зеленый",
        "description": "Несколько перьев лука",
    },
    {
        "name": "Яйцо куриное",
        "description": "Обычное яйцо из магазина",
    },
    {
        "name": "Томат",
        "description": "Используйте только зрелые томаты",
    },
    {
        "name": "Масло сливочное",
        "description": "Добавлять по вкусу",
    },
]

relationships = [
    {
        "recipe_id": 1,
        "ingridient_id": 1,
    },
    {
        "recipe_id": 1,
        "ingridient_id": 2,
    },
    {
        "recipe_id": 1,
        "ingridient_id": 3,
    },
    {
        "recipe_id": 1,
        "ingridient_id": 4,
    },
    {
        "recipe_id": 2,
        "ingridient_id": 4,
    },
    {
        "recipe_id": 2,
        "ingridient_id": 5,
    },
    {
        "recipe_id": 2,
        "ingridient_id": 6,
    },
    {
        "recipe_id": 3,
        "ingridient_id": 1,
    },
    {
        "recipe_id": 3,
        "ingridient_id": 7,
    },
    {
        "recipe_id": 4,
        "ingridient_id": 1,
    },
    {
        "recipe_id": 4,
        "ingridient_id": 7,
    },
    {
        "recipe_id": 4,
        "ingridient_id": 3,
    },
]
