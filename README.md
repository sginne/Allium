![AlliumShop](https://github.com/sginne/Allium/blob/master/app/static/github-logo.png?raw=true)

*clearnet or deepweb - your keys are yours, no blockchain downloading. full control for no price*

##Слава Україне!

I am Timo, and I am ukrainian, been living in Finland, since 1994.
Still am ukraїnian. 

Development is bit chaotic due to the war.

## Introduction

**Alliu₷hop** is small, lightweight shopping system supporting ONLY cryptocurrencies.

## About

There were a lot of deepweb markets.
Markets are centralized, which makes them easy to track and close.

I, however, think that free trade should co-exist with regulated trade, and to make free, unregulated trade possible, I've decided to make opensource shop.

Reason? So that everyone with very basic technical skill can safely run own, small outlet on the *deepkweb*, mostly *Tor*,yet it should work perfectly on clearnet for anyone willing to have own free shop accepting **ONLY** cryptocurrencies, that allow balance checking and private key sweeping.

Can be used on clear web as well, with the same ease, just remember to put proper setting in config.

So, **Alliu₷hop** was born, very lightweight *python3/flask* shop, made with deepweb in mind.

* No blockchain downloading, only bitcoin supported at the moment of writting
* No graphical elements, pure-CSS, except pictures of goods for sale
* Easy sweeping (Electrum supports sweeping, for example)
* Extremely easy installation, which requires very basic knowledge of linux 
* Opensource, no binaries of any kind - you control and own your own shop, and  free to audit and change code as you wish
* Panic button with ability to reconstruct wif private keys

I've done this project before too, but wroten quickly on the knee, it is very unmaintainable with a lot of shortcuts. Keeping it updated is pain.
Laffka, however, quite works, and could be found here: https://github.com/eruina/laffka/

## Installation

* python3 -m venv venv
* source venv/bin/activate
* pip3 install -r requirements.txt
* database in App/db/data.sql, recreate #fixme
* False for SSL_Enabled or cryptolibraries #fixme

## Donations
Project is going to be funded completely by donations, but I don't see why anyonehas to support this project now.


