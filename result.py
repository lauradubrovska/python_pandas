import pandas
get_info=input()  #input information from terminal

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()

Area=None

for line in info_list:
    Description=line[1]
    if Description==get_info:
        Area=line[0]
        break

result=[]
with open("data.csv","r") as m:
    next(m)
    for line in m:
        row=line.rstrip().split(",")
        geo_count=int(row[3])
        if Area==row[1]:
            result.append(int(row[3]))
        
print(sum(result))
