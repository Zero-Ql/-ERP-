import csv
import time


class csv_data:

    @classmethod
    def get_data1(cls, path):
        data = []
        with open(path, encoding="utf-8-sig", errors='ignore') as file:
            csv_read = csv.reader(file)
            next(csv_read)
            for row in csv_read:
                data.append({"key": row[0], "value": row[1]})
        return data

    @classmethod
    def get_data2(cls, path):
        data = []
        with open(path, encoding="utf-8-sig", errors='ignore') as file:
            csv_read = csv.reader(file)
            next(csv_read)
            for row in csv_read:
                data.append({"vendor": row[0], "barcodes": row[1], "quantity": row[2], "price": row[3]})
        return data
