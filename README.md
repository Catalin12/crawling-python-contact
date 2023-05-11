# crawling-python-contact
This Python script utilizes the Scrapy framework to extract addresses from multiple websites.
  The script starts by reading a list of websites from a file. Then, for each website, an HTTP request is made to fetch the web page content.
  If the response is successful (status 200), CSS selectors are used to extract addresses (and others things, unfortunately...) from various HTML elements such as '<span>', '<p>', '<div>', '<address>', '<footer>', and others.
  The extracted addresses are saved in a file named "adrese.txt". During the extraction process, certain additional checks are applied.
  
In summary, this Python script offers a solution to extract addresses from websites using the Scrapy framework, applying specific checks and manipulations as per the requirements.
