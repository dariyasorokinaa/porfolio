
import typing
from decimal import Decimal


class Amount(object):
    def __init__(self, count: Decimal):
        self.count = count


class Sort(object):
    def __init__(self, name: str, sort_id: int):
        self.name = name
        self.sort_id = sort_id


class Product(object):
    def __init__(self, name: str, amount: Amount):
        self.name = name
        self.amount = amount


class Animal(object):

    def __init__(self, sort: str, animal_id: int, products: typing.List[Product]):
        self.sort = sort
        self.animal_id = animal_id
        self.products = products



def read_sorts():
    global sort_count
    sort_count = int(input('Сколько животных у Вас на ферме? '))

    global sorts
    sorts = {}
    for i in range(sort_count):
        name = input('Название: ')
        sorts[i] = Sort(name=name, sort_id=i).name
    return sorts


def read_animals():
    animals_count = int(input('Сколько животных сегодня дали "урожай"?'))

    animals = []
    ids = []
    for _ in range(animals_count):
        animal_sort = input("Вид животного: ")
        while animal_sort not in sorts.values():
            print('Неизвестный вид')
            animal_sort = input("Вид животного: ")
        # Если необходимо условие, что продукцию можно собрать один раз с одного животного:
        a_id = int(input("ID животного: "))

        if a_id in ids:
            print('Уже есть!')
            while a_id in ids:
                a_id = int(input("ID животного: "))
            ids.append(a_id)
        else:
            ids.append(a_id)

        # Если такой необходимости нет, то заменить код между комменатриями на тот,
        # что строчкой ниже + удалить список ids в начале метода

        # a_id = int(input("ID животного: "))

        products = []
        product_name = input('Название продукта: ')
        product_count = float(input("Количество продукта (если ничего - 0):"))
        print('~~~~~~~')
        products.append(Product(name=product_name, amount=Amount(Decimal(product_count))))
        animals.append(Animal(sort=animal_sort, animal_id=a_id, products=products))
    print('------')
    print()
    return animals


def measure():
    measure_dict = {}
    product_name = input('Какой продукт вы получаете на ферме? ')
    measure = input('В чем Вы измеряете ' + product_name + '?')
    measure_dict[product_name] = measure


def main():
    try:
        print()
        print("Добро пожаловать на ферму! \n"
              "Сейчас фрема пуста."
              "Следуйте указаниям программы:)")
        print()

        sorts = read_sorts()
        print()
        print('Отлично! У Вас живут:')
        for sort in sorts.values():
            print(sort)
        print('---------')
        measure()
        print("--------")
        animals = read_animals()
        catalog = {}
        # Сегодняшний урожай
        for animal in animals:
            for product in animal.products:
                if product.name not in catalog.keys():
                    catalog[product.name] = product.amount.count
                else:
                    catalog[product.name] += product.amount.count
        print("Отличный выдался денёк! Сегодня Вы собрали:")
        for k, v in catalog.items():
            print(k, ': ', v)
        print("Поздравляю!")
    except:
        print('Вы неправильно заполнили данные. Придётся начать всё сначала...')


if __name__ == '__main__':
    main()
