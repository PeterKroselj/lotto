import random


def is_unique(num, loto_numbers):
    for key in loto_numbers:
        if num == loto_numbers[key]:
            return False
    return True


def sort(loto_numbers):
    sorted = False
    while not sorted:
        sorted = True
        for n in range(7):
            key1 = "num" + str(n + 1)
            key2 = "num" + str(n + 2)
            num1 = loto_numbers[key1]
            num2 = loto_numbers[key2]
            if num1 > num2:
                loto_numbers[key1] = num2
                loto_numbers[key2] = num1
                sorted = False
    return loto_numbers


def get_rnd():
    loto_numbers = {}
    for n in range(8):
        while True:
            num = random.randint(1, 39)
            if is_unique(num, loto_numbers):
                break
        key = "num" + str(n+1)
        loto_numbers.update({key: num})
    return loto_numbers


def print_numbers(loto_numbers):
    for n in range(8):
        key = "num" + str(n+1)
        num = loto_numbers[key]
        print key, num


def get_max(nums):
    max_num = 0
    for key in nums:
        num = nums[key]
        if num > max_num:
            max_num = num
    return max_num


def get_min(nums):
    min_num = 40
    for key in nums:
        num = nums[key]
        if num < min_num:
            min_num = num
    return min_num


nums = get_rnd()
nums = sort(nums)
print_numbers(nums)
# print get_min(nums), get_max(nums)
