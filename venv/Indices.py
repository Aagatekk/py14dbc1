nums = [2, 17, 11, 8, 3, 15, 3]
target = 9


def indices_of_a_given_sum(nums, target):
    new_list = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            second_substrate = target - nums[i]
            if(nums[j]==second_substrate):
                new_list.append(nums.index(nums[j]))
                new_list.append(nums.index(nums[i]))
            break
        else:
            continue
    return new_list


print(indices_of_a_given_sum(nums, target))