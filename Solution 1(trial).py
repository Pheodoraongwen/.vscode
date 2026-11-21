"""
Get a sum of all numbers from a list that are
unique. If a number appears in the list more
than once, do not include it in the total sum.

Example 1
Input: [1,1,2,3]
Output: 5

Example 2
Input: [1,2,3]
Output: 6
"""
def sum_of_numbers(arr):
    Sorted_arr = sorted(arr)
    sum = 0
    for num in Sorted_arr:
        sum += num
    for i in Sorted_arr:
        n = Sorted_arr.count(i)
        if n > 1:
            sum = sum-n*i
            Sorted_arr.pop(i)
        else:
            sum = sum
    print(sum)
numbers = [1,2,3]
sum_of_numbers(numbers)
