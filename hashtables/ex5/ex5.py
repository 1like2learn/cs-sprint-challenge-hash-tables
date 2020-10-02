# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    queryDict = {}
    result = []
    
    # Add all the queries to the dictionary so we can check them quickly
    for query in queries:
        queryDict[query] = ''

    # Check all the possible paths. Split the path into nodes using the
    # '/' char. If the last node is in the dict add the path to the result.
    for path in files:
        nodes = path.split('/')
        if nodes[-1] in queryDict:
            result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
