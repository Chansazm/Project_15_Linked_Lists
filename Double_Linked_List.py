class DLLNode:
    def __init__(self, data):
        self.data = []
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_data):
        self.next = new_data

    def __repr__(self):
        return "Node object : data={}".format(self.data)

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous
