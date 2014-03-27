import Grid
import Vision

if __name__ == '__main__':
    
    # Grid
    g = Grid.Grid()
    print('distance between ' + '(30, 40) to (20,10)')
    distance = g.distance((30, 40), (20,10))
    print distance
    
    print('nearest path to ' + str((30,40)))
    nearest = g.nearest_line((30,40))
    print nearest
    
    print('nearest tree to ' + str((16,32)))
    nearest = g.nearest_tree((16,32))
    print nearest
    
    trees = ['A1', 'B2']
    nail = 'nail1'
    print('path length for ' + str(nail) + ' to ' + str(trees))
    length = g.path_length(nail, trees)
    print length
    
    # Vision
    v = Vision.Vision()
    col = v.find_trees()
    print col
