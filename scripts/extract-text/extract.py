import pytesseract
from flask import Flask, jsonify, request
import os
import datetime

from PIL import Image
app = Flask(__name__)



def extract_text(filePath: str)-> str:
    # Open the image file
    image = Image.open(filePath)

    # Perform OCR and extract text from the image
    return pytesseract.image_to_string(image).replace('\n', ' ')

def run_service_logic():
    folder_path = r"C:\Users\alche\Pictures\Screenshots" # Replace with the actual folder path
    # Get a list of files in the folder
    files = os.listdir(folder_path)
    # Sort the files based on their creation time
    sorted_files = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)), reverse=True)
    # Get the top 15 files
    top_files = sorted_files[:15]
    # Print the top 15 files
    response = {}
    for file_name in top_files:
        file_path = os.path.join(folder_path, file_name)
        # creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        # print(f"{file_name} (Created: {creation_time})")
        response[file_path] = extract_text(filePath=file_path)
    return response

@app.route('/', methods=['GET'])
def fetch_application_list():
    response_api = run_service_logic()

    return response_api, 200


@app.route('/api/health-status', methods=['GET'])
def health_check():
    return jsonify({"healthly": True, "service":"extract_text"}), 200

if __name__ == '__main__':
    
    app.run( port=4005)

