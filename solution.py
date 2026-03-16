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

if __name__ == '__main__':
    print(zero_duplicate([4,0,1,3,0,2,5,0]))

def zero_duplicate_optimized(inventory):
    sum = 0
    left = 0
    flag = 0
    list_length = len(inventory)
    while sum < list_length
        if inventory[left] == 0:    
            if sum += 2 > list_length:
                flag = 1
                sum += 1
            else:
                sum += 2
        else:
            sum += 1
        left += 1
    
    #when sum == list_length
    if list_length != 0:
        right = list_length - 1
    else:
        right = 0 #break here?
    

    while left >= 0:
        if inventory[left] == 0 and flag == 0:
            inventory[right] = 0
            right -= 1
            left -= 1
            inventory[right] = 0
        else:
            inventory[right] = inventory[left]
            flag = 0
        right -= 1
        left -= 1

    
