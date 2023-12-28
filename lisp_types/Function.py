from .Integer import Integer
from .Boolean import Boolean

class Function:
    class _OpTreeNode:
        def __init__(self, op, child):
            self.action = op if op else lambda x: x
            self.child = child

        def _set_action(self, action):
            self.action = action

        def _evaluate(self):
            param = []
            for c in self.child:
                if isinstance(c, Function._OpTreeNode):
                    param.append(c._evaluate())
                elif isinstance(c, Function.var):
                    param.append(c.val)
                else:
                    param.append(c)
            return self.action(param)

        def __str__(self):
            return f'({self.op} {" ".join([Function._OpTreeNode.stringify(c) for c in self.child])})'

        @staticmethod
        def stringify(node):
            return str(node)
        
        
    class var:
        def __init__(self, val=None, type=None):
            self.val = val
            self.type = type

        def _set(self, v):
            self.val = v
            self.type = type(v)

        def _evaluate(self):
            return self.val

        def _set_Int(self, val):
            self._set(Integer(val))

        def _set_Bool(self, val):
            self._set(Boolean(val))
    

    def __init__(self, parameters, func_body):
        self.parameters = parameters
        self.func_tree = func_body

    def evaluate(self):
        return self.func_tree._evaluate() if isinstance(self.func_tree, Function._OpTreeNode) else self.func_tree