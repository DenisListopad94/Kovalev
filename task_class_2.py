class ChessFigure:
    def __init__(self, color: str, x_coord: int, y_coord: int) -> None:
        self.color = color
        self.x_coord = self.is_valid_coord(x_coord, y_coord)[0]
        self.y_coord = y_coord

    def is_valid_coord(self, x_coord: int, y_coord: int) -> list:
        if x_coord > 7 or x_coord < 0 or y_coord > 7 or y_coord < 0:
            raise ValueError("Coordinate cann't be less than 0 or more then 7")
        return [x_coord, y_coord]

    def can_beat(self, x_to_beat: int, y_to_beat: int) -> bool:
        pass


class Pawn(ChessFigure):
    def can_beat(self, x_to_beat: int, y_to_beat: int):
        self.is_valid_coord(x_to_beat, y_to_beat)
        return abs(x_to_beat - self.x_coord) == 1 and abs(y_to_beat - self.y_coord) == 1


class Queen(ChessFigure):
    def can_beat(self, x_to_beat: int, y_to_beat: int) -> bool:
        self.is_valid_coord(x_to_beat, y_to_beat)
        return x_to_beat == self.x_coord or y_to_beat == self.y_coord or abs(x_to_beat - self.x_coord) == abs(y_to_beat - self.y_coord)


class Knight(ChessFigure):
    def can_beat(self, x_to_beat: int, y_to_beat: int) -> bool:
        self.is_valid_coord(x_to_beat, y_to_beat)
        return (abs(x_to_beat - self.x_coord) == 1 and abs(y_to_beat - self.y_coord) == 2) or (abs(x_to_beat - self.x_coord) == 2 and abs(y_to_beat - self.y_coord) == 1)


queen = Queen('white', 3, 0)
pawn = Pawn('black', 3, 1)
knight = Knight('white', 3, 3)
print(queen.can_beat(3, 4))
print(pawn.can_beat(2, 2))
print(knight.can_beat(0, 1))


class CargoCarrier:
    def __init__(self, name: str, speed: int, tariff: float) -> None:
        self.name = name
        self.speed = speed
        self.tariff = tariff

    def time_to_travell(self, distance: float) -> float:
        return round(distance/self.speed, 2)

    def cost_of_travell(self, distance: float) -> float:
        return round(distance * self.tariff, 2)


class Train(CargoCarrier):
    def __init__(self, tariff: float) -> None:
        super().__init__('Train', 250, tariff)


class Plane(CargoCarrier):
    def __init__(self, tariff: float) -> None:
        super().__init__('Plane', 340, tariff)


class Car(CargoCarrier):
    def __init__(self, tariff: float) -> None:
        super().__init__('Car', 120, tariff)


car = Car(54.2)
train = Train(6000.78)
airplane = Plane(38.19)
moscow_piter_on_car = 703.5
moscow_piter_on_train = 650
moscow_piter_on_plane = 634
print(f'''Car cover the distance {moscow_piter_on_car} in {car.time_to_travell(moscow_piter_on_car)} hours and it costs {car.cost_of_travell(moscow_piter_on_car)}
Train cover the distance {moscow_piter_on_train} in {train.time_to_travell(moscow_piter_on_train)} hours and it costs {train.cost_of_travell(moscow_piter_on_train)}
Plane cover the distance {moscow_piter_on_plane} in {airplane.time_to_travell(moscow_piter_on_plane)} hours and it costs {airplane.cost_of_travell(moscow_piter_on_plane)}''')


class Alive:
    def __init__(self, name: str, max_age: int, food: str, current_age: int) -> None:
        self.name = name
        self.max_age = max_age
        self.food = food
        self.current_age = current_age

    def eating(self, some_food: str) -> str:
        if self.food != some_food:
            return f'{self.name} have nothing to eat'
        else:
            return f'{self.name} eat {some_food}'

    def status(self, remaining_food: str) -> str:
        if self.current_age == self.max_age or self.eating(remaining_food) == 'Nothing to eat':
            return 'Die'
        else:
            return 'Alive'


class Lis(Alive):
    def __init__(self, current_age: int) -> None:
        super().__init__('Lis', 25, 'rabbit', current_age)


class Rabbit(Alive):
    def __init__(self, current_age: int) -> None:
        super().__init__('Rabbit', 9, 'plant', current_age)


class Plant(Alive):
    def __init__(self, current_age: int) -> None:
        super().__init__('Plant', 2, 'sunlight', current_age)


