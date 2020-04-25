import requests
import csv
import pdb


def write_to_csv(data_dict):

    # name of csv file
    filename = "test.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        for row in data_dict:
            # pdb.set_trace()
            cols = list()
            for value in row.values():
                cols.append(value)
            csvwriter.writerow(cols)


        # query = "https://aqs.epa.gov/data/api/list/sitesByCounty?email=test@aqs.api&key=test&state=37&county=183"
county = '183'  # 183
state = '37'  # 37
email = 'test@aqs.api'
key = 'test'
param = '88101'
begin_date = '20200101'
end_date = '20200102'
# query = "https://aqs.epa.gov/data/api/sampleData/byCounty?email=test@aqs.api&key=test&param=88101&bdate=20160101&edate=20160228&state=37&county=183"
query = 'https://aqs.epa.gov/data/api/sampleData/byCounty?' + \
    "email=" + email + \
    "&key=" + key + \
    "&param=" + param + \
    "&bdate=" + begin_date + \
    "&edate=" + end_date + \
    "&state=" + state + \
    "&county=" + county

response = requests.get(query).json()

response_header = response['Header']
print(response_header)

response_payload = response['Data']

print(response_header)
# print(response_payload)
write_to_csv(response_payload)
