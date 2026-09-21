class station:

    def __init__(self, name):
        self.name = name
        self.next = None

    def __str__(self):
        next_name = "nowhere" if self.next is None else self.next.name
        return f"[{self.name} --> <{next_name}>"

