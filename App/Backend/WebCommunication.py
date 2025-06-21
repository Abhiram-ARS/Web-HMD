class WebCommunication:
    def readHtml(url):
        import requests
        from bs4 import BeautifulSoup

        try: 
            response = requests.get(url)
            text = response.text

            soup = BeautifulSoup(text, 'html.parser')
            html_content = soup.get_text().strip().encode('utf-8')
            return(html_content)
            
        except:
            return("Error : E01 - Failed To Read HTML contents in url. ")
        