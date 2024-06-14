from pprint import pprint
import requests

payload = {
    "pageSize": 9000,
    # "currentPageNumber": 0,
    "dateFrom": "2023-05-09T21:00:00.000Z",
    "dateTo": "2024-06-10T20:59:59.999Z",
    "searchFilters": {
        "nameMis": ["1.2.643.2.69.1.2.7"],
        # "medDocumentType": ["198"]
    }
}
response = requests.post(
    url='http://10.128.66.207/fedstats/api/RemdUploadingStatus',
    json=payload
)
data = response.json()
d = {}
for i, record in enumerate(data):
    if record.get("nameMo") not in d:
        d[record.get("nameMo")] = record.get("organization")
    # print(f'{record.get("nameMo")}: {record.get("organization")}')

for i, el in enumerate(d):
    print(f'{i}: {el}: "organization": "{d[el]}",')

# 1.2.643.2.69.1.2.7 nameMis