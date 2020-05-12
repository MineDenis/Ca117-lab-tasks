import sys
def swap_unique_keys_values(d):
    for i in d:
        print(i)
     #return dict([(value, key) for key, value in d.items()])
if __name__ == '__main__':
    import swap_v2_042 as swap
    my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
    new_dict = swap.swap_unique_keys_values(my_dict)
    print(new_dict)