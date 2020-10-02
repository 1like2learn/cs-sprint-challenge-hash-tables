def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    
    # For every weight in weights check if limit minus the current
    # value is in the chache. If it is return it in the appropriate 
    # touple. Otherwise add the current value to the cache.
    for i, weight in enumerate(weights):
        if (limit - weight) in cache:
            return (i,cache[limit - weight])
        else:
            cache[weight] = i
    # If we don't find a good pair return none
    return None
