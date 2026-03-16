def zero_duplicate(inventory):
    '''
    Duplicates zeros and shifts remaining elements to the right. Truncates list at the original length.

    Time: O(n^2)
    Space: O(1)
    '''
    check = 0
    while check < (len(inventory) - 1):
        if inventory[check] == 0:
            inventory.pop()
            check += 1
            inventory.insert(check, 0)
            check += 1
        else:
            check += 1
    return inventory


def zero_duplicate_optimized(inventory):
    '''
    Duplicates zeros and shifts remaining elements to the right. Truncates list at the original length.

    Time: O(n) - improved
    Space: O(1)
    '''
    count = 0
    left = 0
    flag = 0
    list_length = len(inventory)
    right = list_length - 1

    while count < list_length:
        if inventory[left] == 0:
            if count + 2 > list_length:
                flag = 1
                count += 1
            else:
                count += 2
        else:
            count += 1
        left += 1
    
    if left != 0:
        left -= 1
    

    if right >= 0:
        while left >= 0:
            if inventory[left] == 0 and flag == 0:
                inventory[right] = 0
                right -= 1
                inventory[right] = 0
            else:
                inventory[right] = inventory[left]
                flag = 0
            right -= 1
            left -= 1

    return inventory

if __name__ == '__main__':
    inventory = [4,0,1,3,0,2,5,0]
    print(zero_duplicate(inventory))
    print(zero_duplicate_optimized(inventory))