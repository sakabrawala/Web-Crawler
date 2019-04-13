
import os
import openpyxl 
import pandas as pd 
from Sources.ObjectModel.AppDetails import AppDetails 
from pandas import DataFrame
from asyncio.log import logger
class CSVHandlerClass:
    
    global filePath
    
    filePath =r'C:\Users\Smit\Desktop\STQA\ApplicationData.csv'
       
    def FetchedUrls(self):   
        try:
            data = []
            if (os.path.isfile(filePath)== True):
                data = pd.read_csv(filePath, usecols=['Urls']).T.values.tolist()[0]
                return data
            else:
                return data
        except ValueError as e:
            logger.log(e) 
        
        except TypeError as e:
            logger.log(e) 
        
        except KeyError as e:
            logger.log(e) 
        
        except IndexError as e:
            logger.log(e) 
        
        except IOError as e:
            logger.log(e) 
        
    def IsEmptyString(self,content):
        if content:
            return True
        else:
            return False 

        
    def CollectAppDetails(self, appLicationsList):
        appTitle = []
        appPrice = []
        appRating = []
        appTotalReviews = []
        appGenere = []
        appAuthor = []
        appInstalls = []
        appAdultContent = []
        appUrls = []
        
        for app in appLicationsList:
            appTitle.append(app.title) #if self.IsEmptyString(app.title) else "")
            appPrice.append(app.price)# if self.IsEmptyString(app.price) else "")
            appRating.append(app.rating)# if self.IsEmptyString(app.rating) else "")
            appTotalReviews.append(app.totalReviews)# if self.IsEmptyString(app.totalReviews) else "")
            appGenere.append(app.genere)# if self.IsEmptyString(app.genere) else "")
            appAuthor.append(app.author)# if self.IsEmptyString(app.author) else "")
            appInstalls.append(app.installs)# if self.IsEmptyString(app.installs) else "")
            appAdultContent.append(app.adult)# if self.IsEmptyString(app.adult) else "")
            appUrls.append(app.url)# if self.IsEmptyString(app.url) else "")
                
        df_appDetails = {
            "Title" : appTitle,
            "Price" : appPrice,
            "Rating" :appRating,
            "TotalReviews" : appTotalReviews,
            "Genere" : appGenere,
            "Author" : appAuthor,
            "Installs" : appInstalls,
            "Adult" : appAdultContent,
            "Urls" : appUrls
            }
        
        df = pd.DataFrame(df_appDetails)
        
        errorCount = 0
        try:
        
            if (os.path.isfile(filePath)!= True):  
                df.to_csv(filePath, mode='a', header=True, index=False)
            else :
                df.to_csv(filePath, mode='a', header=False, index=False)
        
        except ValueError as e:
            errorCount =+ 1 
            logger.log(e) 
        
        except TypeError as e:
            errorCount =+ 1
            logger.log(e) 
        
        except KeyError as e:
            errorCount =+ 1
            logger.log(e) 
        
        except IndexError as e:
            errorCount =+ 1
            logger.log(e) 
        
        except IOError as e:
            errorCount =+ 1
            logger.log(e)
         
        except Exception as e:
            errorCount =+ 1
            logger.log(e) 
        
        finally:
            if(errorCount > 0):
                return False
            else:
                return True