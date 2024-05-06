from flask import Flask, request
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/', methods=['GET'])
def home():
    item = request.args.get('item')
    url = f'https://www.iconfinder.com/search?q={item}'
    
    # Send a GET request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url , headers=headers)
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the first element with className="view"
    element = soup.find_all(class_='d-block',limit=3)
    # print(element[2]['src'])
    return element[2]['src'] if element[2] else "Element not found"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)