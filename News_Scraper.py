import requests
from bs4 import BeautifulSoup
def scrape_headlines():
    url="https://www.thehindu.com/"
    try:
        response=requests.get(url)
        if response.status_code==200:
            print("Website fetched successfully!")
            soup=BeautifulSoup(response.text,"html.parser")
            headlines=soup.find_all("h2")
            file=open("headlines.txt","w",encoding="utf-8")
            print("Top news Headlines:\n")
            count=1
            for headline in headlines:
                text=headline.get_text().strip()
                if text!="":
                    print(str(count)+ "."+text )
                    file.write(str(count)+"."+text+"\n")
                    count+=1
                file.close()
                print("\n Headlines saved in headlines.txt")
        else:
            print("Failed to fetch website")
            print("Status code:",response.status_code)
    except Exception as e:
        print("Error occured:",e)
scrape_headlines()