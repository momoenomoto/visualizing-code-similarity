def twoSum(numbers, target_val):
    numbers = enumerate(numbers)
    numbers = sorted(numbers, key=lambda x:x[1])
    left, right = 0, len(numbers)-1
    while left < right:
        if numbers[left][1]+numbers[right][1] == target_val:
            return sorted([numbers[left][0]+1, numbers[right][0]+1])
        elif numbers[left][1]+numbers[right][1] < target_val:
            left += 1
        else:
            right -= 1

def threeSum(numbers):
    numbers = sorted(numbers)
    output = set()
    for i in range(len(numbers)):
        left = i + 1
        right = len(numbers) - 1
        target_val = 0 - numbers[i]
        while left < right:
            if numbers[left] + numbers[right] == target_val:
                output.add((numbers[i], numbers[left], numbers[right]))
                left += 1
                right -= 1
            elif numbers[left] + numbers[right] < target_val:
                left += 1
            else:
                right -= 1
    return list(output)

def fourSum(numbers, target_val):
    numbers.sort()
    i = 0
    length_nums = len(numbers)
    output = []
    while i < length_nums-3:
        j = i+1
        while j < length_nums-2:
            left = j+1
            right = length_nums-1
            new_target_val = target_val-numbers[i]-numbers[j]
            while left<right:
                if numbers[left]+numbers[right] > new_target_val:
                    right-=1
                elif numbers[left]+numbers[right] < new_target_val:
                    left+=1
                else:
                    output.append([numbers[i],numbers[j],numbers[left],numbers[right]])
                    temp_left = numbers[left]
                    temp_right = numbers[right]
                    while(left<right and numbers[left]==temp_left):
                        left+=1
                    while(left<right and numbers[right]==temp_right):
                        right-=1
            while j < length_nums-3 and numbers[j] == numbers[j+1]:
                j+=1
            j+=1
        while i < length_nums-4 and numbers[i] == numbers[i+1]:
            i+=1
        i+=1
    return output