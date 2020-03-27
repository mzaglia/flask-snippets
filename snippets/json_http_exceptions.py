from flask import Flask
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(Exception)
def exception_handler(e):
    """Handle Exceptions."""
    if isinstance(e, HTTPException):
        return {'code': e.code, 'description': e.description}, e.code
    app.logger.exception(e)
    return {'code': '500', 'description': 'Internal Server Error'}, 500

if __name__ == '__main__':
    app.run(debug=True)
