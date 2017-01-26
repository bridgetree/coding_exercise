def twoSum(nums, target):
    check = {}
    for i,num in enumerate(nums):
        if num not in check:
             check[target-num]=i
        else:
             return [check[num],i]
