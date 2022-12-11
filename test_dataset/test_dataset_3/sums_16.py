def twoSum(numbers, target_val):
    numbers = []
    for i, val in enumerate(numbers):
        numbers.append((i, val))
    numbers = sorted(numbers, key=lambda ele:ele[1])
    right = len(numbers)-1
    left = 0
    index = 1
    while left < right:
        if numbers[left][index]+numbers[right][index] == target_val:
            return sorted([numbers[left][0]+1, numbers[right][0]+1])
        elif numbers[left][index]+numbers[right][index] < target_val:
            left += 1
        else:
            right -= 1

def threeSum(numbers):
    numbers.sort()

    output = set()
    for i in range(len(numbers)):
        target_val = 0 - numbers[i]
        right, left = len(numbers) - 1, i + 1

        while left < right:
            if numbers[left] + numbers[right] == target_val:
                right -= 1
                left += 1
                output.add((numbers[i], numbers[left], numbers[right]))
            
            elif numbers[left] + numbers[right] < target_val: left += 1
            else: right -= 1

    return list(output)

def fourSum(numbers, target_val):
    numbers.sort()
    output = []
    i, length_nums = 0, len(numbers)

    while i < length_nums - 3:
        j = i+1
        while j < length_nums-2:
            left, right = j+1, length_nums-1
            new_target_val = target_val-numbers[i]-numbers[j]
            while left<right:
                if numbers[left]+numbers[right] > new_target_val: right-=1
                elif numbers[left]+numbers[right] < new_target_val: left+=1
                else:
                    output.append([numbers[i],numbers[j],numbers[left],numbers[right]])
                    temp_left, temp_right = numbers[left], numbers[right]
                    
                    while(left<right and numbers[left]==temp_left): left+=1
                    while(left<right and numbers[right]==temp_right): right-=1
            while j < length_nums-3 and numbers[j] == numbers[j+1]: j+=1
            j+=1
        while i < length_nums-4 and numbers[i] == numbers[i+1]: i+=1
        i+=1
    return output