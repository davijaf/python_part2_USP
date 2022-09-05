class Search:
    def sequencial_search(self, list, element):
        for i in range(len(list)):
            if list[i] == element:
                return i
        return -1

    def binary_search(self, list, element):
        first = 0
        last = len(list)-1
        while first <= last:
            quite = (first + last)//2
            print(list[quite])
            if list[quite] == element:
                return quite
            else:
                if element < list[quite]:
                    last = quite - 1
                else:
                    first = quite + 1
        return -1

lista = [3, 6, 12, 13, 17, 18, 43]

b = Search()

print(b.binary_search(lista,5))
