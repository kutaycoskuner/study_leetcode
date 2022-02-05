def Main():
    # ==== test
    nums = [3,3,4,15]
    target = 6
    
    # ==== logic
    for ii in range(0, len(nums)):
        for yy in range(ii+1, len(nums)):
            if yy+1 <= len(nums):
                if nums[ii]+nums[yy] == target:
                    print(ii, yy)
                    return [ii, yy]

if __name__ == "__main__":
    Main()