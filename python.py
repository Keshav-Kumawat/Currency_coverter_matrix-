
import os 
import requests  
    

def download_image():
    folder_name = "files"

    os.makedirs(folder_name,exist_ok=True)
    url = 'https://img.freepik.com/free-vector/digital-futuristic-earth-technology-background-with-glowing-lights_1017-23327.jpg?semt=ais_hybrid&w=740&q=80'
    try:
        response = requests.get(url)  
        response.raise_for_status()
        file_path = os.path.join(folder_name,"image.jpg")
        
        with open (file_path,"wb") as f:
            f.write(response.content) 
            print("image download successfully")
    except requests.exceptions.RequestException as e:
        print(f"unexpected Error occured :{e}")        

download_image()