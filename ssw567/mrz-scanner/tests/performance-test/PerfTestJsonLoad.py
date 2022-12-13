import time
import json
from decimal import Decimal
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'mrz-scanner'))
from service import MRTD as m

timerList = []
def main():
    scanValueList = readEncodedJson()
    dbValueList = readDecodedJson()
    calcTimeForK(100, scanValueList, dbValueList)
    for k in range(1000, 10001, 1000):
        calcTimeForK(k, scanValueList, dbValueList)
    [print (time) for time in timerList]

def readEncodedJson():
    encoded_file = open('../../json/records_encoded.json')
    encoded_data_collection_json = json.load(encoded_file)
    encoded_data = encoded_data_collection_json['records_encoded']
    data_collector = []
    for data in encoded_data:
        data_collector.append(data)
    #print (data_collector[1])
    return data_collector

def readDecodedJson():
    decoded_file = open('../../json/records_decoded.json')
    decoded_data_collection = json.load(decoded_file)
    decoded_data_json = decoded_data_collection['records_decoded']
    #print(decoded_data_json[1])
    data_collector = []
    decoded_data_list = []
    for data in decoded_data_json:
        decoded_data_list = []
        decoded_data_list.append("P")
        decoded_data_list.append(data['line1']['issuing_country'])
        decoded_data_list.append(data['line1']['last_name'])
        given_name = data['line1']['given_name'].split(" ")
        decoded_data_list.append(given_name[0])
        if(len(given_name) == 1):
            decoded_data_list.append("")
        else:
            decoded_data_list.append(given_name[1])
        decoded_data_list.append(data['line2']['passport_number'])
        decoded_data_list.append(data['line2']['country_code'])
        decoded_data_list.append(data['line2']['birth_date'])
        decoded_data_list.append(data['line2']['sex'])
        decoded_data_list.append(data['line2']['expiration_date'])
        decoded_data_list.append(data['line2']['personal_number'])
        data_collector.append(decoded_data_list)
    #print (data_collector[1])
    return data_collector

def calcTimeForK(k, scanValueList, dbValueList):
    tic = time.perf_counter()
    for dataIndex in range(k):
        scanValue = scanValueList[dataIndex]
        dbValue = dbValueList[dataIndex]
    #scanValue = "P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<5"
    #dbValue = ["P","UTO","ERIKSSON","ANNA","MARIA","L898902C3", "UTO",740812, "F",120415,"ZE184226B"]
        m.startFunc(scanValue,dbValue)
    toc = time.perf_counter()
    calcTime = toc - tic
    timerList.append([k,calcTime])

if __name__ == "__main__":
    main()

