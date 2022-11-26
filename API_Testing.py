import requests
from bs4 import BeautifulSoup
with open('C:/Users/UJJWAL KUMAR/Desktop/python project/LnB.html') as f:
    content=f.read()

url = 'file:///C:/Users/UJJWAL%20KUMAR/Downloads/LnB.html'
r = requests.post(content,json={'Years of Experience':2, 'Projects Build':9, 'Interview Grades':6})

print(r.json())
