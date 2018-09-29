print("hello word!")

def binary_search(my_list, value):
    start = 0
    end = len(my_list) - 1
    if value == my_list[start]:
        return start
    if value == my_list[end]:
        return end

    while end >= start:
        mid = (end + start) // 2
        if my_list[mid] < value:
            start = mid + 1
        elif my_list[mid] > value:
            end = mid -1
        else:
            return mid
    return None

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    value = 3
    print(binary_search(my_list, value))
    
