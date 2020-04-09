from django.test import TestCase
import pandas as pd
from models import Booth, Map

def load_data_test(file_name):
    read_file = pd.read_excel ("./../" + file_name)
    read_file.to_csv ("./data.csv", index = None, header=True)
    
    #creating new map for user
    map = Map()
    map.name= file_name
    map.save()

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
    return map

class AllocationTest(TestCase):
    def test_empty(self):
        filename = "Empty.xlsx"
        map = load_data_test(filename)
        booth = map.booths.all()
        allocate(booth)
        self.assertTrue(map)
 


if __name__ == '__main__':
    unittest.main()

