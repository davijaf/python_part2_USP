def bubble_sort(list):
    last = len(list)
    test = sorted(list)
    if last > 1:
        for i in range(last-1,0,-1):
            change = False
            for j in range(i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1],list[j]
                    print(list)
                    change = True
            if test == list or not change:
                return list
    else:
        return list

#print(bubble_sort([5]))
#print(bubble_sort([1,2,3,4,5,0]))
#print(bubble_sort([0, 1, 6, 19, 8, 25, 26, 15, 16, 29, 31, 33, 45, 48, 52, 37, 53, 28, 54, 56, 17, 10, 24, 57, 49, 64, 2, 66, 68, 70, 34, 38, 32, 63, 71, 72, 11, 27, 9, 50, 65, 74, 67, 60, 55, 21, 42, 40, 51, 4, 39, 76, 41, 7, 22, 79, 14, 75, 80, 82, 47, 5, 18, 83, 73, 12, 84, 62, 81, 85, 69, 58, 59, 43, 78, 87, 13, 88, 46, 44, 20, 86, 36, 61, 30, 77, 35, 23, 3, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
#print(bubble_sort([1, 5, 3, 4, 2, 0]))
