# Return the sum of the numbers in the array, except ignore sections of numbers starting
# with a 6 and extending to the next 7 (every 6 will be followed by at least one 7).
# Return 0 for no numbers.


def sum67(nums):
  count = 0
  count2 = 0
  for n in range(len(nums)):
    xn = nums[n]
    count += nums[n]
    if nums[n] == 6:
      count2 += nums[n]
      for r in range(n + 1, len(nums)):
        xr = nums[r]
        if nums[r] == 7:
          count2 += nums[r]
          break
        elif nums[r] == 6:

          break
        else:
          count2 += nums[r]

  return count- count2


print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))  # 236 234



