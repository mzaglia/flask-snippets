from flask import Flask

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
if __name__ == '__main__':
        app.run(debug=True)
