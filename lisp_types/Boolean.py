class Boolean:
    def __init__(self, val):
        if isinstance(val, bool):
            self.val = val
        else:
            raise TypeError("Boolean must be initialized with a boolean value")

    def __bool__(self):
        return self.val

    def __and__(self, bool2):
        if isinstance(bool2, Boolean):
            return Boolean(self.val and bool2.val)
        else:
            raise TypeError(f"Expect type 'Boolean', got {bool2.__class__.__name__}")

    def __or__(self, bool2):
        if isinstance(bool2, Boolean):
            return Boolean(self.val or bool2.val)
        else:
            raise TypeError(f"Expect type 'Boolean', got {bool2.__class__.__name__}")

    def __not__(self):
        return Boolean(not self.val)

    def __eq__(self, bool2):
        if isinstance(bool2, Boolean):
            return Boolean(self.val == bool2.val)
        else:
            raise TypeError(f"Expect type 'Boolean', got {bool2.__class__.__name__}")

    def __ne__(self, bool2):
        if isinstance(bool2, Boolean):
            return Boolean(self.val != bool2.val)
        else:
            raise TypeError(f"Expect type 'Boolean', got {bool2.__class__.__name__}")

    def __str__(self):
        return '#t' if self.val else '#f'
    