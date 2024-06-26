# from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# import pyautogui
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Welcome to the API!"
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})

#     UPLOAD_FOLDER = 'C:\\Users\\arsla\\OneDrive\\Documents'

# # Set the upload folder
#     app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Construct the absolute file path
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)    



#     # file_path = '/path/to/save/' + file.filename
#     file.save(file_path)
    
#     driver = webdriver.Chrome()

    

#     # driver.set_window_size(375,667)
#     driver.maximize_window()

#     driver.get('https://upscales.ai/')
    
#     upload_file = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]')
#     upload_file.click()
#     time.sleep(3)
#     pyautogui.typewrite(file_path)
#     pyautogui.press('enter')
    
#     time.sleep(3)
#     src = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[4]/div[1]/div/div[1]/div/div/img-comparison-slider/img[2]").get_attribute("src")
#     base64_string = src.split(',')[1]
    
#     driver.quit()
    
#     return jsonify({'base64_string': base64_string})

# if __name__ == '__main__':
#     app.run(debug=True)


import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# import pyautogui
import os



# Set the DISPLAY environment variable to a dummy value
os.environ['DISPLAY'] = ':0.0'

# Now import pyautogui
import pyautogui

# Rest of your code...


def main():
    st.title("Image Upload")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Initialize Chrome webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        
        driver.maximize_window()
        driver.get('https://upscales.ai/')
        
        # Perform actions
        upload_file = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]')
        upload_file.click()
        time.sleep(3)
        pyautogui.typewrite(file_path)
        pyautogui.press('enter')
        time.sleep(3)
        src = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[4]/div[1]/div/div[1]/div/div/img-comparison-slider/img[2]").get_attribute("src")
        base64_string = src.split(',')[1]
        
        # Display result
        st.image(base64_string)

        # Quit driver
        driver.quit()

if __name__ == "__main__":
    main()
