nums = list(map(int,input().split()))
nums = sorted(nums)
maior = nums[3]

if nums[0] + nums[1] > nums[2]:
    print("S")
else:
    if nums[0] + nums[1] > nums[2]:
        print("S")
    else:
        if nums[0] + nums[2] > nums[3]:
            print("S")
        else:
            if nums[1] + nums[2] > nums[3]:
                print("S")
            else:
                print("N")

