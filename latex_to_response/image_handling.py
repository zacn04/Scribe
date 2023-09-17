import requests
import json

def find_proper_image(json_result):
    pods = json_result["queryresult"]["pods"]
    for pod in pods:
        if "Visual representation of" in pod["title"]:
            return pod["subpods"][0]["img"]["src"]
        if "illustration" in pod["title"]:
            return pod["subpods"][0]["img"]["src"]
    return None

def save_image(query, filename):
    base_url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": query,
        "format": "image",
        "output": "JSON",
        "appid": "QQ9932-7PXA4JPRGK",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        result = response.json()

    else:
        print(f"Error: {response.status_code} - {response.text}")

    url = find_proper_image(result)
    if url is None:
        print("No valid url found")
        return 0
    
    response = requests.get(url)

    if response.status_code == 200:
        # The file content is stored in response.content
        with open(filename, "wb") as f:
            f.write(response.content)
        print("File downloaded successfully.")
        return 1
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
        return 0

# with open("sample.json", "w") as outfile:
#     outfile.write(json.dumps(result["queryresult"]["pods"], indent=4))