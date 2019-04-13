
from Sources.Modules.Crawler import Crawler 
from Sources.Modules.Spider import SpiderClass 
from Sources.DataHandler.CSVHandler import CSVHandlerClass

class Controller:
    
    DBHandler = CSVHandlerClass()
    
    fetchedUrlsList = DBHandler.FetchedUrls()
    
    spiderObj = SpiderClass()      
    
    crawlerObj = Crawler()
    
    urlsList = spiderObj.Spider(2)
  
    
    pendingUrlsList = []
    
    if(len(fetchedUrlsList) > 0):
        pendingUrlsList = crawlerObj.Cleaner(urlsList, fetchedUrlsList)
    else:
        pendingUrlsList = urlsList
    
    
    if __name__ == '__main__':
        
        if(len(pendingUrlsList) > 0):
            print("B4 crawler")
            detailsList = crawlerObj.Crawl(pendingUrlsList)
            print("after crawler")
            print(len(detailsList))
    
            r = DBHandler.CollectAppDetails(detailsList)
        
            print(r)
    