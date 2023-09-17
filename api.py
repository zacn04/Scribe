import requests
import json

url = 'https://api.mathpix.com/v3/text'
headers = {
    "app_key": "692e9c0662a2d7f5d7ba246d6e9833d5536d63defb1305b3af2e80ff8ce5a894"
}

# Options for OCR
options = {
    'formats': ['text', 'data', 'html']
}



with open("Image.jpg", "rb") as img_file:
    files = {'file': img_file}
    data = {'options_json': json.dumps(options)}
    response = requests.post(url, headers=headers, files=files, data=data)


# Process the response
if response.status_code == 200:
    result = json.loads(response.text)
    print("Text: ", result.get('text'))
    # Further processing
else:
    print(f"Request failed with status code {response.status_code}")
