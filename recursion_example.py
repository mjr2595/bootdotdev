weapons = {
    "melee_weapons": {
        "stabbies": {"spears": 4, "daggers": 2},
        "smashies": {"hammers": 5, "maces": 3},
    },
    "ranged_weapons": {
        "pew_pew": {"crossbows": 6, "guns": {"pistols": 7, "rifles": 8}},
        "throwy": {"rocks": 1, "darts": 1},
    },
}


# def dict_depth(d, max_depth_so_far=1):
#     if not isinstance(d, dict) or not d:
#         return max_depth_so_far
#     return max(dict_depth(v, max_depth_so_far + 1) for v in d.values())


def dict_depth(d, max_depth_so_far=1):
    if not isinstance(d, dict) or not d:
        return max_depth_so_far

    current_max = max_depth_so_far

    for v in d.values():
        depth_of_subdict = dict_depth(v, max_depth_so_far + 1)
        if depth_of_subdict > current_max:
            current_max = depth_of_subdict

    return current_max


print(dict_depth(weapons))
print(dict_depth({}))  # Empty dict
print(dict_depth({"a": 1, "b": 2}))  # Flat dict
print(dict_depth({"a": {"b": {"c": 1}}}))  # Nested dict
print(dict_depth({"a": {"b": {"c": 1}}, "d": {"e": 2}}))  # Multiple nested dict


def sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum(nums[1:])


print(sum([1, 2, 3, 4, 5]))  # 15


def factorial_r(x):
    if x == 1:
        return 1
    return x * factorial_r(x - 1)


print(factorial_r(5))  # 120
print(factorial_r(3))  # 6
