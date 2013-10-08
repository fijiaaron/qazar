from flask import render_template
from app import app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def controller(path):
    """
    A catch-all function serving every URL.
    """
    return render_template(path)
