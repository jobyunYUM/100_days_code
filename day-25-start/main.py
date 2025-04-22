# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon" , "Black"],
    "Count" : [grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list= data["temp"].to_list()
# print(temp_list)
#
# # Average in a series
# # temp_sum = sum(temp_list)
# # temp_avg = temp_sum/len(temp_list)
# # print(temp_avg)
# print(data["temp"].mean())
#
# # max in a series
# print(data["temp"].max())
#
# # Get data in columns
# # This is the same two methods: one is object (second) one is calling it like a data point
# # print(data["condition"])
# print(data.condition)

# # Get data in a row
# print(data[data.day == "Monday"])
# # row with hottest day
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy","James","Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")