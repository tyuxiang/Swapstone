from capstone.models import Booth
import math
from decimal import Decimal
from copy import deepcopy


class Group:
    def __init__(self,shape,start=(0,0),end=(0,0),radius=0,centre=(0,0),start_angle= 0,end_angle=0,downward_sloping = False):
        self.start = start
        self.end = end
        self.radius = radius
        self.centre = centre
        self.shape = shape
        self.start_angle=start_angle
        self.end_angle =end_angle
        if shape == 'horizontal' or shape =='vertical':
            self.point = list(start)
        elif shape=='slanted':
            self.point = list(start)
            if downward_sloping:
                self.angle = math.degrees(math.atan((start[1]-end[1])/(start[0]-end[0])))
            else:
                self.angle= math.degrees(math.atan((end[1]-start[1])/(end[0]-start[0])))
        # elif shape =='circle':
        #     self.point_angle = self.start_angle
        #     self.point =[0,0]
        #     if start_angle>=0 and start_angle<=90:
        #         self.point[0] = self.centre[0] - self.radius*math.cos(self.start_angle)
        #         self.point[1] = self.centre[1] - self.radius*math.sin(self.start_angle)
        #     elif start_angle>90 and start_angle<=180:
        #         self.point[0] = self.centre[0] + self.radius*math.cos(180-self.start_angle)
        #         self.point[1] = self.centre[1] - self.radius*math.sin(180-self.start_angle)
        #     elif start_angle>180 and start_angle<=270:
        #         self.point[0] = self.centre[0] + self.radius*math.cos(self.start_angle)
        #         self.point[1] = self.centre[1] + self.radius*math.sin(self.start_angle)
        #     elif start_angle>270 and start_angle<=360:
        #         self.point[0] = self.centre[0] + self.radius*math.cos(self.start_angle)
        #         self.point[1] = self.centre[1] + self.radius*math.sin(self.start_angle)


    def add(self, booth):
        if self.shape == "horizontal":
            # do we need to check for width?
            if(self.point[0]+booth.length_pixel <=self.end[0]):
                booth.position_x = self.point[0]
                print(self.point[0])
                booth.position_y = self.point[1] + booth.width_pixel
                self.point[0] = self.point[0] + booth.length_pixel
                booth.rotation=0
                booth.save()
                return True
            else:
                return False
        elif self.shape == "vertical":
            if(self.point[1]+booth.length_pixel <=self.end[1]):
                booth.rotation = 0
                booth.position_x = self.point[0]
                booth.position_y = self.point[1] + booth.width_pixel
                self.point[1] = self.point[1] + booth.length_pixel
                booth.save()
                return True
            else:
                return False
        elif self.shape == "slanted":
            theta = 90 - self.angle
            x =booth.length_pixel*Decimal(math.sin(theta))
            if(self.point[0]+x<=self.end[0]):

                booth.project_name = "slanted"
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
        #     theta =2*math.asin((booth.length_pixel/self.radius)/2)
        #     if(self.point_angle +theta <= self.end_angle):
        #         booth.position_x = self.point[0]
        #         booth.position_y = self.point[1]
        #         self.point[0] = self.point[0] + booth.length_pixel*Decimal(math.cos((180-theta)/2))
        #         self.point[1] = self.point[1] + booth.length_pixel*Decimal(math.sin((180-theta)/2))
        #         booth.angle = 0
        #         booth.save()
        #         return True
        #     else:
        #         return False





def allocate(booths):
    groups = [Group(shape="horizontal",start = (270,240),end = (500,240)),
    Group(shape="horizontal",start = (255,340),end = (540,340)),
    Group(shape = "horizontal",start =(15,150),end =(175,150)),
    Group(shape = "vertical",start =(175,150),end =(175,320)),
    Group(shape = "horizontal",start =(15,320),end =(175,320)),
    Group(shape="slanted",start=(80,380),end= (230,510),downward_sloping = True),
    Group(shape="slanted",start = (500,515),end=(640,360),downward_sloping =False)]

  
    industries = [str(1),str(2)]

    print("Starting allocation algorithm")
    #booths = deepcopy(final_booths)
    #booths.objects.order_by('-area','industry')
    booths_byindustry =[]
    for industry in industries:
        booth_temp =[]
        for booth in booths:
            if(booth.industry == industry):
                booth_temp.append(booth)
        booths_byindustry.append(booth_temp)

    industry_count = 0
    booth_count = 0
    overall_booth_count = 0
    group_count =0
    group_full = 0
    while (overall_booth_count < len(booths)):
        overall_booth_count+=1
        booth = booths_byindustry[industry_count][booth_count]
        group_full = 0
        while not groups[group_count].add(booth):
            group_full +=1
            if group_full>=len(groups):
                return
        group_count = (group_count+1)%len(groups)
        industry_count +=1
        if industry_count >= len(industries):
            booth_count +=1
            check = 0
            industry_count = industry_count % len(industries)
        while(booth_count>= len(booths_byindustry[industry_count])):
            check +=1
            industry_count+=1
            industry_count =industry_count % len(industries)
            if check>= len(industries):
                return
            
            
                
            


    # for booths_industry in booths_byindustry:
    #     for booth in booths_industry:
    #         if booth.industry == industry:
    #             check = 0
    #             while not groups[i].add(booth):
    #                 check+=1
    #                 if check>=len(groups):
    #                     break
    #                 i = (i+1) % len(groups)
    #             i = (i+1) % len(groups)