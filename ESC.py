import math
#initialise the data of the booths
class Booth:
    def __init__(self,length,width,name):
        self.length=length
        self.width=width
        self.area=length*width
        self.name=name
        self.position="null"
    
    def get_length(self):
        a=self.length
        return a
    
    def get_width(self):
        b=self.width
        return b
    
    def get_area(self):
        c=self.area
        return c
    
    def get_name(self):
        d=self.name
        return d
    
    def set_position(self,pos):
        self.position=pos
    
    def get_position(self):
        e=self.position
        return e

#creating a list to hold all the booths
booth_list=[]
booth1=Booth(2,2,'booth1')
booth2=Booth(3,4,'booth2')
booth3=Booth(4,5,'booth3')
booth4=Booth(20,20,'booth4')
booth_list.append(booth1)
booth_list.append(booth2)
booth_list.append(booth3)
booth_list.append(booth4)

#create a list that contains all the empty spaces(5 by 10, each single number stands for a 1 by 1 space) 
space_list=[[],[],[],[],[]]
k=1
for i in range(0,len(space_list)):
    for j in range(0,10):
        space_list[i].append(k)
        k=k+1

def find_position(booth_list,space_list):
    row_num=len(space_list)
    col_num=len(space_list[0])
    result={}
    space_left=[]
    for l in range(1,row_num*col_num+1):
        space_left.append(l)

    for m in range(0,len(booth_list)):  #for every Booth in the booth_list
        widt=booth_list[m].width        #get its length and width
        leng=booth_list[m].length   
        n=min(space_left)               #the starting point, always start from the smallest
        checking_list=[]
        for o in range(0,leng):         #check if all the required spaces are available
            p=n+o
            if(p in space_left and math.floor((p-1)/col_num)==math.floor((n-1)/col_num)):
                checking_list.append(p)
        for q in range(1,widt):
            r=n+q*col_num
            if(r in space_left):
                checking_list.append(r)
        if(len(checking_list)==leng+widt-1):    #if it fits in the space left
            for r in range(leng,leng+widt-1):
                for s in range(1,leng):
                    checking_list.append(checking_list[r]+s)
        if len(checking_list)==booth_list[m].area:   #if all spaces are available, set the position to the booth, remove the space taken from space_left
            booth_list[m].set_position(n)
            for t in checking_list:
                space_left[t-1]=10000
        result[booth_list[m].name]=booth_list[m].position
    return result

print(find_position(booth_list,space_list))
    




        
            

    
    
    


    
