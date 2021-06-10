def three_sum(arr, target):
    # sort
    arr.sort()
    # make out array
    out = [[]]
    # define 3 pointers
    lp = 0
    mp = 1
    rp = len(arr) - 1
    # while the lp is less than the length of the array -2
    while lp < len(arr) - 2:
        # while the mp is less than the rp
        while mp < rp:
            # check for target
            total = arr[lp] + arr[mp] + arr[rp]
            if total == target:
                arr.append()
            # if the sum is less than target mp ++
            elif total < target:
                mp += 1
            # if sum is greater than target rp --
            else: # total > target:
                rp -= 1
        # lp ++
        lp += 1
        # mp lp + 1
        mp = lp + 1
    # return out array
    return out
