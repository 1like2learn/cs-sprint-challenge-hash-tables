def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    
    # Loop through every array in arrays. If the current number
    # is not in the cache make an entry. If an entry exists 
    # add one to it. If the value of the entry is equal to the 
    # number of arrays add it to the result.
    for array in arrays:
        for num in array:
            if not num in cache:
                cache[num] = 1
            else:
                cache[num] += 1
                if cache[num] == len(arrays):
                    result.append(num)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
