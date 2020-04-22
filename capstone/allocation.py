from capstone.models import Booth
import math
from decimal import Decimal
from copy import deepcopy


class Group:
    def __init__(self,shape,start=(0,0),end=(0,0),radius=0,centre=(0,0),start_angle= 0,end_angle=0,downward_sloping = False,max_height=3):
        self.start = start
        self.end = end
        self.radius = radius
        self.centre = centre
        self.shape = shape
        self.start_angle=start_angle
        self.end_angle =end_angle
        self.downward_sloping = downward_sloping
        self.max_height= max_height
        if shape == 'horizontal' or shape =='vertical':
            self.point = list(start)
        elif shape=='slanted':
            self.point = list(start)
            if downward_sloping:
                self.angle = math.degrees(math.atan((start[1]-end[1])/(start[0]-end[0])))
            else:
                self.angle= math.degrees(math.atan((end[1]-start[1])/(end[0]-start[0])))


    def add(self, booth):
        if self.shape == "horizontal":
            if(self.point[0]+booth.width_pixel <=self.end[0]) and booth.length <= self.max_height:
                booth.position_x = self.point[0] 
                booth.position_y = self.point[1]-booth.length_pixel
                self.point[0] = self.point[0] + booth.width_pixel
                booth.rotation=0
                print("horizontal",booth.project_id,booth.position_x,booth.position_y)
                booth.save()
                return True
            else:       
                return False

        elif self.shape == "vertical":
            print("Trying to fit project id "+booth.project_id+" into vertical")
            print(self.point[1]+booth.length_pixel <=self.end[1])
            if(self.point[1]+booth.length_pixel <=self.end[1] and booth.width <= self.max_height):
                booth.rotation = 0
                booth.position_x = self.point[0]
                booth.position_y = self.point[1]
                self.point[1] = self.point[1] + booth.length_pixel
                print("vertical",booth.project_id,booth.position_x,booth.position_y)
                booth.save()
                return True
            else:
                return False
                
        elif self.shape == "slanted":
            theta = 90 - self.angle
            x =booth.length_pixel*Decimal(math.sin(theta))
            if (self.downward_sloping == True):
                if(self.point[0]+x<=self.end[0] and booth.length <= self.max_height):
                    booth.position_x = self.point[0] + booth.length_pixel*Decimal(math.sin(math.radians(theta)))   
                    booth.position_y = self.point[1] - booth.length_pixel*Decimal(math.cos(math.radians(theta)))
                    booth.rotation = self.angle
                    self.point[0] = self.point[0] + booth.width_pixel*Decimal(math.sin(math.radians(theta)))
                    self.point[1] = self.point[1] + booth.width_pixel*Decimal(math.cos(math.radians(theta)))
                    print("slanted",booth.project_id,booth.position_x,booth.position_y)
                    booth.save()
                    return True
                else:
                    return False
            else:
                if(self.point[0]+x<=self.end[0] and booth.length <= self.max_height):
                    booth.position_x = self.point[0] - booth.length_pixel*Decimal(math.sin(math.radians(theta)))   
                    booth.position_y = self.point[1] + booth.length_pixel*Decimal(math.cos(math.radians(theta)))
                    booth.rotation = self.angle
                    self.point[0] = self.point[0] + booth.width_pixel*Decimal(math.sin(math.radians(theta)))
                    self.point[1] = self.point[1] + booth.width_pixel*Decimal(math.cos(math.radians(theta)))
                    print("slanted",booth.project_id,booth.position_x,booth.position_y)
                    booth.save()
                    return True
                else:
                    return False

def allocate(booths):
    #defining the spaces
    space_1 = Group(shape="vertical",start = (85,120),end = (85,255),max_height=3)
    space_2 = Group(shape="horizontal",start = (130,100),end = (275,100),max_height=4)
    space_3 = Group(shape="vertical",start = (280,120),end = (280,255),max_height=3)
    space_4 = Group(shape="slanted",downward_sloping = True,start = (140,300),end = (315,450),max_height=6)
    space_5 = Group(shape="horizontal",start = (350,160),end = (560,160),max_height=6)
    space_6 = Group(shape="horizontal",start = (350,300),end = (560,300),max_height=6)
    space_7 = Group(shape="vertical",start = (590,125),end = (590,245),max_height=3)
    space_8 = Group(shape="slanted",downward_sloping = False,start = (680,90),end = (780,60),max_height=2)
    space_9 = Group(shape="slanted",downward_sloping = False,start = (540,500),end = (772,280),max_height=6)
    space_10 = Group(shape="vertical",start = (804,110),end = (804,239),max_height=3)
    space_11 = Group(shape="slanted",downward_sloping = True,start = (115,920),end = (380,1145),max_height=6)
    space_12 = Group(shape="slanted",downward_sloping = False,start = (500,1180),end = (720,960),max_height=6)
    groups = [space_1,space_2,space_3,space_4,space_5,space_6,space_7,space_8,space_9,space_10,space_11,space_12]


    #finding out how many industries are there
    industries = []
    for booth in booths:
        if booth.industry not in industries:
            industries.append(booth.industry)

    #sort booths by industry into booths_byindustry where each element is a list of booths in the same industry
    #booths are also sorted by size for easy allocation
    booths_byindustry =[]
    booth_count = []
    booths = sorted(booths, key=lambda t: t.width)
    for industry in industries:
        booth_temp =[]
        for booth in booths:
            if(booth.industry == industry):
                booth.position_x =-1
                booth.position_y =-1
                booth.save()
                booth_temp.append(booth)
                print(industry,booth.project_id)
        booth_count.append(len(booth_temp)-1)
        booths_byindustry.append(booth_temp)

    print("Start allocating")
    industry_count = 0
    overall_booth_count = 0
    group_count =0
    group_full = 0
    while (overall_booth_count < len(booths)):
        if(booth_count[industry_count]>=0):
            
            booth = booths_byindustry[industry_count][booth_count[industry_count]]
            
            
            #adds booth to a group, if group is full/booth cannot fit, move on to the next one
            group_full = 0
            overall_booth_count+=1
            while not groups[group_count].add(booth):
                group_full +=1
                group_count = (group_count+1)%len(groups)
                if group_full>=len(groups):
                    #if all groups are full, booth cannot fit, move on to the next booth
                    if(overall_booth_count<len(booths)):
                        break
                    #if all booths are done, finish the allocation
                    else:
                        return

            #decrease the booth_count
            booth_count[industry_count]=booth_count[industry_count]-1

        #increment the industry
        industry_count=(industry_count + 1)%len(industries)

        # check = 0
        # while(booth_count>= len(booths_byindustry[industry_count])):
        #     print(booth.project_id,booth_count,industry_count,len(booths_byindustry[industry_count]))
        #     check +=1
        #     print(industry_count)
        #     industry_count =(industry_count+1) % len(industries)
        #     print(industry_count)
        #     if check>= len(industries):
        #         return
            
                
            


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