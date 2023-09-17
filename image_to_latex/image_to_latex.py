import requests
import json
<<<<<<< HEAD

# This code makes an API request to Mathpix, which can generate LaTeX from handwritten images.
=======
from PIL import Image
from io import BytesIO
import io

#This code makes an API request to Mathpix, which can generate LaTeX from handwritten images.
>>>>>>> 9125d73 (tys first commit)
url = 'https://api.mathpix.com/v3/text'
headers = {
    "app_key": "692e9c0662a2d7f5d7ba246d6e9833d5536d63defb1305b3af2e80ff8ce5a894"
}

<<<<<<< HEAD

options = {
    'formats': ['text', 'data', 'html']
}

def image_to_latex(img: str) -> str:
    print(img)
    with open(img, "rb") as img_file:
        files = {'file': img_file}
        data = {'options_json': json.dumps(options)}
        response = requests.post(url, headers=headers, files=files, data=data)

    # print(response)
=======
# Options for OCR
options = {
    'formats': ['text', 'data', 'html']
}
    
def image_to_latex(img) -> str:
    img_buffer = BytesIO()
    img = img.convert('RGB')
    img.save(img_buffer, format='JPEG')  # Change the format as needed
    img_buffer.seek(0)
    img_buffer_binary = io.BufferedReader(img_buffer)

    files = {'file': img_buffer_binary}
    print(img_buffer)
    data = {'options_json': json.dumps(options)}
    response = requests.post(url, headers=headers, files=files, data=data)

>>>>>>> 9125d73 (tys first commit)
    # Process the response
    if response.status_code == 200:
        result = json.loads(response.text)
        with open("latex.json", "w+") as f:
            json.dump(result.get('text'), f)
<<<<<<< HEAD
=======
            print("resulting text",result.get('text'))
>>>>>>> 9125d73 (tys first commit)
        return result.get('text')
        # Further processing
    else:
        return f"Request failed with status code {response.status_code}"
<<<<<<< HEAD
=======

if __name__ == "__main__":
    img = Image.open("Image.jpg")
    print(image_to_latex(img))
>>>>>>> 9125d73 (tys first commit)
