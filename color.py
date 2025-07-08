class Colors: 
        dark_grey = (40, 44, 55)
        green = (64, 255, 64)
        red = (255, 77, 77)
        orange = (255, 140, 50)
        yellow = (255, 255, 80)
        purple = (204, 51, 255)
        cyan = (51, 255, 255)
        blue = (56, 107, 255)
        white = (255, 255, 255)
        dark_blue = (102, 153, 204)
        light_blue = (59, 85, 162)
        

        @classmethod
        def get_cell_color(cls): 
            return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
