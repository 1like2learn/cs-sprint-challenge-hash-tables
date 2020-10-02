#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []
    # For every ticket store it's key = source and value = destination
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # Check every link in the chain of locations until the destination 
    # is "NONE." Append places to the route list in the order they are 
    # in the chain.
    place = cache["NONE"]
    while not place == "NONE":
        route.append(place)
        place = cache[place]
        
    # Add None because that needs to be on the end of the list for 
    # some reason.
    route.append(place)
    return route
