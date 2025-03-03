import requests

r = requests.post("https://ylz6jajpoido2wzwn2nhkqjvba0mzpyn.lambda-url.us-east-1.on.aws/test/insertdistance",
                  data={"graph":"Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"})