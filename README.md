# Py_Bot: A Bot to Beat All Bots
## Or at least to buy stuff alongside other bots
This is a bot I have created with a dual purpose of practicing web scraping with Python and finding products online that are perpetually out of stock.
This bot basically automates F5-ing the sites you have no time to F5.

## Setup
You can clone this branch using the following code in your terminal in the directory you desire
```
git clone https://github.com/edfranco/pybot.git my-dir
```

Go to the directory that this code lives in and once there use the following code in terminal to install Python packages

If you have Python2
```
pip install -r requirements.txt
```
If you have Python3
```
pip3 install -r requirements.txt
```
To run the bot just use

```
python3 bot.py
```
The bot will scrape the urls provided from a list in the file products_db.py. Py_Bot looks for the "Buy Now" button on the page. (Every store supported by the bot has one and the bot is tuned for each one)

If the "Buy Now" button doesn't exist it most likely means the item is not in stock and it will look for the next item on the list. If the "Buy Now" button does exist then it will look for the element containing the price, take the text, remove the dollar sign and comma from the number, turn it into a float, round it to the nearest hundredth and then compare that to the max price set for the item.

``
float(driver.find_element_by_id("price_inside_buybox").text.translate({ord(i):None for i in '$,'})) > i.max_price
``

![Screenshot of terminal showing output of running python3 bot.py showing items out of stock](https://user-images.githubusercontent.com/11623323/107704382-fe63f500-6c71-11eb-8f4b-a50d0df6a711.png)

If the item is within your budget it will click the buy now button, log you in, then click the place order button on Amazon

## Buy Functionality
While this bot serves to refresh and scrape web pages for information and relaying it to a user, it actually CAN buy items from AMAZON specifically as long as
the item is in stock and the max price the user has set for the item is less than the listed price. To set up that functionality you'll want to create a .env file

```
touch .env
```

and in that file add your email and password for Amazon

```
EMAIL = YOUR_EMAIL
AMAZON_PASSWORD = YOUR_PASSWORD
```

Inspired by [Falcodrin on Twitch](https://www.twitch.tv/falcodrin)