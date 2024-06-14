import datetime
import unittest
from pprint import pprint
from typing import List
from unittest import TestCase

import requests
from datetime import datetime as dt, timedelta


class RemdHTTPPostClient:

    def __init__(self,  medDocumentType: List[str], currentStatus: List[str] = None, pagesize=100, dateFrom=None, dateTo=None):
        self.pagesize = pagesize

        self.dateFrom = self.date_format(dateFrom or (dt.now() - timedelta(days=365)))

        self.dateTo = self.date_format(dateTo or dt.now())

        self.searchFilters = {
            "nameMis": ["1.2.643.2.69.1.2.7"],  # Vista
            "medDocumentType": medDocumentType,
            "currentStatus": currentStatus if currentStatus else [],
        }

    def post(self):
        response = requests.post(
            url='http://10.128.66.207/fedstats/api/RemdUploadingStatus',
            json=self.payload
        )
        self.data = response.json()

        return self.data

    @property
    def payload(self):
        return self.__dict__

    @staticmethod
    def date_format(date: datetime.date):
        return date.isoformat()[:-3] + "Z"

    def get_events(self, events_num=10):
        # print(self.data)
        it = iter(self.data)
        while events_num:
            try:
                next_el = next(it)
                yield (next_el.get('idCaseMis'), next_el.get('organization'))
            except StopIteration:
                return
            events_num -= 1


cl = RemdHTTPPostClient(medDocumentType=['198'], currentStatus=['3', '4', '5'])
cl.post()

for i, el in enumerate(cl.get_events()):
    print(f'{i + 1}: {el}')


class TestSEMD(TestCase):

    def setUp(self, medDocumentType: List[str], currentStatus: List[str] = None, pagesize=100, dateFrom=None, dateTo=None) -> None:
        ...

