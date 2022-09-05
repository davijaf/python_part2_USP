import random
import time

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

    def bubble(self,list):
        last = len(list)

        for i in range(last-1, 0, -1):
            for j in range(i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1],list[j]
        return list

class List:
    def mount_list(self,numbers):
        lists = []
        for i in range(numbers):
            lists.append(random.randint(1,100))
        print("Unorder Lists :",lists)
        return lists

u = List()
antes0 = time.time()
list = u.mount_list(1000)
o = Order()
antes1 = time.time()

print("Order List :",o.bubble(list))
depois = time.time()
print("Execuçao list em",float("{:.2f}".format(antes1-antes0)),"segundos")
print("Execuçao order em",float("{:.2f}".format(depois-antes1)),"segundos")