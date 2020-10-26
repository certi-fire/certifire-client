import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

class Lemur:
    def __init__(self, 
            url: str =None, 
            uname:str =None, 
            pwd:str =None):
        self.url = url if url else os.getenv("LEMUR_URL")
        self.uname = uname if uname else os.getenv("LEMUR_UNAME")
        self.pwd = pwd if pwd else os.getenv("LEMUR_PWD")
        self.session = self.authenticate()
    
    def authenticate(self):
        s = requests.session()
        s.mount("https://", requests.adapters.HTTPAdapter(max_retries=3))
        s.headers.update({'content-type': 'application/json'})
        authResponse = s.post(
            "{0}/auth/login".format(self.url),
            data=json.dumps({'username': self.uname, 'password': self.pwd}),
                    )
        if authResponse.status_code == 401:
            print("Authentication to Lemur in ({0}) failed".format(self.url))
            return None
        print("Authentication to Lemur in ({0}) succeeded!".format(self.url))
        token = authResponse.json()['token']
        s.headers.update({'Authorization': 'Bearer ' + token})
        return s

    def getCertificates(self, id = None):
        geturl = self.url + '/certificates'
        if id:
            if type(id) == int:
                geturl += '/' + str(id)
            else:
                geturl += '?filter=name;{0}'.format(id)
        return self.session.get(geturl).json()

    def newCert(self,
            name: str,
            owner: str = None,  
            authority: str = None, 
            notify: bool = True):
        owner = owner if owner else os.getenv("CERT_DEFAULT_OWNER")
        authority = authority if authority else os.getenv("CERT_DEFAULT_AUTHORITY")

        data = {
            "owner": owner,
            "commonName": name,
            "extensions": {
              "subAltNames": {
                "names": [
                  {
                    "nameType": "DNSName",
                    "value": name
                  }
                ]
              }
            },
            "notify": notify,
            "authority": {
              "name": authority
            }
        }

        posturl = self.url + '/certificates'
        return self.session.post(posturl, data=json.dumps(data)).json()