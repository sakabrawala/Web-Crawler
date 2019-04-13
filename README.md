# Web-Crawler

No of classes - 5
1) SPIDER CLASS
2) CRAWLER CLASS
3) CSVHANDLER
4) CONTROLLER
5) ANALYSIS

MAIN LIBRARIES USED 
1) BEAUTIFULSOUP- Beautiful Soup is a Python package for parsing HTML and XML documents.
2) NUMPY - NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
3) PANDAS - pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.

Steps - 
1) SPIDER CLASS fetches the URL of the website to be parsed.
2) CRAWLER CLASS crawls the page and matches the class defined by us matches the class of the website or not. Like TITLE, USER RATING CLASS etc
3) CSVHANDLER manages the data which matches and creates a CSV file in our allocated location on drive. It later stores them in tables where name of the table is the CLASS name.
4) CONTROLLER class is the controller for running all these classes. It's the parent class.
5) ANALYSIS class is used for plotling graph and according to our data.
