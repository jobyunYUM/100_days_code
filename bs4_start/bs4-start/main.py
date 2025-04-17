from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents,"html.parser")
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# class_is_heading = soup.find_all(class_="heading")
#
# heading = soup.find(name="h1", id="name")
#
# section_heading = soup.find(name="h3", class_="heading")
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector ="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("")

BeautifulSoup(yc_web_page)
