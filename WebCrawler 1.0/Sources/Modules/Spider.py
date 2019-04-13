
import requests
from bs4 import BeautifulSoup

from asyncio.log import logger

#Spider Class to gather all the app web links for the analyzation.
class SpiderClass:
    
    def Spider(self, limit):
        page = 1
        
        webAppList = []
        
        while page < limit:
            url = r"https://play.google.com/store/apps/category/GAME/collection/topselling_new_free?hl=en"
            try:
            
                source_Code = requests.get(url, timeout = 10)
            
                raw_text = source_Code.text
        
                soup = BeautifulSoup(raw_text, "html.parser")
          
                self.FetchAppLinks(soup, webAppList)
                
            
            except requests.ConnectionError as connError:
                logger.log("Connection Error while connecting to Play store: ", url," Error: ", connError)
            
            except requests.HTTPError as httpError:
                logger.log("Invalid HTTP response to Play store: ", url, " Error: ", httpError)
            
            except requests.Timeout() as requestTimeoutError:
                logger.log("Time-out to connect to Play store: ", url, " Error: ", requestTimeoutError)
                
            except requests.TooManyRedirects() as redirectsError:
                logger.log("Too many redirects for connection to Play store: ", url, " Error: ", redirectsError)
                
            #except HTMLParseError as htmlParsingError: 
            #   logger.log("HTMLParse Error: ", htmlParsingError)
            
            except Exception as e:
                logger.log("Execpetion occured at Func Spider: ", e)
            
            except requests.exceptions.Timeout as timeoutException:
                logger.log("Timeout Exception", timeoutException)
                
            page += 1
        
        return webAppList
    
    
    def FetchAppLinks(self, soup, webAppList):
        for link in soup.find_all('a',{'class': 'title'}):
            hreff = "https://play.google.com" + link.get('href')
            
            if((webAppList.__contains__(hreff))!= True):
                    webAppList.append(str(hreff)) 
        
    