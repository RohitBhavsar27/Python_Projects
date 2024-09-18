import os
import shutil
import datetime
import schedule
import time

source_dir = "C:\\Users\\bhavs\\OneDrive\\Videos\\Captures"
destination_dir = "D:\\VS CODE\\21 Python Projects\\Automated_File_Bcakup_20\\Backup"

def copy_folder_to_directory(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))
    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder alredy exists in: {dest}")

#inline anonymous function using lambda        
schedule.every().day.at("15:20").do(lambda: copy_folder_to_directory(source_dir,destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)