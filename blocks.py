from block import Block
from position import Position
class LBlock(Block) :
    def __init__(self):
        super().__init__(id =1)
        self.cells = { 
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1),Position(2,1), Position(2,2)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)]
        }
        self.move(0,3)

class JBlock(Block): 
    def __init__(self):
        super().__init__(id =2)
        self.cells = {
                0: [Position(0, 0), Position(1, 0),Position(1,1), Position(2, 0)],  # L shape
                1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],  # Bottom row shape
                2: [Position(1,0), Position(1, 1), Position(1, 2), Position(2,2)],  # Top row
                3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2,1)]   # J with horizontal
        }
        self.move(0,3)


class IBlock(Block): 
    def __init__(self):
        super().__init__(id =3)
        self.cells = {
                0: [Position(0, 0), Position(1, 0),Position(1,1), Position(2, 0)],  # L shape
                1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],  # Bottom row shape
                2: [Position(1,0), Position(1, 1), Position(1, 2), Position(2,2)],  # Top row
                3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2,1)]   # J with horizontal
        }
        self.move(-1,3)


class OBlock(Block): 
    def __init__(self):
        super().__init__(id =4)
        self.cells = {
                0: [Position(0, 0), Position(0,1),Position(1,0), Position(1, 1)]
        }
        self.move(0,4)

class SBlock(Block): 
    def __init__(self):
        super().__init__(id =5)
        self.cells = {
                0: [Position(0,1), Position(0,2),Position(1,0), Position(1, 1)],  # L shape
                1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],  # Bottom row shape
                2: [Position(1,1), Position(1, 2), Position(2,0), Position(2,1)],  # Top row
                3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2,1)]   # J with horizontal
        }
        self.move(0,3)


class TBlock(Block): 
    def __init__(self):
        super().__init__(id =6)
        self.cells = {
                0: [Position(0, 1), Position(1, 0),Position(1,1), Position(1, 2)],  # L shape
                1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],  # Bottom row shape
                2: [Position(1,0), Position(1, 1), Position(1, 2), Position(2,1)],  # Top row
                3: [Position(0, 1), Position(1, 0), Position(1,1), Position(2,1)]   # J with horizontal
        }
        self.move(0,3)
        
class ZBlock(Block): 
    def __init__(self):
        super().__init__(id =7)
        self.cells = {
                0: [Position(0, 0), Position(0, 1),Position(1,1), Position(1, 2)],  # L shape
                1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],  # Bottom row shape
                2: [Position(1,0), Position(1, 1), Position(2,1), Position(2,2)],  # Top row
                3: [Position(0, 1), Position(1, 0), Position(1,1), Position(2,0)]   # J with horizontal
        }
        self.move(0,3)


        
        