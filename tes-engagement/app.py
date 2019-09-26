# Import Python packages
import json
import os

# Import Bottle
import bottle
from bottle import Bottle, request, Response, run, static_file
import requests
from truckpad.bottle.cors import CorsPlugin, enable_cors

# Define dirs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'dist')

# App Config
bottle.debug(True)
app = Bottle()


@app.get('/')
def show_index():
    """Show Index page"""
    return static_file('index.html', root=STATIC_DIR)

@app.post('/comment')
def post_comment():
    comment = request.json.get('comment')
    email = request.json.get('email')
    payload = {
            'eventData': {
                'eventType': 'Comment',
                }
            }
    if comment:
        payload['eventData']['comment'] = comment
    if email:
        payload['eventData']['email'] = email
    res = requests.post('https://api.kevalin.io/collections/SERVICE.R4R.COMMENTS/events',
            headers={'Authorization': f'X-API-Key {os.getenv("KEVALIN_API_KEY")}'},
            json=payload)
    res.raise_for_status()

# Static files route
@app.get('/<filename:path>')
def get_static_files(filename):
    """Get Static files"""
    return static_file(filename, root=STATIC_DIR)


app.install(CorsPlugin(origins=['*.rax.io']))


# Run server
run(app, server='auto', host='localhost', port=8080, reloader=True)
