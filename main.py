class Holodilnik:
    def __init__(self, milk = 0, meat = 0, cheese = 0, coca_cola = 0):
        self.milk = milk
        self.meat = meat
        self.cheese = cheese
        self.coca_cola = coca_cola

def fridge_edit():
    global overall_milk, overall_meat, overall_cheese, overall_chocolate
    overall_milk = int(input('Сколько литров молока положить или взять?: '))
    overall_meat = int(input('Сколько килограмм мяса положить или взять?: '))
    overall_cheese = int(input('Сколько кусочков сыра положить или взять?: '))
    overall_chocolate = int(input('Сколько бутылок кока-колы положить или взять?: '))
    fridge_result()

def fridge_result():
    add_milk = Fridge(milk = overall_milk)
    if add_milk.milk < 0:
        print('В холодильнике не хватает молока')
    else:
        milk_result = add_milk.milk
        print('В холодильнике ' + str(milk_result) + ' литров молока')

    add_meat = Fridge(meat = overall_meat)
    if add_meat.meat < 0:
        print('В холодильнике не хватает мяса')
    else:
        meat_result = add_meat.meat
        print('В холодильнике ' + str(meat_result) + ' килограмм мяса')

    add_cheese = Fridge(cheese = overall_cheese)
    if add_cheese.cheese < 0:
        print('В холодильнике не хватает сыра')
    else:
        cheese_result = add_cheese.cheese
        print('В холодильнике ' + str(cheese_result) + ' кусочков сыра')

    add_coca_cola = Fridge(coca_cola = overall_coca_cola)
    if add_coca_cola.coca_cola < 0:
        print('В холодильнике не хватает бутылок кока-колы')
    else:
        coca_cola_result = add_chocolate.chocolate
        print('В холодильнике ' + str(chocolate_result) + ' кусочков шоколада')

if __name__ == '__main__':
    fridge_edit()
