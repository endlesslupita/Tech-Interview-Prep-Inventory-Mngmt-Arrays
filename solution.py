def zero_duplicate(inventory_list):
        check = 0
        while check < (len(inventory_list) - 1):
                if inventory_list[check] == 0:
                        inventory_list.pop()
                        check += 1
                        inventory_list.insert(check, 0)
                        check += 1
                else:
                        check += 1
        return inventory_list

if __name__ == '__main__':
        print(zero_duplicate([4,0,1,3,0,2,5,0]))