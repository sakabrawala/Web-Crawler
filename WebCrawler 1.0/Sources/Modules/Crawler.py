
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import threading
from asyncio.log import logger
import re 
from Sources.ObjectModel.AppDetails import AppDetails

class Crawler:
    
    def Cleaner(self, appUrlslist, fetchedUrlsList):

        pendingAppUrlslist = [e for e in appUrlslist if e not in fetchedUrlsList]
        
        return pendingAppUrlslist
            
    def Crawl(self,appList):
       
        try:
            appPool = Pool()
            
            result = appPool.map(self.GooglePlayStoreCrawler, appList)
        
            appPool.close()
        
            appPool.join()
            
            return result
                    
        except Exception as e:
            logger.critical(e)
        
    def GooglePlayStoreCrawler(self, appLink):
        #for appLink in appList:
        appDetails = AppDetails()
        
        appDetails.url = appLink
        
        appDetails.appStore = "Google Play Store"
        
        #print(appLink)
        sourceCode = requests.get(appLink)
        rawText = sourceCode.text
        soupObj = BeautifulSoup(rawText,"html.parser")
    
        #Thread for title
        tTitle = threading.Thread(target=self.GetTitle, args=(soupObj, appDetails))
                   
        #Thread for ratings
        tReviews = threading.Thread(target=self.GetRatings,args=(soupObj, appDetails))
        
        #Thread for price
        tPrice = threading.Thread(target=self.GetPrice, args=(soupObj, appDetails))
            
        #Thread for total Reviewers
        tTotalReviewers = threading.Thread(target=self.GetTotalReviewers, args=(soupObj, appDetails))
            
        #Thread for Genere
        tGenere = threading.Thread(target=self.GetGenere, args=(soupObj, appDetails))
                       
        #Thread for author
        tAuthor = threading.Thread(target=self.GetDeveloper, args=(soupObj, appDetails))
            
        #Installs
        tInstalls = threading.Thread(target=self.GetInstalls, args=(soupObj, appDetails))
                        
        #Content
        tContent = threading.Thread(target=self.GetContent, args=(soupObj, appDetails))
    
        threadList = [tTitle, tGenere, tPrice, tAuthor, tContent, tInstalls, tReviews, tTotalReviewers]
            
        try:
                
            #Initializing the threads
            for threadApp in threadList:
                threadApp.start()
                
            #Waiting for threads to complete their tasks    
            for threadApp in threadList:
                threadApp.join()
            
        except Exception as e: 
            logger.log("Exception caught in threading in Crawler Class: ", e)
                        
        finally:
            
            return appDetails
    
    def GetPrice(self, soupObj, appDetails):
         
        price = soupObj.find('button', attrs={'class': 'price buy id-track-click id-track-impression'})      
        appDetails.price = price.strip()
                 
    def GetTitle(self, soupObj, appDetails):
        #User Rating
        title = soupObj.find(attrs={'class': 'AHFaub'})
        
        appDetails.title = title.text.strip()
    
    def GetRatings(self, soupObj, appDetails):
        #User Rating
        score = soupObj.find('div', attrs={'class': 'BHMmbe'})
        
        appDetails.rating = score.text.strip()
        
    def GetGenere(self, soupObj, appDetails):
        genere = soupObj.find(attrs={'itemprop': 'genre'})
        
        appDetails.genere = genere.text.strip()
    
    def GetInstalls(self, soupObj, appDetails):
        try:
            pull = soupObj.find('div', attrs={'class': 'content', 'itemprop': 'numDownloads'})
            appDetails.installs = pull.text
        
        except TypeError as typeError:
            logger.log("Type Error at GetInstalls: ", typeError)
        
        except Exception as e:
            logger.log("Exception at GetInstalls: ", e)
        
    def GetTotalReviewers(self, soupObj, appDetails):
        totalReviews = soupObj.find('span', attrs={'class': 'EymY4b'})
        appDetails.totalReviews = totalReviews.text
    
    def GetDeveloper(self, soupObj, appDetails):    
        dev = soupObj.find(attrs={'class': 'hrTbp R8zArc'})
        
        appDetails.author = dev.text.strip()
    
    def GetContent(self, soupObj, appDetails):    
        contents = soupObj.find(attrs={'itemprop': 'contentRating'})
        
        fetchedContents = contents.text.strip()
        
        if(fetchedContents.count('Mature') | fetchedContents.count('+')):
            appDetails.adult = True
