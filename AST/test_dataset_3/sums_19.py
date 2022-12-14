def whole():
    def twoSum(arr, val):
        arr = enumerate(arr)
        arr = sorted(arr, key=lambda e:e[1])
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l][1]+arr[r][1] == val:
                return sorted([arr[l][0]+1, arr[r][0]+1])
            elif arr[l][1]+arr[r][1] < val:
                l += 1
            else:
                r -= 1

    def threeSum(arr):
        arr = sorted(arr)
        res = set()
        i = 0
        while i < len(arr):
            l = i + 1
            r = len(arr) - 1
            val = 0 - arr[i]
            while l < r:
                if arr[l] + arr[r] == val:
                    res.add((arr[i], arr[l], arr[r]))
                    l += 1
                    r -= 1
                elif arr[l] + arr[r] < val:
                    l += 1
                else:
                    r -= 1
        return list(res)

    def fourSum(arr, val):
        arr.sort()
        i = 0
        length_arr = len(arr)
        res = []
        while i < length_arr-3:
            j = i+1
            while j < length_arr-2:
                l = j+1
                r = length_arr-1
                val2 = val-arr[i]-arr[j]
                while l<r:
                    if arr[l]+arr[r] > val2:
                        r-=1
                    elif arr[l]+arr[r] < val2:
                        l+=1
                    else:
                        res.append([arr[i],arr[j],arr[l],arr[r]])
                        l_temp = arr[l]
                        r_temp = arr[r]
                        while(l<r and arr[l]==l_temp):
                            l+=1
                        while(l<r and arr[r]==r_temp):
                            r-=1
                while j < length_arr-3 and arr[j] == arr[j+1]:
                    j+=1
                j+=1
            while i < length_arr-4 and arr[i] == arr[i+1]:
                i+=1
            i+=1
        return res