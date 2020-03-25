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
                # print(self.point[0])
                booth.position_y = self.point[1] - booth.width_pixel
                self.point[0] = self.point[0] + booth.length_pixel
                booth.rotation=0
                print("horizontal",booth.project_id,booth.position_x,booth.position_y)
                booth.save()
                return True
            else:
                return False
        elif self.shape == "vertical":
            if(self.point[1]+booth.length_pixel <=self.end[1]):
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
            if(self.point[0]+x<=self.end[0]):

                booth.project_name = "slanted"
                booth.position_x = self.point[0] + booth.width_pixel*Decimal(math.sin(math.radians(theta)))   
                booth.position_y = self.point[1] - booth.width_pixel*Decimal(math.cos(math.radians(theta)))
                booth.rotation = self.angle
                self.point[0] = self.point[0] + booth.length_pixel*Decimal(math.sin(math.radians(theta)))
                self.point[1] = self.point[1] + booth.length_pixel*Decimal(math.cos(math.radians(theta)))
                print("slanted",booth.project_id,booth.position_x,booth.position_y)
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
    space_1 = Group(shape="vertical",start = (85,120),end = (85,255))
    space_2 = Group(shape="horizontal",start = (130,100),end = (275,100))
    space_3 = Group(shape="vertical",start = (280,120),end = (280,255))
    space_4 = Group(shape="slanted",downward_sloping = True,start = (140,320),end = (315,450))
    space_5 = Group(shape="horizontal",start = (330,145),end = (580,145))
    space_6 = Group(shape="horizontal",start = (330,280),end = (580,280))
    space_7 = Group(shape="vertical",start = (590,125),end = (590,245))
    #space_8 = Group(shape="horizontal",start = (330,280),end = (580,280))
    space_9 = Group(shape="slanted",downward_sloping = False,start = (570,440),end = (740,300))
    groups = [space_1,space_2,space_3,space_4,space_5,space_6,space_7,space_9]

  
    industries = [str(i) for i in range(1,5)]

    # print("Starting allocation algorithm")
    #booths = deepcopy(final_booths)
    #booths.objects.order_by('-area','industry')
    booths_byindustry =[]
    booth_count = []
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

    industry_count = 0
    overall_booth_count = 0
    group_count =0
    group_full = 0
    while (overall_booth_count < len(booths)):
        if(booth_count[industry_count]>=0):
            
            booth = booths_byindustry[industry_count][booth_count[industry_count]]
            
            
            #adds booth to a group, if group is full, move on to the next one
            #if all groups are full, return
            group_full = 0
            overall_booth_count+=1
            while not groups[group_count].add(booth):
                group_full +=1
                group_count = (group_count+1)%len(groups)
                if group_full>=len(groups):
                    return  

            #decrease the booth
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