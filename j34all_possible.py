import itertools

class ListOps():
    
    def __init__(self, length=9, total=100):
        self.length = length
        self.total = total
        temp_list = []
        temp_value = [0, 1, -1]
        temp_value = tuple(temp_value)
        temp_list.append(temp_value)
        for i in range(2, self.length):
            temp_value = [0, i, -i, (10 * (i - 1)) + i, - ((10 * (i - 1)) + i)]
            temp_value = tuple(temp_value)
            temp_list.append(temp_value)
        temp_value = [self.length, - (self.length),
                      (10 * (self.length - 1)) + self.length, -
                      ((10 * (self.length - 1)) + self.length)]
        temp_list.append(temp_value)
        self.poss_values = tuple(temp_list)
        self.valid_list = []
        self.final_list = []
        
    def _make_full_list(self):
        self.full_list = list(itertools.product(*self.poss_values))

    def _is_valid(self, num_list):
        for i in range(1, len(num_list)):
            if abs(num_list[-(i)]) > 10 and abs(num_list[-(i) -1]) > 0:
                return False
            elif abs(num_list[-(i)]) < 10 and num_list[-(i) -1] == 0:
                return False
        return True
       
    def _make_valid_list(self):
        for i in range(0, len(self.full_list)):
            if self._is_valid(self.full_list[i]):
                self.valid_list.append(self.full_list[i])

    def _equals_total(self, num_list):
        total = 0
        for i in range(0, len(num_list)):
            total += num_list[i]
        if total == self.total:
            return True
        else:
            return False            
            
    def _make_final_list(self):
        for i in range(0, len(self.valid_list)):
            if self._equals_total(self.valid_list[i]):
                self.final_list.append(self.valid_list[i])

    def _print_final_list(self):
        for i in range(len(self.final_list)):
            for j in range(len(self.final_list[i])):
                if self.final_list[i][j] == 0:
                    print('', end = '')
                elif self.final_list[i][j] > 0:
                    print('+', self.final_list[i][j], ' ', end = '')
                elif self.final_list[i][j] < 0:
                    print('-', abs(self.final_list[i][j]), ' ', end = '')
            print('')

    def run(self):
        self._make_full_list()
        self._make_valid_list()
        self._make_final_list()
        self._print_final_list()

def main():
    list_obj = ListOps()
    list_obj.run()    

if __name__ == '__main__':
    main()