lis = Lis(24)
rabbit = Rabbit(5)
plant = Plant(1)
print(lis.eating('rabbit'))
print(lis.status('plant'))
print(rabbit.eating('lis'))
print(rabbit.status('plant'))
print(plant.eating('sunlight'))
print(plant.status('sunlight'))

# # Уверен, что переусложнил, но код уже был на таком этапе, что решил допилить то, что есть
# # Классы транспортных средств вызываются из задачи выше
class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
    def make_order(self, point_of_departure: str ,destination: str, time_to_deliver : str = 'not important', amount_of_money: str = 'not important') -> list:
        return [point_of_departure, destination, time_to_deliver, amount_of_money]
class Agency:
    def __init__(self, name: str) -> None:
        self.filials = {}
        self.name = name
    def add_filial(self, city: str, size: str, location : int) -> None:
       if city not in self.filials:
          self.filials[city] = [size, location]
          return [city, self.name]
       else:
           print(f'{city} is already filial of {self.name}')
    def choose_transport(self, order_info: list) ->str:
        if order_info[0] not in self.filials or order_info[1] not in self.filials:
            raise ValueError('Transport agency not deliver from(to) this city')
        elif self.filials[order_info[0]][0] == 'big' and self.filials[order_info[1]][0] == 'big':
            if order_info[3] == 'small':
                return Train(6000.78)
            elif order_info[2] == 'fast':
                return Plane(38.19)
            else:
                return Car(54.2)
        elif (self.filials[order_info[0]][0] == 'middle' or self.filials[order_info[0]][0] == 'big') and (self.filials[order_info[1]][0] == 'middle' or self.filials[order_info[1]][0] == 'big'):
            if order_info[3] == 'small':
                return Train(6000.78)
            else:
                return Car(54.2)
        else:
            return Car(54.2)  
    def calculate_income(self, others: list)->None:
        income = 0
        details = {'Plane':0,'Train':0,'Car':0}
        for other in others:
            for order in other.orders:
                income += order['cost']
                details[order['transport_type']] += order['cost']
        print(f'Total income: {income} \nBy transport:')
        for detail in details:
            print(f'{detail} - {details[detail]}')   
    def analize_time(self, others: list) -> None:
        total_time = 0
        details = {'Plane':0,'Train':0,'Car':0}
        for other in others:
            for order in other.orders:
                total_time += order['delivery_time']
                details[order['transport_type']] += order['delivery_time']
        print(f'Total time: {total_time} \nBy transport:')
        for detail in details:
            print(f'{detail} - {details[detail]}')    
class Filial(Agency):
    def __init__(self,name: str, agency_name: str) -> None:
        self.name = name
        self.agency_name = agency_name
        self.orders = []
    def place_order(self, weight: int, order_info: list, other: Agency) -> dict:
        transport = other.choose_transport(order_info)
        cost = round(transport.tariff * weight, 2)
        delivery_time = round((other.filials[order_info[1]][1] - other.filials[order_info[0]][1])/transport.speed, 2)
        order = {
            'weight': weight,
            'destination': order_info[1],
            'transport_type': transport.name,
            'cost': cost,
            'delivery_time': delivery_time,
        }
        self.orders.append(order)
        return order

ag = Agency('tmh')
info_about_first = ag.add_filial('Minsk','middle', 15)
filial1 = Filial(info_about_first[0],info_about_first[1])
info_about_second = ag.add_filial('Moskow','big',100)
filial2 = Filial(info_about_second[0],info_about_second[1])
info_about_third = ag.add_filial('Piter', 'big', 780)
filial3 = Filial(info_about_third[0],info_about_third[1])
info_about_fours = ag.add_filial('Smolensk','small',48)
filial4 = Filial(info_about_fours[0],info_about_fours[1])
current_customer = Customer('THL')
first_order = current_customer.make_order('Minsk','Moskow', 'fast', 'big')
second_order = current_customer.make_order('Moskow','Piter', 'fast', 'big')
third_order = current_customer.make_order('Moskow','Piter', 'fast', 'small')
fours_order = current_customer.make_order('Smolensk','Piter', 'fast', 'small')
filial1.place_order(58,first_order, ag)
filial2.place_order(105,third_order, ag)
filial2.place_order(800, second_order, ag)
filial4.place_order(758, fours_order, ag)
ag.calculate_income([filial1, filial2, filial3, filial4])
ag.analize_time([filial1, filial2, filial3, filial4])