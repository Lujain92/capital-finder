from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        my_dictionary=dict(query_string_list)
        if 'capital' in my_dictionary:
            capital=my_dictionary['capital']
            url='https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital)
            data=r.json()
            # if data['message']=="Not Found":
            #     result="enter valid one"
            # else:
            country=data[0]["name"]["common"]
            result=f"the country of {capital}is {country} "
        # else:
        #     country="please give me a capital city"
        if 'country' in my_dictionary:
            country=my_dictionary['country']
            url='https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data=r.json()
            
            capital=data[0]["capital"][0]
            result=f"the capital of {country} is {capital}"
            
        # else:
        #     country="please give me a country"
        
        # if 'capital' in my_dictionary:
        #     capital=my_dictionary['capital']
        #     print(capital)
        #     url='https://restcountries.com/v3.1/all'
        #     r = requests.get(url)
        #     data=r.json()
        #     for x in data:
        #         capitalx=x["capital"][0]
        #         if capitalx==capital:
        #             message=x['name']['common']
        #             print(message)
                
                
                    
                   

        # else:
        #     message="please give me a capital city"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(result.encode())
        return