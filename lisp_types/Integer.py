from .Boolean import Boolean

class Integer:
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
        else:
            raise TypeError("Integer must be initialized with an integer")

    def __add__(self, int2):
        if isinstance(int2, Integer):
            return Integer(self.val + int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __iadd__(self, int2):
        if isinstance(int2, Integer):
            self.val += int2.val
            return self
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __sub__(self, int2):
        if isinstance(int2, Integer):
            return Integer(self.val - int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __mul__(self, int2):
        if isinstance(int2, Integer):
            return Integer(self.val * int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __imul__(self, int2):
        if isinstance(int2, Integer):
            self.val *= int2.val
            return self
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __floordiv__(self, int2):
        if isinstance(int2, Integer):
            if int2.val != 0:
                return Integer(self.val // int2.val)
            else:
                raise ZeroDivisionError
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")
    
    def __mod__(self, int2):
        if isinstance(int2, Integer):
            if int2.val != 0:
                return Integer(self.val % int2.val)
            else:
                raise ZeroDivisionError
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __lt__(self, int2):
        if isinstance(int2, Integer):
            return Boolean(self.val < int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __gt__(self, int2):
        if isinstance(int2, Integer):
            return Boolean(self.val > int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __eq__(self, int2):
        if isinstance(int2, Integer):
            return Boolean(self.val == int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __le__(self, int2):
        if isinstance(int2, Integer):
            return Boolean(self.val <= int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __ge__(self, int2):
        if isinstance(int2, Integer):
            return Boolean(self.val >= int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __ne__(self, int2):
        if isinstance(int2, Integer):
            return Boolean(self.val != int2.val)
        else:
            raise TypeError(f"Expect type 'Integer', got '{int2.__class__.__name__}'")

    def __str__(self):
        return str(self.val)
    