class SSLNode:

    def __init__(self, data):
        """Create the node
        """
        self.data = []
        self.next = None

    def get_data(self):
        """
        Return the data from the self.data
        """
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_data):
        self.next = new_data

    def __repr__(self):
        return "Node object : data = {}.format(self.data)"


#*###########################################################################

class SLL:

    def __init__(self):
        self.head = None
