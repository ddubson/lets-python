import http.client # python 3.x+

client = http.client.HTTPConnection("www.google.com")

client.request("GET", "/")
data = client.getresponse()
print(data.code)
print(data.headers)
text = data.readlines()
for t in text:
    print(t.decode('utf-8'))
