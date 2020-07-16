from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyme(title,message):
	notification.notify(
		title = title,
		message = message,
		app_icon = "icon.ico",
		timeout = 10
		)
    
def getdata(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
	#notifyme("Divyanshu","Hii There")
    html_doc = getdata("https://www.mohfw.gov.in/")
    #print(html_doc)
    soup = BeautifulSoup(html_doc,'html.parser')
    #print(soup.pretiffy())
    myStr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myStr += tr.get_text()
    
    myStr = myStr[1:]
    #print(myStr)
    myList = myStr.split('\n\n')
    #print(myList)
    check = ['Madhya Pradesh']
    for item in myList[0:34]:
        item = item.split('\n')
        #print(item)
        if item[1] in check:
            title = "COVID-19 Updates:"
            message = f"State : {item[1]}\nCases : {item[2]}\nRecovered : {item[3]}\nDeaths : {item[4]}"
            notifyme(title, message)
    