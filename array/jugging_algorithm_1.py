def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def juggle_rotate(arr, d):
    # If d is 0, no need to perform rotations
    if d == 0:
        return

    # Calculate the number of different sets/cycles we need to loop through
    num_cycles = gcd(len(arr), d)

    # Loop through each set and rotate all elements under it
    for cycle_start_idx in range(num_cycles):

        next_idx = cycle_start_idx
        running_num = arr[cycle_start_idx]

        # Rotate all elements present in the current set/cycle
        # Which starts from "cycle_start_idx"
        while True:
            # Calculate the next index in the current cycle
            next_idx = (next_idx + d) % len(arr)

            # Swap the current element with the running number
            running_num, arr[next_idx] = arr[next_idx], running_num

            # If we've come back to the starting index
            # It means all elements in the current set/cycle are rotated
            if next_idx == cycle_start_idx:
                break


# Lets now test the function

# nums = [1,2,3,4,5,6,7]
nums = [-1,-100,3,99]

arr = nums
juggle_rotate(arr, 2)
print("Array after rotating all elements by 3 positions to the right: ")
print(arr)
