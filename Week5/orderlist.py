import random
import time

class Order:
    def bubble_ef(self,list):
        last = len(list)
        for i in range(last-1, 0, -1):
            change = False
            for j in range(i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1],list[j]
                    change = True
            if not change:
                #print(list)
                return list

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

    def sorted(self,list):
        last = sorted(list)
        return last



class List:
    def mount_list(self,numbers):
        lists = []
        for i in range(numbers):
            lists.append(random.randint(1,numbers))
        #print("Unorder Lists :",lists)
        return lists

    def list_order(self,numbers):
        lists = [x for x in range(numbers)]
        lists[numbers//10] = 500
        return lists

class Count:
    def timer_count(self,number,lists,orders):
        antes0 = time.time()
        u = List()
        list = lists(number)
        o = Order()
        antes1 = time.time()
        orders(list)
        depois = time.time()

        #print("Execuçao list em",float("{:.4f}".format(antes1-antes0)),"segundos")
        print("Execuçao order em",float("{:.4f}".format(depois-antes1)),"segundos")

def tempo():
    x = Count()
    l = List()
    o = Order()
    x.timer_count(1000,l.list_order,o.direct_selection)
    x.timer_count(1000,l.list_order,o.bubble)
    x.timer_count(1000,l.list_order,o.bubble_ef)
    x.timer_count(1000,l.list_order,o.sorted)


#tempo()