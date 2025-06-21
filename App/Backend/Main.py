from WebCommunication import WebCommunication
from Hash import Hash

class Main:
    def generateHash(data):
        url=data['url']
        try:
            scode=WebCommunication.readHtml(url)
            if isinstance(scode, str):
                retVal ={
                    'status':1,
                    'msg':scode
                }
                
            else:
                hashVal=Hash.genHash_sha256(scode)
                retVal ={
                    'status':1,
                    'link':url,
                    'hash':hashVal,
                    'msg':"Hash Generated."
                }

        except Exception as e:
            retVal = {
                "Status":0, 
                "Error":e,
                "msg":"Error : E03 - Failed to generate Hash for URL"
            }
        
        return retVal
    
    def compareHash(data):
        url=data['url']
        inHash=data['hash']
        try:
            scode=WebCommunication.readHtml(url)
            hashVal=Hash.genHash_sha256(scode)
            retVal ={
                'status':1,
                'link':url,
                'hash':hashVal,
                'inhash':inHash,
            }
            if hashVal == inHash:
                retVal['msg'] = "Hash Matched"
            else:
                retVal['msg'] = "Hash value Changed"
               
        except Exception as e:
            retVal = {
                "Status":0, 
                "Error":e,
                "msg":"Error : E03 - Failed to generate Hash for URL"
            }
        
        return retVal