import numpy
import math

class Grid:
    
    ## Init
    def __init__(self):
    
        ## Absolute Position
        self.x_range = 96 # inches
        self.y_range = 96 # inches
        
        ## Tree Locations
        self.trees = {
            'A1' : (16,32),
            'A2' : (16,48),
            'A3' : (16,64),
            'A4' : (16,80),
            'B1' : (32,32),
            'B2' : (32,48),
            'B3' : (32,64),
            'B4' : (32,80),
            'C1' : (48,32),
            'C2' : (48,48),
            'C3' : (48,64),
            'C4' : (48,80),
            'D1' : (64,32),
            'D2' : (64,48),
            'D3' : (64,64),
            'D4' : (64,80),
            'E1' : (80,32),
            'E2' : (80,48),
            'E3' : (80,64),
            'E4' : (80,80)
        }
                        
        ## Blackline Paths
        self.lines = {
            'start1' : [(8,0), (8,24)],
            'start2' : [(48,0),(48,24)],
            'start3' : [(88,0),(88,24)],
            'crossover' : [(8,24),(88,24)],
            'row1' : [(24,24),(24,88)],
            'row2' : [(40,24),(40,88)],
            'row3' : [(56,24),(56,88)],
            'row4' : [(72,24),(72,88)]
        }
        
        ## Nails
        self.nails = {
            'nail1' : (8,0),
            'nail2' : (48,0),
            'nail3' : (88,0)
        }
    
    ## 
    
    ## Distance (Euclidean) between two points
    def distance(self, a, b):
        (a_x, a_y) = a
        (b_x, b_y) = b
        c = math.sqrt((b_x-a_x)**2 + (b_y-a_y)**2)
        return c
        
    ## Nearest black line to the current position (all paths are lateral)
    def nearest_line(self, pos, error=0):
        (pos_x, pos_y) = pos
        shortest = self.x_range # no paths longer than the lateral dimensions
        for line_name in self.lines:
            line = self.lines[line_name]
            (start_x, start_y) = line[0]
            (end_x, end_y) = line[1]
            try:
                dist = abs(start_x - pos_x)
            except ZeroDivisionError as error:
                dist = abs(start_y - pos_y)
            if dist < shortest:
                shortest = dist
        return shortest

    ## Nearest tree to the current position
    def nearest_tree(self, pos, error=0):
        (pos_x, pos_y) = pos
        shortest = self.x_range # no paths longer than the lateral dimensions
        for tree_name in self.trees:
            tree = self.trees[tree_name]
            dist = self.distance(pos, tree)
            if dist < shortest:
                shortest = dist
        return shortest
        
    ## Path Length for a trial run of 1 nail + N trees
    def path_length(self, nail_name, tree_names):
        length = 0
        nail = self.nails[nail_name]
        for tree_num in range(len(tree_names)):
            if tree_num == 0:
                tree = self.trees[tree_names[tree_num]]
                dist = self.distance(nail, tree)
            elif tree_num == len(tree_names):
                dist = 0
            else:
                a = self.trees[tree_names[tree_num - 1]]
                b = self.trees[tree_names[tree_num]]
                dist = self.distance(a,b)
            print dist
            length += dist
        return length
    
