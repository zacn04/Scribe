import requests
import json

# def get_app_id (full_answer = False):
#     return ("QQ9932-L6V5AVHXPV") # quick maths


def request_query_response (query):

    base_url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": query,
        "format": "plaintext",
        "output": "JSON",
        "appid": "QQ9932-L6V5AVHXPV",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        result = response.json()
        # Process the Wolfram Alpha response here
        return(result)

    else:
        print("ERROR")
        return(f"Error: {response.status_code} - {response.text}")

def parse_and_find_result(result):
    for pod in result["queryresult"]["pods"]:
        if pod["title"] == "Result":
            return pod["subpods"][0]["plaintext"]
        if pod["title"] == "Definite integral":
            return pod["subpods"][0]["plaintext"]
        if pod["title"] == "Indefinite integral":
            return pod["subpods"][0]["plaintext"]
        if pod["title"] == "Sum":
            return pod["subpods"][0]["plaintext"]
        if pod["title"] == "Exact result":
            return pod["subpods"][0]["plaintext"]
        
        
    assert False, "Result not found"

def clean_result(result):
    if "= " in result:
        index = result.find("= ")
        return result[index+2:]
    return result

def parse(result):
    answer = parse_and_find_result(result)
    clean_answer = clean_result(answer)
    return clean_answer

if __name__ == "__main__":
    # query = "let i = 10. sum of x from x = 0 to x = i?"
    # query = "3 + 3 ="
    query = "3 + 3 ="
    result = parse(request_query_response(query))
    print(result)
    # with open("sample.json", "w") as outfile:
    #     outfile.write(json.dumps(result["queryresult"]["pods"], indent=4))

    
    # print(result)

# with open("sample.json", "w") as outfile:
#     outfile.write(json.dumps(result["queryresult"]["pods"], indent=4))
