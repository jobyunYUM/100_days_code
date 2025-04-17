from http.client import responses

import requests
import datetime as dt

USERNAME = "jobyun"
TOKEN = "askjwkw2123da4gsde3"
COLOR =  "ajisai"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPHID = "beegbooger1"
DATE = dt.date.today().strftime("%Y%m%d")
INPUT_HRS = str(input("How many hours did you exercise today?: "))


user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# push = requests.post(url = pixela_endpoint, json=user_params)
# print(push.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPHID,
    "name" : "Gym Graph",
    "unit" : "Hours",
    "type" : "float",
    "color" : COLOR,
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# graph_response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(graph_response)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
post_pixel_config = {
    "date" : DATE,
    "quantity" : INPUT_HRS,
}

# post_pixel_response = requests.post(url = post_pixel_endpoint, json = post_pixel_config, headers = headers)


for day in range(1,24):
    DATE = dt.datetime(2025,2,day).strftime("%Y%m%d")
    INPUT_HRS = "10"
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}"
    new_pixel_config = {
    "quantity" : INPUT_HRS,
    }
    update_response = requests.put(url = update_endpoint,json=new_pixel_config,headers=headers)
    print(update_response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}"

# delete_response = requests.delete(url=delete_endpoint, headers=headers)
