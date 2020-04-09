import math
import copy
#initialise the data of the booths
class Booth:
    def __init__(self,length,width,name,category,drone):
        self.length=length
        self.width=width
        self.area=length*width
        self.name=name
        self.category=category
        self.drone=drone
        self.position="null"
        self.assigned=False
		self.id=int(name[-1])
    
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
booth1=Booth(8,5,'booth1',"banking",'No')
booth2=Booth(8,5,'booth2',"sports","No")
booth3=Booth(8,5,'booth3',"medical","No")
booth4=Booth(8,5,'booth4',"electrical","Yes")
booth5=Booth(2,2,'booth5',"medical","No")
booth_list.append(booth1)
booth_list.append(booth2)
booth_list.append(booth3)
booth_list.append(booth4)
booth_list.append(booth5)

#create a list that contains all the empty spaces(5 by 10, each single number stands for a 1 by 1 space) 
space_list1=[]
space_list2=[]
space_list3=[]
space_list4=[]
for i in range(0,50):
    space_list1.append([])
    space_list2.append([])
    space_list3.append([])
    space_list4.append([])
total_space=[space_list1,space_list2,space_list3,space_list4]
for h in range(0,len(total_space)):
    k=1
    for i in range(0,len(total_space[h])):
        for j in range(0,100):
            total_space[h][i].append(k)
            k=k+1


def find_position(booth_list,space_list):
    row_num=len(space_list)
    col_num=len(space_list[0])
    result={}
    coodinates={}
    categories={}
    space_left=[]
    for l in range(1,row_num*col_num+1):
        space_left.append(l)
    backup_space_left=space_left    #create a back up for restoration
    for m in range(0,len(booth_list)):  #for every Booth in the booth_list
        while(True):
            if(booth_list[m].assigned==False):
                widt=booth_list[m].width*10        #get its length and width
                leng=booth_list[m].length*10  
                n=min(space_left)   #the starting point, always start from the smallest
                x=1
                while(x==1):    
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
                    if len(checking_list)==booth_list[m].area*100:   #if all spaces are available, set the position to the booth, remove the space taken from space_left
                        booth_list[m].set_position(n)
                        space_left=copy.deepcopy(backup_space_left)
                        for t in checking_list:
                            space_left[t-1]=10000
                        booth_list[m].assigned=True
                        result[booth_list[m].name]=booth_list[m].position
                        categories[booth_list[m].name]=booth_list[m].category
                        backup_space_left=copy.deepcopy(space_left)
                        x=0

                    else:
                        space_left[space_left.index(n)]=10000   #mark that starting from this space cannot fit for the booth 
                        if min(space_left)==10000:  #if all space are not available, break the process
                            x=0
                        else:       #else start checking for the next space available
                            n=min(space_left)
                space_left=copy.deepcopy(backup_space_left)    #restore all the positions set to 10000 for checking
            break
           
    industry=list(categories.values())	#check whether there are booths with same category in the same area
    key=list(result.keys())
    for a in range(0,len(industry)):
        for b in range(0,a):
            if(industry[a]==industry[b]):
                x=key[a]
                y=int(x[-1])
                result.pop(x)
                booth_list[y-1].assigned=False
    
    positions=list(result.values())    #remove booth with position 'null' for better viewing
    key=list(result.keys())
    for n in range(0,len(positions)):
        if(positions[n]=="null"):
            result.pop(key[n])
    for i in range(0,len(result)):
        point=positions[i]
        x=point%col_num
        y=math.ceil(point/col_num)
        coodinate=[x,y]
        coodinates[key[i]]=coodinate
    return result,coodinates




piano_area=[]
for i in range(0,len(booth_list)):
    if(booth_list[i].drone=="Yes"):
        piano_area.append(booth_list[i].name)
        booth_list[i].assigned=True

for j in range(0,len(total_space)):
    print(find_position(booth_list,total_space[j]))
print(piano_area)


    




        
            

    
    
    


    
