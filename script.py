import requests

while True:
    url = input("Enter the URL: ")
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        print("Site source code: ",text)
    else:
        print("An error occured.")