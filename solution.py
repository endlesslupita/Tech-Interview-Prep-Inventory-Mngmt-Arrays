def zero_duplicate(inventory_list):
        check = 0
        while inventory_list:
                if inventory_list[check] == 0:
                        inventory_list.pop()
                        check += 1
                        inventory_list[check].insert(0)
                        check += 1
                else:
                        check += 1