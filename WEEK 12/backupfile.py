import os





print(os.getcwd())
print(os.listdir(os.getcwd()))


# os.makedirs(os.getcwd() + "/new folder", exist_ok=True)
# os.makedirs(os.path.join(os.getcwd(), "new folder 2"), exist_ok=True)


print(os.path.abspath(__file__))


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)


for root, dirs, files in os.walk(BASE_PATH):
    for filename in files:
        print(filename)

















import csv
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# CSV is in the SAME folder as this file
CSV_FOLDER = BASE_PATH

CSV_PATH = os.path.join(CSV_FOLDER, "MY FIRSTCSV.csv")

print(CSV_PATH)

csv_data = []

with open(CSV_PATH, mode="r", newline="") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_data.append(row)

print("--------------------------------------------------")
print(csv_data)

# FIX: only index that exists
print(csv_data[0])



csv_new_data = []
for row in csv_data:
    csv_new_data.append([row[1], row [5]])


with open (os.path.join(CSV_FOLDER, "WRITE_CSV.csv"), mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_new_data)
















import os
import csv
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
WEEK12_FOLDER = os.path.join(BASE_PATH, "WEEK12")
SERVICE_KEY = os.path.join(WEEK12_FOLDER, "cmpe-bse-ece-1-4-3a712a3d06b7.json")

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(credentials)

share_url = "https://docs.google.com/spreadsheets/d/1zV44TOErP1s2DxB2kffvKGNdZx8r1azebSmcuDEYonQ/edit?usp=sharing"

gs_instance = client.open(sheet_url)
sheet_instance = gs_instance.woksheet(0)


googlesheet_data_tab0 = sheet_instance.get_all_records()
print(googlesheet_data_tab0)














import os
import csv
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
WEEK12_FOLDER = os.path.join(BASE_PATH, "WEEK12")
SERVICE_KEY = os.path.join(WEEK12_FOLDER, "cmpe-bse-ece-1-4-3a712a3d06b7.json")

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(credentials)

share_url = "https://docs.google.com/spreadsheets/d/1zV44TOErP1s2DxB2kffvKGNdZx8r1azebSmcuDEYonQ/edit?usp=sharing"

gs_instance = client.open(sheet_url)
sheet_instance = gs_instance.woksheet(0)


googlesheet_data_tab0 = sheet_instance.get_all_records()
print(googlesheet_data_tab0)















