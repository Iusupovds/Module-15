import json

with open('json_example.json', encoding='utf8') as f:
    templates = json.load(f)
    
    
def CheckInt(item):
    return isinstance(item, int)

def CheckStr(item):
    return isinstance(item, str)

def CheckBool(item):
    return isinstance(item, bool)

def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False
    
def CheckStrValue(item, val): 
    if isinstance(item, str):
        return item in val
    else:
        return False
    
def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})

listOfItems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url', 'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'itemId': 'str', 'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool', 'firstInSession': 'bool'}

Error = []
for items in templates:
    for item in items:
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not CheckInt(item[item]):
                    ErrorLog(item, items[item], f'expected type {listOfItems[item]}')
            elif listOfItems[item] == 'str':
                if not CheckStr(item[item]):
                    ErrorLog(item, items[item], f'expected type {listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not CheckBool(item[item]):
                    ErrorLog(item, items[item], f'expected type {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not CheckUrl(item[item]):
                    ErrorLog(item, items[item], f'expected type {listOfItems[item]}')
            elif listOfItems[item] == 'val':
                if not CheckStrValue(item[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], 'expected type itemBuyEvent or itemViewEvent')
            else:
                ErrorLog(item, items[item], 'unexpected value')
        else:
            ErrorLog(item, items[item], 'unkknown data')

if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)
    
