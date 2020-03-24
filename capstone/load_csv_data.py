import csv
import pandas as pd
from capstone.models import Booth

def load_csv_data(file_name):
    read_file = pd.read_excel ("./"+file_name)
    read_file.to_csv ("./data.csv", index = None, header=True)
    Booth.objects.all().delete()
    with open("./data.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            print("Data loaded successfully")
            for row in reader:
                booth = Booth()
                booth.project_id = row['Project ID']
                booth.project_name = row['Project Name']
                booth.length = row['Length'] 
                booth.width = row['Width']
                booth.length_pixel = float(booth.length)/0.07
                booth.width_pixel = float(booth.width)/0.07
                booth.area = float(booth.length)*float(booth.width)
                if(row['Project ID']=='Yes'):
                    booth.in_campus_centre = True
                else:
                    booth.in_campus_centre = False
                booth.industry = row["Industry"]
                booth.save()
            
