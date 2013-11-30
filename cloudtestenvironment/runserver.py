#!python
<<<<<<< HEAD
#import sys
#sys.path.insert(0, '.')

from cloudtestenvironment import web_app as web_application
web_application.run(host='127.0.0.1', port=5000, debug=True)
=======
import sys
sys.path.insert(0, '.')

from cloudtestenvironment import app as application
application.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> 0c660dee2d2740666b6deb3a259c9fd87b1362eb
