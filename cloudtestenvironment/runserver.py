#!python
import sys
sys.path.insert(0, '.')

from cloudtestenvironment import app as application
application.run(host='0.0.0.0', port=5000, debug=True)