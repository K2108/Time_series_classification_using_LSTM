# Input data file consist of 5 relevant columns
# Column 2 : PupilLeft
# Column 3 : PupilRight
# Column 4 : LoadLevel
# Column 5 : Time_in_sec
# Column 6 : Diff_in_time
import pandas as pd
folder_name = "E:\Kyanite\Data Analysis\Timeseries_Dataset_Considering_Response_Status\timeseries"
for i in range(1,12):
  filename = folder_name + str(i) +".csv"   #get the name of the .csv file
  try:
    df = pd.read_csv(filename, header=None)
    print(filename)
  except:
    print("Kritika")
  print("It still works")