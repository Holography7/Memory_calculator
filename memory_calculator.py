import math

class Program():

    def main(self):
        command_line = Command_line()
        command_line.create()

    def str_to_digit(self, num_str):
        if (type(num_str) == str):
            if (num_str.isdigit()):
                return int(num_str)
            else:
                if (num_str.count('.') == 1):
                    float_temp_number = num_str.split('.')
                    if (float_temp_number[0].isdigit() and float_temp_number[1].isdigit()):
                        return float(num_str)
                    else:
                        print('String to digit convert error: one part of number is not digit.')
                        return None
                else:
                    print('String to digit convert error: getted not a number (getted {}).'.format(num_str))
                    return None
        else:
            print('String to digit convert error: getted not str (getted {})'.format(type(num_str)))
            return None

    def read_txt(self, file_name, txt_encoding):
        txt_file = open(file_name, 'r', encoding=txt_encoding)
        data = txt_file.read()
        txt_file.close()
        return data

class Command_line(Program):

    def __init__(self):

        def __plus(number_1, number_2):
            if ((type(number_1) == User_number) and (type(number_2) == User_number)):
                number_1.bits += number_2.bits
                number_1.update_number()
                return number_1
            else:
                print('Plus operator error: wrong input numbers (getted {} and {}).'.format(type(number_1), type(number_2)))
                return None

        def __multiplication(number_1, number_2):
            if ((type(number_1) == User_number) and ((type(number_2) == float) or (type(number_2) == int))):
                number_1.bits = math.ceil(number_1.bits * number_2)
                number_1.update_number()
                return number_1
            else:
                print('Multiplication operator error: wrong input numbers (getted {} and {}).'.format(type(number_1), type(number_2)))
                return None

        self.user_string = ''
        self.number_1 = User_number('0 b')
        self.number_2 = User_number('0 b')
        self.__operators_syms = ('*', '/', '+', '-')
        self.__operators_objects = (Operators('*', lambda num_1, num_2: __multiplication(num_1, num_2)), Operators('/', lambda num_1, num_2: __multiplication(num_1, 1 / num_2)), Operators('+', lambda num_1, num_2: __plus(num_1, num_2)), Operators('-', lambda num_1, num_2: __plus(num_1, num_2.negative())))
        self.__help = self.read_txt('README.txt', 'utf-8')
        self.__help_ru = self.read_txt('README (RU).txt', 'utf-8')
        self.__changelogs = self.read_txt('changelog.txt', 'utf-8')

    def create(self):
        print('Memory calculator v.0.2.7 alpha by Holography_7.\nType "help" to know how use this calculator (or "help ru" for same on russian language).\nType "changelog" to see changelogs.\nType "exit" to close calculator.')
        self.user_string = input('> ')
        while (self.user_string != 'exit'):
            if (self.user_string == 'help'):
                print(self.__help)
            elif (self.user_string == 'help ru'):
                print(self.__help_ru)
            elif (self.user_string == 'changelog'):
                print(self.__changelogs)
            else:
                exist_operators = [False, False, False, False]
                for i in range(len(self.__operators_syms)):
                    if (self.user_string.count(self.__operators_syms[i]) != 0):
                        exist_operators[i] = True
                if (exist_operators == [False, False, False, False]):
                    print('Command error: unknown command "{}"'.format(self.user_string))
                else:
                    user_command = self.user_string.replace(' ', '')
                    temp_command = user_command
                    list_command = []
                    for i in range(len(user_command)):
                        for j in range(len(self.__operators_syms)):
                            if (user_command[i] == self.__operators_syms[j]):
                                list_command.extend(temp_command.partition(self.__operators_syms[j]))
                                temp_command = list_command[len(list_command) - 1]
                                list_command.pop(len(list_command) - 1)
                    list_command.append(temp_command)
                    abort_command = False
                    for i in range(len(self.__operators_syms)):
                        for j in range(list_command.count(self.__operators_syms[i])):
                            oper_index = list_command.index(self.__operators_syms[i])
                            if (oper_index - 1 >= 0):
                                numbers = [list_command[oper_index - 1], list_command[oper_index + 1]]
                                if ((type(numbers[0]) == str) or (type(numbers[1]) == str)):
                                    for k in range(len(numbers)):
                                        if (type(numbers[k]) == str):
                                            if ((numbers[k].count('b') == 1) or (numbers[k].count('B') == 1)):
                                                numbers[k] = User_number(numbers[k])
                                            else:
                                                numbers[k] = self.str_to_digit(numbers[k])
                                new_number = self.__operators_objects[i]._action(numbers[0], numbers[1])
                                list_command[oper_index - 1] = new_number
                                list_command.pop(oper_index + 1)
                                list_command.pop(oper_index)
                            else:
                                print('Command error: number before "{}" not found.'.format(list_command[oper_index]))
                                abort_command = True
                                break
                        if (abort_command):
                            break
                    print('{} {} ({} bits)'.format(str(list_command[0].user_number), list_command[0].user_metric, str(list_command[0].bits)))
            self.user_string = input('> ')
        print('Bye.')

