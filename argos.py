import requests
import json
import time as t
from discord import *
from colorama import init, Fore, Back, Style
from os import system

system('title ' + ' ARGOS BOT 2.0')

init(convert=True)

productID = ['3106437', '8107242', '4123770', '7928556', '8956730'] #, '2078126', '3280858', '2077921'


catentryId={
    '3106437': '2047925',
    '8107242': '1607384',
    '3280858': '1988947',
    '2077921': '1957846',
    '2078126': '1957844',
    '4123770': '1336895',
    '7928556': '1607269',
    '8956730': '1810400'
}

productTitle = {
    '3106437': 'Lay-Z-Spa Cancun 2-4 Person Hot Tub - Home Delivery Only',
    '8107242': 'Lay Z Spa Bali 2-4 Person LED Hot Tub - Home Delivery Only',
    '3280858': 'Portal TV from Facebook',
    '2077921': 'Nintendo Switch Console - Neon with improved battery',
    '2078126': 'Nintendo Switch Console - Grey with improved battery',
    '4123770': 'Remington Quick Cut Hair Clipper',
    '7928556': 'Lay-Z-Spa St Moritz 5-7 Person Hot Tub',
    '8956730': 'Lay-Z-Spa Helsinki 7 Person AirJet Hot Tub'
}

headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

def productSearch():
    for i in range(len(productID)):
        url = "https://www.argos.co.uk/webapp/wcs/stores/servlet/CollectionFfm?storeId=10151&langId=110&noCollectOrDeliver=false&prefixHTTP=https%3A%2F%2Fwww.argos.co.uk%2Fwebapp%2Fwcs%2Fstores%2Fservlet&displayLayoutB=false&stockCheckAvailable=true&sourceId=&isOneClickEligibleForThisProduct=true&checkStore=true&actionType&isConvenienceResponseNeeded=false&partNumber={}&formattedPartNumber={}&catentryId={}&collectable=true&deliverableOnly=false&collectableOnly=false&pdMaxAvailable=10&stockCheck=true&quantity=1&storeDistance=0&pageReqType=nearestStore&physicalStoreId=4707&selectedStore=High%20Wycombe%20Argos%20in%20Sainsburys".format(productID[i], productID[i], catentryId[productID[i]])
        r=requests.get(url, headers=headers)
        content = r.json()
        stock=content['invRes'][0]['inStock']
        if stock == False:
            dateTimeObj = datetime.now()
            print(Fore.YELLOW + ' [{}] Currently Out Of Stock: {}'.format(str(dateTimeObj),productTitle[productID[i]]))
        else:
            dateTimeObj = datetime.now()
            print(Fore.GREEN + '[{}] In Stock: {}'.format(str(dateTimeObj),productTitle[productID[i]]))
            prodtitle=productTitle[productID[i]]
            url='https://www.argos.co.uk/product/' + productID[i]
            sendHook(prodtitle, url, dateTimeObj)

while (True):
    try:
        productSearch()
    except KeyError:
        dateTimeObj = datetime.now()
        print(Fore.RED + '[{}] KEY ERROR: INVRES NOT FOUND'.format(str(dateTimeObj)))
    except json.decoder.JSONDecodeError:
        print(Fore.RED + '[{}] ISSUE CONVERTING JSON OBJECT'.format(str(dateTimeObj)))
    except ConnectionError:
        print(Fore.RED + '[{}] LOST CONNECTION....'.format(str(dateTimeObj)))
