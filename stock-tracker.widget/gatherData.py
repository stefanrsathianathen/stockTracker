import urllib2
import json

KEY = ""
stocks = ["SPY","DIA","AAPL","FB","DIS","AMZN","TSLA","GOOG"]

darkred = "style='background:#600000 !important;'"
midred = "style=background:#900000 !important;'"
lightred = "style=background:#FF0000 !important;'"
darkgreen = "style=background:#006000 !important;'"
midgreen = "style=background:#009000 !important;'"
lightgreen = "style=background:#00B000 !important;'"


def cleanData(data):
    name = data["symbol"]
    price = data["latestPrice"]
    opening_price = data["previousClose"]
    percent_change = calculatePercent(opening_price,price)
    price = "{0:,.2f}".format(price)
    change = data["change"]

    if percent_change == 0:
        print("<tr><td style='background: #366797 !important;'>{}</td><td >${}</td><td>{}</td><td>{}%</td></tr>".format(name,price,percent_change,change))
    if percent_change > 0:
        if percent_change > 4:
            print("<tr><td style='background: #366797 !important;'>{1}</td><td {0}>${2}</td><td {0}>+{4}</td><td {0}>{3}%</td></tr>".format(lightgreen,name,price,percent_change,change))
        elif percent_change > 1:
            print("<tr><td style='background: #366797 !important;'>{1}</td><td {0}>${2}</td><td {0}>+{4}</td><td {0}>{3}%</td></tr>".format(midgreen,name,price,percent_change,change))
        else:
            print("<tr><td style='background: #366797 !important;'>{1}</td><td {0}>${2}</td><td {0}>+{4}</td><td {0}>{3}%</td></tr>".format(darkgreen,name,price,percent_change,change))
    elif percent_change < 0:
        if percent_change < -4:
            print("<tr><td style='background: #366797 !important;'>{1}</td><td {0}>${2}</td><td {0}>{4}</td><td {0}>{3}%</td></tr>".format(lightred,name,price,percent_change,change))
        elif percent_change < -1:
            print("<tr><td style='background: #366797 !important;'>{1}</td><td {0}>${2}</td><td {0}>{4}</td><td {0}>{3}%</td></tr>".format(midred,name,price,percent_change,change))
        else:
            print("<tr><td style='background: #366797 !important;'>{1}</td><td {0}>${2}</td><td {0}>{4}</td><td {0}>{3}%</td></tr>".format(darkred,name,price,percent_change,change))
    
def calculatePercent(openP,closeP):
    return round(((closeP-openP)/openP)*100,2)



for x in stocks:
    response = urllib2.urlopen('https://cloud.iexapis.com/stable/stock/{}/book?token={}'.format(x,KEY))
    data = json.loads(response.read())
    cleanData(data["quote"])
    response.close()

