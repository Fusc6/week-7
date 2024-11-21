class Operation:
    def __init__(self, first, operator, second):
        self.first = first
        self.second = second
        self.operator = operator
        self.__calculate()
        return
    def __str__(self)->str:
        values = [
            str(self.first),
            self.operator,
            str(self.second),"=",
            str(self.answer)
        ]
        return " ".join(values)
    def __calculator(self):
        operator = self.operator
        try:
            operations = self.__operations()
            operations[operator]()
            pass
        except Exception as e:
            raise e
        return
    def __operations(self):
        operations = {
            "+": self.__add,
            "-": self.__subtract,
            "x": self.__multiply,
            "/": self.__divide
        }
        return operations
    def __add(self):
        self.answer = self.first + self.second
        return
    def __subtract(self):
        self.answer = self.first - self.second
        return
    def __multiply(self):
        self.answer = self.first * self.second
        return
    def __divide(self):
        try:
            self.answer = self.first / self.second
            pass
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")
        return
    def __convert_str_to_num(self, number):
        try:
            #convert string to float
            number = float(number)
            if number.is_integer():
                number = int(number)
                pass
            return number
        except Exception:
            raise Exception("must be a number")
        @property
        def answer(self):
            return self.__answer
        @property
        def first(self):
            return self.__first
        @property
        def second(self):
            return self.__second
        @property
        def operator(self):
            return self.__operator
        @answer.setter
        def answer(self, answer):
            #check to see if the answer can be an integer
            if answer.is_integer():
                answer = int(answer)
                pass
            self.__answer = answer
            return
        @first.setter
        def first(self, first):
            try: 
                self.__first = self.__convert_str_t_num(first)
                pass
            except Exception as e:
                raise e
        @second.setter
        def second(self, second):
            try:
                self.__second = self.__convert_str_to_num(second)
                pass
            except Exception as e:
                raise e
        @operator.setter
        def operator(self, operator):
            operations = self.__operations()
            if operator in operations.keys():
                self.__operator =operator
                return
        pass
    
    class Calculator:
        def __init__(self):
            self.__operation_history = []
            self.__home()
            return
        def __history(self)-> None:
            if(len(self.__operation_history)>0):
                print("History")
                for operation in self.__operation_history:
                    print(operation)
                    pass
                pass
            else:
                print("No History")
                pass
            self.__home()
            return
        def __home(self)->None:
            print("Calculator")
            menu = [
                ("Add", self.__add),
                ("Subtract", self.__subtract),
                ("Mutiply", self.__multiply),
                ("Divide", self.__divide),
                ("History", self.__history),
                ("Close", self.__close)
            ]
            for item in menu:
                index = menu.index(item) + 1
                print(index, item[0])
                pass
            response = input("Please enter an option: ")
            #exception handling
            try:
                index = int(response)
                index -= 1
                option = menu[index]
                option[1]() #run the method
                pass
            except Exception as e:
                print(e)
                print("wrong input, must be a number between 1 and", len(menu))
                self.__home()
                pass
            return
        def __operation(self, first, second, operator):
            try:
                #create an operation and add to history
                operation = Operation(first, operator, second)
                print(operation)
                self.__operation_history.append(operation)
                pass
            except Exception as e:
                print(e)
        def __create_operation(self, operator):
            first = input("please enter a number: ")
            second = input("please enter another number: ")
            try:
                self.__operation(first, second, operator)
                pass
            except Exception as e:
                print(e)
                pass
            finally:
                self.__home
                pass
            return
        
        def __add(self):
            print("Adding")
            self.__create_operation("+")
            return
        def __subtract(self):
            print("Subtracting")
            self.__create_operation("-")
            return
        def __multiply(self):
            print("Mutiplying")
            self.__create_operation("x")
            return
        def __divide(self):
            print("Dividing")
            self.__create_operation("/")
            return
        def __close(self):
            print("Closing")
            return
        pass

    Calculator() #this runs everything
    







                

            
        

        


    


