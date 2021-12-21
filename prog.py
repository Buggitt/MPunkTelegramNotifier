# Created by Buggitt
# Program that notifies via telegram when an mpunk is mined for your address
# so that it can be minted manually.


#Make sure to install python, the below libraries, and setup the initial setup
# of telegram_send, which for now will require setting up your own bot.
import json, requests
from ast import literal_eval
import telegram_send
import time

# Functions
def print_mpunk_info(item):
    print("Discoverer Addr: " + item["address"])
    print("Nonce: " + item["nonce"])
    dec = literal_eval(item["nonce"])
    print("Nonce converted to dec: ", dec )
    print("Time Stamp: " + item["ts"])

def print_pool_status(item):
    print("Current Addr Pool Pointed: " + item["current"])
    print("Pool Hashrate: " + item["hashrate"])
    print("My Score: " , item["pings"][my_addr])

def search_mminer4pool_for_my_mpunks():
    xx = 0
    print("Looking for your punks in history")
    for x in range(0,len(finds)):
        if finds[x]["address"] == my_addr:
            print(finds[x])
            xx+1
    if xx > 0:
        print("\nat least one mpunk found")
    else:
        print("None found.")


# Varibles


my_addr = "0x96b11E6D2c9f62380Fe328Dc30abAa9bF4C760ca"

# Program


telegram_send.send(messages=["starting.. :D"])



dothething = True
while dothething:
    score_url = requests.get("https://trust-in.info/score.txt")
    score_raw = "[" + score_url.text + "]"

    data = json.loads(score_raw)

    score = data[0]
    print_pool_status(score)



    latest_url = requests.get("https://trust-in.info/latest.txt")
    latest_raw = "[" + latest_url.text + "]"

    data = json.loads(latest_raw)

    latest = data[0]

    finds_url = requests.get("https://trust-in.info/nonces.txt")
    finds_raw = "[" + finds_url.text + "]"


#There's some mistakes in the found nonces data and this fixes them.
    finds_raw = finds_raw.replace("}{" , "},{" )
    finds_raw = finds_raw.replace("}\n{" , "},{" )

    #print(finds_raw)

    data = json.loads(finds_raw)
    #print(data)
    finds = data




#Use this to test a success case of found mpunk.
    #my_addr=latest["address"]

    if my_addr == latest["address"]:
        telegram_send.send(messages=["GOT a MPunk!"])
        telegram_send.send(messages=[latest])
        dothething = False
        print("Pool found an mpunk for your address!")
        print_mpunk_info(latest)
        exit()

    print("waiting...")
    time.sleep(60)
