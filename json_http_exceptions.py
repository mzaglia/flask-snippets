from flask import Flask
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(HTTPException)
def http_exception_handler(e):
    return {'code': e.code, 'description': e.description}

if __name__ == '__main__':
    app.run(debug=True)
