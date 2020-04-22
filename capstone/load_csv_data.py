import csv
import pandas as pd
from capstone.models import Booth, Map

def load_csv_data(file_name,display_name,request):
    
    read_file = pd.read_excel ("./" + file_name)
    read_file.to_csv ("./data.csv", index = None, header=True)

    #creating new map for user
    map = Map()
    map.name= display_name
    map.user= request.user
    map.save()

    #setting curr_map to this map
    user_maps = Map.objects.filter(user=request.user)    
    curr_map = user_maps[0]
    booths = curr_map.booths
    for booth in booths.all():
        booth.delete()
    curr_map.curr_map_ref = map.id
    curr_map.save()

    with open("./data.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            print("Data loaded successfully")
            for row in reader:
                booth = Booth()
                booth.project_id = row['Project ID']
                booth.project_name = row['Project Name']
                booth.length = row['Length'] 
                booth.width = row['Width']
                booth.length_pixel = float(booth.length)*13.397
                booth.width_pixel = float(booth.width)*13.397
                booth.area = float(booth.length)*float(booth.width)
                if(row['Project ID']=='Yes'):
                    booth.in_campus_centre = True
                else:
                    booth.in_campus_centre = False
                booth.industry = row["Industry"]
                booth.saved_map = map
                booth.save()
                curr_map_booth = booth
                curr_map_booth.pk = None
                curr_map_booth.saved_map = curr_map
                curr_map_booth.save()
                
    return map
            
