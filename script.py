import requests

while True:
    url = input("Enter the URL: ")
    response = requests.get(url)
    if response.status_code == 200:
        try:
            text = response.json()
            print("Response: ",text)
        except:
            text = response.text
            print("Response: ",text)
    else:
        print("An error occured.")