class User_number(Program):

    def __init__(self, input_number):
        self.__metrics = {'b': 1, 'B': 8, 'K': 1024, 'M': 1048576, 'G': 1073741824, 'T': 1099511627776, 'P': 1125899906842624, 'E': 1152921504606846976, 'Z': 1180591620717411303424, 'Y': 1208925819614629174706176, 1: 'b', 8: 'B', 1024: 'K', 1048576: 'M', 1073741824: 'G', 1099511627776: 'T', 1125899906842624: 'P', 1152921504606846976: 'E', 1180591620717411303424: 'Z', 1208925819614629174706176: 'Y'}
        if (input_number.count(' ') != 0):
            temp_number = input_number.split(' ')
        else:
            if (input_number.find('b') == len(input_number) - 1) or (input_number.find('B') == len(input_number) - 1):
                if (self.__metrics.get(input_number[len(input_number) - 2])):
                    temp_number = [input_number[:len(input_number) - 2], input_number[len(input_number) - 2:len(input_number)]]
                else:
                    temp_number = [input_number[:len(input_number) - 1], input_number[len(input_number) - 1]]
            else:
                print('User number error: wrong input number (getted {})'.format(temp_number))
                return False
        temp_number[0] = self.str_to_digit(temp_number[0])
        if (temp_number[0] == None):
            return False
        else:
            self.user_number = temp_number[0]
        self.user_metric = temp_number[1]
        if (self.user_number >= 1024) and (self.user_metric[0] != 'Y'):
            while(self.user_number >= 1024):
                self.user_number = self.user_number / 1024
                if ((self.user_metric == 'b') or (self.user_metric == 'B')):
                    self.user_metric = 'K' + self.user_metric
                else:
                    self.user_metric = self.__metrics[self.__metrics[self.user_metric[0]] * 1024] + self.user_metric[1]
        elif (self.user_number < 1) and (self.user_number >= 0) and ((self.user_metric[0] != 'b') or (self.user_metric[0] != 'B')):
            while (self.user_number < 1):
                if ((self.user_metric == 'b') or (self.user_metric == 'B')):
                    break
                self.user_number = self.user_number * 1024
                if (self.user_metric[0] == 'K'):
                    self.user_metric = self.user_metric[1]
                else:
                    self.user_metric = self.__metrics[self.__metrics[self.user_metric[0]] / 1024] + self.user_metric[1]
        if (len(self.user_metric) == 1):
            self.bits = round(self.user_number * self.__metrics[self.user_metric])
        elif (len(self.user_metric) == 2):
            self.bits = round(self.user_number * self.__metrics[self.user_metric[0]] * self.__metrics[self.user_metric[1]])
        else:
            print('Calculating bits error: len metrics more than 2 or = 0 (getted {}).'.format(len(self.user_metric)))
            return False
        if (self.user_metric == 'b'):
            self.user_number = self.bits

    def convert_over_metric(self, new_metric):
        if (new_metric == 'b'):
            self.user_number = self.bits
        elif (new_metric == 'B'):
            self.user_number = self.bits / 8
        elif (len(new_metric) == 2):
            if (self.__metrics.get(new_metric[0]) and self.__metrics.get(new_metric[1])):
                self.user_number = self.bits / self.__metrics[new_metric[0]] / self.__metrics[new_metric[1]]
                if (self.user_number.is_integer()):
                    self.user_number = int(self.user_number)
            else:
                print('Convert error: wrong metrics.')
                return False
        else:
            print('Convert error: wrong metrics.')
            return False
        self.user_metric = new_metric
        return True

    def update_number(self):
        new_number = self.bits
        if (len(self.user_metric) == 2):
            new_metric = self.user_metric[1]
        else:
            new_metric = self.user_metric
        if (new_metric == 'B') and (new_number > 8):
            new_number = new_number / 8
        i = 1
        new_metric_2 = ''
        while (new_number > 1024):
            new_number = new_number / 1024
            new_metric_2 = self.__metrics[1024 ** i]
            i += 1
        self.user_metric = new_metric_2 + new_metric
        self.user_number = new_number

    def negative(self):
        self.user_number = -self.user_number
        self.bits = -self.bits
        return self

class Operators(Program):

    def __init__(self, sym, action_func):
        if (type(sym) == str):
            self.__sym = sym
        else:
            print('Creating operator error: variable "sym" not string (getted {}).'.format(str(type(sym))))
            return False
        if (type(action_func) == type(lambda: print('0'))):
            self._action = action_func
        else:
            print('Creating operator error: variable "action_func" not function (getted {}).'.format(str(type(action_func))))
            return False

program = Program()
program.main()
