import cv2
import numpy

class Vision:

    def __init__(self, index=0):
        self.cam = cv2.VideoCapture(index)
    
    ## Find Trees by
    def find_trees(self, num_trees=12):
        (s, rgb) = self.cam.read()
        if s:
            hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
            sat = hsv[:,:,1]
            eri = sat # > threshold 
            columns = numpy.sum(eri, axis=1)
            image_width = columns.size
            probabilities = []
            for pix in range(image_width):
                if columns[pix] > (numpy.mean(columns) + 1*numpy.std(columns)):
                    probabilities.append(pix)
            return probabilities
        else:
            raise Exception
            
    def __close__(self):
        pass
