def swap_unique_keys_values(d):
    new = {}
    return [new[value] : key if value not in new else new.pop(value) for key, value in d.items()]
if __name__ == '__main__':
    my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
    new_dict = swap.swap_unique_keys_values(my_dict)
