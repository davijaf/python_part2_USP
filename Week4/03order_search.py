import random

class Order:
    def direct_selection(self,list):

        finish = len(list)

        for i in range(finish - 1):
            minimal_position = i

            for j in range(i+1, finish):
                if list[j] < list[minimal_position]:
                    minimal_position = j
            list[i], list[minimal_position] = list[minimal_position], list[i]
        return list

class List:
    def mount_list(self,numbers):
        lists = []
        for i in range(numbers):
            lists.append(random.randint(1,10))
        print("Unorder Lists :",lists)
        return lists

u = List()
list = u.mount_list(10)
o = Order()
print("Order List :",o.direct_selection(list))
