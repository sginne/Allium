#  (?<=(?<!\\)(?:\\{2})*)\*\*[^\\*]*(?:\\.[^\\*]*)*\*\*
import re
import hashlib
from flask import current_app
from . import http_module
from sqlalchemy import create_engine,MetaData
import sqlalchemy
from .. import models,currency,db
import time
def process_orders(app,engine):
    print(engine.table_names())
    orders = models.Orders.query.all()
    with current_app.app_context():
        currency_module=currency.FiatCurrency(app.config['CURRENCY']).module
    for order in orders:
        status=str(order.status)
        data=currency_module.read_wallet(order.public_wallet)
        if status=="Status.placed":
        #{'hash160': 'e8bb29a0b2ee355fe3a92c6911011ae88c1e2ca6', 'address': '1NDZynro2f1uSTeM2WWbypH7xDHKgzudHF', 'n_tx': 0, 'n_unredeemed': 0, 'total_received':0, 'total_sent': 0, 'final_balance': 0, 'txs': []}
  
            #print(data)
            order.status="fully_paid"
            db.session.commit()
        #print(currency_module.read_wallet(order.public_wallet))
        time.sleep(app.config['UPDATE_RATE_DELAY'])
       
def password_hashing(password):
    """
    Returns sha512 from password and app.config['SECRET_KEY']
    :param password: password string
    :return: salted and hashed password
    """
    print("Something hashed")
    return hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),current_app.config['SECRET_KEY'].encode('utf-8'),66766).hex()#fix me 66766 is for no reason

def markup(string_to_parse):
    """
    Returns parsed text with <html>
    :param string_to_parse: String to parse into HTML
    :return: returns html
    """
    bold_re=re.compile(r".*?(\*\*(.*?)\*\*).*?") # **bold**
    italic_re=re.compile(r".*?(''(.*?)'').*?")  # ''italics**
    image_re=re.compile(r".*?(!\[\-(.*?)\-\]).*?")  # ![-image_id-]

    found_matches=re.findall(image_re,string_to_parse)
    for match in found_matches:
        string_to_parse=string_to_parse.replace(match[0],"<div class=\"float-left popover popover-right\"><img class=\"card mx-2\" align=\"left\" width=\"100px\" src=\"/picture/"+match[1]+"\"><div class=\"popover-container\"><img class=\"card mx-2\" align=\"left\" width=\"400px;\" src=\"/picture/"+match[1]+"\"></div></div>")

    #.thumbnail: hover\{position: relative;top: -40 px;left: -100px;width:800px;height: auto;display: block;z - index: 999;\}
    found_matches=re.findall(italic_re,string_to_parse)
    for match in found_matches:
        string_to_parse=string_to_parse.replace(match[0],"<i>"+match[1]+"</i>")

    found_matches=re.findall(bold_re,string_to_parse)
    for match in found_matches:
        string_to_parse=string_to_parse.replace(match[0],"<b>"+match[1]+"</b>")
    return string_to_parse.replace("\n","<br>")
def markup_list_descriptions(items_list):
    return_items=[]
    for item in items_list:
        item.description=markup(item.description)
        return_items.append(item)
    return return_items
