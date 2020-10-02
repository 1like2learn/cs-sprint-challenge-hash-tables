def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    
    # For every number in the list check if an opposite sign
    # version is in the cache. if it is add it's absolute 
    # value to the result. if the number is not in the cache 
    # add it.
    for num in a:
        if (-num) in cache:
            result.append(abs(num))
        elif not num in cache:
            cache[num] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
