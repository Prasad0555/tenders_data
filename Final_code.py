#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install webdriver-manager')


# In[2]:


from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[4]:


class Web_Scraping():
    def scraping(self):
        Status = []
        Planholders = [] 
        Due_Date = []
        ID = []
        Agency_Name = []
        Titles = []
        Broadcast_Date = []
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://www.demandstar.com/app/agencies/california/city-of-sunnyvale/procurement-opportunities/e9a860f4-8f17-43af-aae7-e5dc8389f36e/"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        spans = soup.select('.text-truncate span')
        spans1 = soup.select('.list-inline-item:nth-child(4)')
        spans2 = soup.select('.list-inline-item:nth-child(2)')
        spans3 = soup.select('.list-inline-item:nth-child(1)')
        spans4 = soup.select('p')
        spans5 = soup.select('.mw-75')
        spans6 = soup.select('.list-inline-item:nth-child(3)')
        for span in spans:
            Status.append(span.text.strip())
        for span in spans1:
            Planholders.append(span.text.replace("#Planholders:","").strip())
        for span in spans2:
            Due_Date.append(span.text.replace("Due:","").strip())
        for span in spans3:
            ID.append(span.text.replace("Due:","").strip())
        for span in spans4:
            Agency_Name.append(span.text.strip())
            Agency_Name = Agency_Name[0:100]
        for span in spans5:
            Titles.append(span.text.strip())
        spans6 = soup.select('.list-inline-item:nth-child(3)')
        for span in spans6:
            Broadcast_Date.append(span.text.replace("Broadcast:","").strip())
        df=pd.DataFrame({'Titles':Titles,
                 'Agency_Name':Agency_Name,
                 'ID':ID,
                 'Planholders':Planholders,
                 'Broadcast_Date':Broadcast_Date,
                 'Due_Date':Due_Date,
                 'Status':Status,
                })
        df.to_csv('data.csv', index=False, encoding='utf-8')
        print(df.head(20))    
        return "scrapping successful"



if __name__ == "__main__":
    process = Web_Scraping()
    process.scraping()


# In[5]:


pd.read_csv('data.csv')


# In[ ]:




