class TwoVariables:
    def __init__(self, first_atr : int, second_atr : int) -> None:
        self.first_atr = first_atr
        self.second_atr = second_atr
    def summary(self) -> int:
        return self.first_atr + self.second_atr
    def set_atributes(self, new_first, new_second):
        self.first_atr = new_first
        self.second_atr = new_second
    def printer(self) -> None:
        print(f'First variable: {self.first_atr} second variable {self.second_atr}')
    def maximum(self) -> int:
        return max(self.first_atr, self.second_atr)
    
temp = TwoVariables(5,10)
print(temp.summary())
print(temp.maximum())
temp.set_atributes(9,89)
temp.printer()

class Counter:
    def __init__(self, start = 1, end = 10) -> None:
        self.start = start
        self.end = end
        self.current = start
    def increase(self):
        if self.current < self.end:
            self.current += 1
        else:
            print('Out of range')
    def decrease(self):
        if self.current > self.start:
            self.current -= 1
        else:
            print('Out of range')
    def information(self):
        print(f'Current station of counter: {self.current}')

count = Counter(0,18)
count.information()
count.increase()
count.information()
count.decrease()
count.information()

class Shop:
    avliable = {}
    def __init__(self) -> None:
        self.products = {}
    def add_product(self, name:str, price:float = 0) -> None:
       if name not in self.products:
          self.products[name] = price
       else:
           print(f'{name} is already in the shop')
    def search(self, find_name: str) -> None:
        if find_name in self.products:
            print(f'{find_name} is already in the shop and costs {self.products[find_name]}')
        else:
            print(f'There is no {find_name}  in the shop')
    def del_prod(self, produst_to_del: str) -> None:
        if produst_to_del in self.products:
            del self.products[produst_to_del]
        else:
            print(f'There is no {produst_to_del}  in the shop')
    def info(self) -> None:
        for product in self.products:
            print(f'{product}:{self.products[product]}')
my_shop = Shop()
my_shop.add_product('Apple', 25)
my_shop.add_product('Milk', 40)
my_shop.add_product('Chocobar', 15)
my_shop.info()
my_shop.del_prod('Milk')
my_shop.add_product('Sprite', 28)
my_shop.search('Sprite')
my_shop.info()

class MoneyBox: 
    coins = 0
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
    def can_add(self,coins_to_add: int) ->bool:
        return self.coins + coins_to_add <= self.capacity
    def add(self,coins_to_add: int) -> None:
        self.coins += coins_to_add
    def current_quantity(self) -> None:
        print(f'Quantity of coins: {self.coins}')

kop = MoneyBox(5)
kop.current_quantity()
print(kop.can_add(6))
kop.add(4)
kop.current_quantity()

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator =numerator
        self.denominator = denominator
    def info(self) -> None:
        if self.denominator == 1:
            print(f'{self.numerator}')
        else:
            print(f'{self.numerator}/{self.denominator}')
    def simplify(self):
        for i in reversed(range(1,max(self.denominator,self.numerator))):
            if self.numerator %i == 0 and self.denominator%i == 0:
                self.numerator = int(self.numerator/i)
                self.denominator = int(self.denominator / i)
        return Fraction(self.numerator, self.denominator)
    def __add__(self,other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,self.denominator * other.denominator).simplify()

fr = Fraction(27,15)
fr.info()
fr2 = Fraction(8,4)
fr2.info()
fr.simplify()
fr.info()
fr_sum = fr + fr2
fr_sum.info()


class Applicant:
    def __init__(self, first_name: str, last_name: str, faculty: str = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.exams = [] 
        self.grades = [] 
    def info(self) -> None:
        print(f"{self.first_name} {self.last_name}, faculty {self.faculty}") 
    def add_exam(self, exam: str) -> None:
        self.exams.append(exam) 
    def add_grade(self, grade: int) -> None:
        self.grades.append(grade) 
    def get_average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) 


class Teacher:
    def __init__(self, first_name: str, last_name: str, subject: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
    def info(self) -> None:
        print(f"{self.first_name} {self.last_name}, subject {self.subject}") 
    def set_grade(self, applicant) -> None:
        grade = int(input('Rate a student:'))
        applicant.add_grade(grade)
        print(f"{self.first_name} {self.last_name} get {grade} applicant {applicant.first_name} {applicant.last_name} by subject {self.subject}")


class Faculty:
    def __init__(self, name: str, min_score: float) -> None:
        self.name = name
        self.min_score = min_score 
        self.applicants = [] 
    def info(self) -> None:
        print(f"Faculty {self.name}, minimal mark {self.min_score}") 
    def add_applicant(self, applicant) -> None:
        self.applicants.append(applicant) 
    def get_enrolled_applicants(self) -> list:
        enrolled = []
        for applicant in self.applicants:
            if applicant.get_average_grade() >= self.min_score:
                enrolled.append(applicant) 
        return enrolled

class System:
    def __init__(self) -> None:
        self.faculties = [] 
        self.teachers = [] 
        self.applicants = [] 
    def add_faculty(self, faculty) -> None:
        self.faculties.append(faculty) 
    def add_teacher(self, teacher) -> None:
        self.teachers.append(teacher)
    def add_applicant(self, applicant) -> None:
        self.applicants.append(applicant) 
    def register_applicant(self, applicant, faculty) -> None:
        applicant.faculty = faculty 
        faculty.add_applicant(applicant) 
        print(f"Applicant {applicant.first_name} {applicant.last_name} register on {faculty.name}")
    def conduct_exams(self) -> None:
        for applicant in self.applicants:
            for teacher in self.teachers:
                if teacher.subject in applicant.exams:
                    teacher.set_grade(applicant) 
    def determine_enrolled_applicants(self) -> None:
        for faculty in self.faculties:
            enrolled = faculty.get_enrolled_applicants() 
            if enrolled == []:
                print(f'No one was enrolled on  {faculty.name}')
            else:
                print(f"On {faculty.name} enrolled:")
                for applicant in enrolled:
                    print(f'{applicant.first_name} {applicant.last_name}')

test_system = System()
fpmi_fac = Faculty('fpmi', 4.2)
ksis_fac = Faculty('ksis', 4.8)
mike = Applicant('Mike', 'Green')
kate = Applicant('Kate', 'Drew')
math_teacher = Teacher('Andrew', 'Graud', 'math')
physics_teacher = Teacher('Matew', 'Millou', 'physics')
test_system.add_faculty(fpmi_fac)
test_system.add_faculty(ksis_fac)
test_system.add_teacher(math_teacher)
test_system.add_teacher(physics_teacher)
test_system.add_applicant(mike)
test_system.add_applicant(kate)
test_system.register_applicant(mike, fpmi_fac)
test_system.register_applicant(kate, ksis_fac)
mike.add_exam('math')
mike.add_exam('physics')
kate.add_exam('math')
kate.add_exam('physics')
test_system.conduct_exams()
test_system.determine_enrolled_applicants()