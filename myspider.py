import scrapy
import pandas as pd
import logging
import time


logging.getLogger('scrapy').setLevel(logging.CRITICAL)
class MySpider(scrapy.Spider):
    name = 'myspider'
    def start_requests(self):
        df = pd.read_parquet("list of company websites.snappy.parquet", engine="pyarrow")
        count = 0
        for _, row in df.iterrows():
            domain = row["domain"]
            url = "http://" + domain if not domain.startswith(("http://", "https://")) else domain
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
            count += 1
            if count % 10 == 0:
                time.sleep(1)
                print(f"pause after {count}")

    def parse(self, response):
        url = response.url
        if response.status == 200:

            addresses = response.css('footer div p::text, span.address::text, p.address::text, div.address::text, div.locations-info p:first-child::text, address::text, footer > div.library-info > p::text, footer div.library-info a::text, footer div p a::text, footer div p::text').getall()
            with open("adrese.txt", "a", encoding="utf-8") as f:
                
                f.write(f'{url} -> \n')
                for address in addresses:
                    if address is None or len(address) < 5 or address.isspace() or '©' in address:
                        continue
                    address = address.lstrip()
                    address = address.rstrip()
                    f.write(f'{address}\n')
                    print(f'{address}\n')

            if len(addresses) == 0:
                print(f'not found content for {url}')
        #else:
            #print(f'offline {url}')
        
#python -m scrapy runspider myspider.py