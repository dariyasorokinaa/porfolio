animals_products = {
    'корова': {'animal': 'корова', 'product': 'молоко', 'unit': 'л', 'min': 8, 'max': 12},
    'курица': {'animal': 'курица', 'product': 'яйца', 'unit': 'шт', 'min': 0, 'max': 1}

}
animals = []
amount = []
products = {}
ids = []


class Amount():
    def __init__(self, animal: str, amount: int):
        self.amount = amount
        self.animal = animal


class Animal(object):
    def __init__(self, animal_id: int, sort: str):
        self.sort = sort
        self.animal_id = animal_id


class AnimalProduct():
    def __init__(self, animal: str, max_amount: float, min_amount: float, product: str, unit: str):
        self.max_amount = max_amount,
        self.min_amount = min_amount,
        self.animal = animal,
        self.product = product
        self.unit = unit
        if min_amount not in range(0, 100):
            print("Недопустимое минимальное значение. От 0 до 100")
            pass
        if max_amount not in range(0, 100):
            print("Недопустимое максимальное значение. От 0 до 100")
            pass

    print()


def read_animals():
    for animal in animals_products.values():
        animal_name = animal['animal']
        text = 'Сколько животных "{}" добавить? '.format(animal_name)
        animal_amount = int(input(text))
        amount.append(Amount(animal=animal_name, amount=animal_amount))
        for _ in range(animal_amount):
            animal_id = int(input('Введите ID для животного "{}" '.format(animal_name)))
            while animal_id in ids:
                print('Животное с ID={} уже зарегистрировано'.format(animal_id))
                animal_id = int(input('Введите ID для животного "{}" '.format(animal_name)))
            while animal_id <= 0:
                print('ID должен быть больше 0')
                animal_id = int(input('Введите ID для животного "{}" '.format(animal_name)))
            animals.append(Animal(animal_id=animal_id, sort=animal_name))
            ids.append(animal_id)
        print()
    print("Сейчас на ферме зарегистрированы:")
    for animal in animals:
        print(animal.sort, 'id:', animal.animal_id)
    print('----ЖИВОТНЫЕ УСПЕШНО ДОБАВЛЕНЫ-----')
    actions()


def read_products():
    if animals:
        for animal in animals:
            text = 'Сколько {} продукта {} получено с животного "{}" (ID={})?'.format(
                animals_products[animal.sort]['unit'], animals_products[animal.sort]['product'], animal.sort,
                animal.animal_id)
            am = float(input(text))
            try:
                while am > animals_products[animal.sort]['max'] or am < animals_products[animal.sort]['min']:
                    print('Невозможно столько собрать от животного {} !'.format(animal.sort))
                    print('МАКСИМУМ {}, МИНИМУМ {} !'.format(animals_products[animal.sort]['max'],
                                                             animals_products[animal.sort]['min']))
                    text = 'Сколько {} продукта {} получено с животного "{}" (ID={})?'.format(
                        animals_products[animal.sort]['unit'], animals_products[animal.sort]['product'], animal.sort,
                        animal.animal_id)
                    am = float(input(text))
            except:
                while am > float(animals_products[animal.sort]['max'][0]) or am < float(
                        animals_products[animal.sort]['min'][0]):
                    print('Невозможно столько собрать от животного {} !'.format(animal.sort))
                    print('МАКСИМУМ {}, МИНИМУМ {} !'.format(animals_products[animal.sort]['max'],
                                                             animals_products[animal.sort]['min']))
                    text = 'Сколько {} продукта {} получено с животного "{}" (ID={})?'.format(
                        animals_products[animal.sort]['unit'], animals_products[animal.sort]['product'], animal.sort,
                        animal.animal_id)
                    am = float(input(text))
            if animal.sort not in products:
                products[animal.sort] = am
            else:
                products[animal.sort] += am
        print('----УРОЖАЙ УСПЕШНО СОБРАН------')
    else:
        print('Сначала добавьте животных!')
        print()

    actions()


def collect():
    if products:
        for animal in products.items():
            print("От животного {} получено {} {} продукта '{}'".format(animal[0], animal[1],
                                                                        animals_products[animal[0]]['unit'],
                                                                        animals_products[animal[0]]['product']))
    else:
        print('Вы еще не собрали урожай!')
        print()

    actions()


def read_new_sort():
    name = input('Введите название животоного: ')
    product = input('Что производит {} ?'.format(name))
    unit = input('В чём измеряется {} ?'.format(product))
    max = float(input('Сколько максимум {} продукта {} может дать {} ?'.format(unit, product, name)))
    min = float(input('Сколько минимум {} продукта {} может дать {} ?'.format(unit, product, name)))
    while min >= max:
        print('Минимум не может быть больше или равен максимуму')
        max = float(input('Сколько максимум {} продукта {} может дать {} ?'.format(unit, product, name)))
        min = float(input('Сколько минимум {} продукта {} может дать {} ?'.format(unit, product, name)))
    p = AnimalProduct(max_amount=max, min_amount=min, unit=unit, animal=name, product=product)
    animals_products[name] = {'animal': p.animal[0], 'product': p.product, 'unit': p.unit, 'min': p.min_amount,
                              'max': p.max_amount}
    print('-----НОВЫЙ ВИД УПСЕШНО ДОБАВЛЕН--------')
    actions()


def actions():
    print('--------------')
    actions = {
        1: "Добавить новый вид",
        2: "Добавить новое животное",
        3: "Собрать урожай",
        4: "Показать сколько продукции получено",
        5: "Выход"
    }
    for k, v in actions.items():
        print(k, ':', v)
    main()


def main():
    act = int(input())
    if act == 1:
        read_new_sort()
    elif act == 2:
        read_animals()
    elif act == 3:
        try:
            read_products()
        except NameError:
            print('На ферме ещё не зарегистрировано ни одно животное... Начните заново')
            main()
    elif act == 4:
        collect()
    elif act == 5:
        exit(0)
    else:
        while act not in range(1, 5):
            print('Попробуйте ещё раз...')
            act = int(input())
            main()


print(
    'ИНСТРУКЦИЯ: перед тем, как собрать урожай - зарегистрируйте всех животных.'
    ' Перед тем, как показать весь урожай - соберите его')
print('Выберите действие (введите цифру):')
actions()
main()
