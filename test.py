import requests
from pprint import pprint
import json

def getWordDef(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url).json()
    definitions = []
    # pprint(response)
    k = 0;
    l = 0;
    for i in response[0]['meanings']:
        pprint(response[0]['meanings'][k]['definitions'][0]['definition'])
        definitions.append(response[0]['meanings'][k]['definitions'][0]['definition'])
        k += 1
    for i in definitions:
        print("Definition " + str(l) + ": " + i)
        l += 1
        
    return definitions

def getWordSyn(word):
    pass
def getWordAnt(word):
    pass


# no = response[0]['meanings'][0]['definitions']
# no1 = response[0]['meanings'][1]['definitions']
# no2 = response[0]['meanings'][2]['definitions']
# print(no)
# print(no1)
# print(no2)