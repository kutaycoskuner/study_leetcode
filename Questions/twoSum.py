def Main():
    # ==== test
    nums = [3,3,4,15]
    target = 6
    
    # ==== logic
    dict = {}
    for ii in range(0, len(nums)):
        if nums[ii] in dict:
            # print(dict[nums[ii]],ii)
            return [dict[nums[ii]],ii]
        dict[target - nums[ii]] = ii
    
    # :: ilk cozum
    # for ii in range(0, len(nums)):
    #     for yy in range(ii+1, len(nums)):
    #         if yy+1 <= len(nums):
    #             if nums[ii]+nums[yy] == target:
    #                 print(ii, yy)
    #                 return [ii, yy]

if __name__ == "__main__":
    Main()