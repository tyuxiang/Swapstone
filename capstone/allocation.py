from capstone.models import Booth
import math
from decimal import Decimal
from copy import deepcopy


class Group:
    def __init__(self,shape,start=(0,0),end=(0,0),radius=0,centre=(0,0),downward_sloping = False):
        self.start = start
        self.end = end
        self.radius = radius
        self.centre = centre
        self.shape = shape
        if shape == 'square':
            self.point = list(start)
        elif shape=='line':
            self.point = list(start)
            if downward_sloping:
                self.angle = math.degrees(math.atan((start[1]-end[1])/(start[0]-end[0])))
            else:
                self.angle= math.degrees(math.atan((end[1]-start[1])/(end[0]-start[0])))


    def add(self, booth):
        if self.shape == "square":
            # do we need to check for width?
            if(self.point[0]+booth.length_pixel <=self.end[0]):
                booth.position_x = self.point[0]
                print(self.point[0])
                booth.position_y = self.point[1] + booth.width_pixel
                self.point[0] = self.point[0] + booth.length_pixel
                booth.save()
                return True
            else:
                return False
        elif self.shape == "line":
            theta = 90 - self.angle
            x =booth.length_pixel*Decimal(math.sin(theta))
            if(self.point[0]+x<=self.end[0]):
                if(self.start[0]==125):
                    booth.project_name = "Left"
                booth.position_x = self.point[0] + booth.width_pixel*Decimal(math.sin(math.radians(theta)))   
                booth.position_y = self.point[1] - booth.width_pixel*Decimal(math.cos(math.radians(theta)))
                booth.rotation = self.angle
                self.point[0] = self.point[0] + booth.length_pixel*Decimal(math.sin(math.radians(theta)))
                self.point[1] = self.point[1] + booth.length_pixel*Decimal(math.cos(math.radians(theta)))
                booth.save()
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





def allocate(booths):
    groups = [Group(shape="square",start = (270,240),end = (500,240)),
    Group(shape="square",start = (255,340),end = (540,340)),
    Group(shape="line",start=(80,380),end= (230,510),downward_sloping = True),
    Group(shape="line",start = (500,515),end=(640,360),downward_sloping =False)]
    # Group(centre = (82,247),start = (80,130),end = (80,337),radius = 110, shape = "circle"),
    # Group(centre= (80,250),start = (30,160),end = (100,340),radius = 110,shape = "circle")]
    industries = [str(1),str(2)]
    i = 0
    check = 0
    print("Starting allocation algorithm")
    #booths = deepcopy(final_booths)
    for industry in industries:
        for booth in booths:
            if booth.industry == industry:
                check = 0
                while not groups[i].add(booth):
                    check+=1
                    if check>=len(groups):
                        break
                    i = (i+1) % len(groups)
                i = (i+1) % len(groups)