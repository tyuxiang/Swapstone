from capstone.models import Booth
import math
from copy import deepcopy

class Group:
    def __init__(self,shape,start=(0,0),end=(0,0),radius=0,centre=(0,0)):
        self.start = start
        self.end = end
        self.radius = radius
        self.centre = centre
        self.shape = shape
        if shape == 'square':
            self.point = list(start)

    def add(self, booth):
        if self.shape == "square":
            # do we need to check for width?
            print("Adding to square space")
            if(self.point[0]+booth.length_pixel <=self.end[0]):
                booth.position_x = self.point[0]
                booth.position_y = self.point[1]
                self.point[0] = self.point[0] + booth.length_pixel
                booth.save()
                print("Booth updated")
                return True
            else:
                return False
        # elif self.shape =="circle":
        #     # do we need to check for width?
        #     angle = 2*math.asin((booth.length_pixel/self.radius)/2)
        #     check = []
        #     check[0] = self.length_pixel + self.length*math.sin(angle)
        #     check[1] = self.length_pixel + self.length*math.cos(angle)
        #     if(self.point[0]+booth.length_pixel <=self.end[0]):
        #         booth.position_x = self.point[0]
        #         booth.position_y = self.point[1]
        #         self.point[0] = self.point[0] + booth.length_pixel
        #         return True
        #     else:
        #         return False





def allocate():
    booths = Booth.objects.all()
    groups = [Group(shape="square",start = (280,225),end = (480,225)),
    Group(shape="square",start = (220,400),end = (540,400))]
    # Group(centre = (680,237),start = (570,280),end = (760,170),radius = 110, shape = "circle"),
    # Group(centre= (80,250),start = (30,160),end = (100,340),radius = 110,shape = "circle")]
    industries = [str(1),str(2)]
    i = 0
    check = 0
    print("Starting allocation algorithm")
    #booths = deepcopy(final_booths)
    for industry in industries:
        for booth in booths:
            print("Choosing booth")
            print(type(industry))
            print(type(booth.industry))
            print(booth.industry == industry)
            if booth.industry == industry:
                print("Adding booth")
                check = 0
                while not groups[i].add(booth):
                    check+=1
                    if check>=len(groups):
                        print("Not added")
                        break
                    i = (i+1) % len(groups)
                i = (i+1) % len(groups)