from unittest import result


class Calc:
    def __init__(self, number_1, number_2):
        self.set_number_1 = number_1
        self.set_number_2 = number_2

    def add_number(self):
        result = self.set_number_1 + self.set_number_2
        return result

    def minus_number(self):
        result = self.set_number_1 - self.set_number_2
        return result

    def multi_number(self):
        result = self.set_number_1 * self.set_number_2
        return result



class Make_Array:


    def __init__(self):
        self.result_array = []

    def push_array(self, *arg):
        for element in arg:
            self.result_array.append(element)
        return self.result_array

    def pull_array(self, *arg):
        for element in arg:
            self.result_array.remove(element)

        return self.result_array

    def make_new(self):
        self.result_array = [i for i in range(1, 101)]
        return self.result_array



