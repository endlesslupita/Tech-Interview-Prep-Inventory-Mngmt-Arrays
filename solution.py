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
    position = 0
    list_length = len(inventory)
    while sum < list_length
        if inventory[position] == 0 and sum += 2 <= list_length:
            sum += 2
        else:
            sum += 1

        position += 1
    #when sum == list_length
    if sum != 0:
        right = sum - 1
    else:
        right = 0
    if list_length != 0:
        left = list_length - 1
    else:
        left = 0 #break here?
    
    while 
    inventory[list_length - ] = inventory[-zero_count]
        inventory[right] = inventory[left]
    zero_count += 1
