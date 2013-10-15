import sys
import json
import argparse
from pprint import pprint
from qazar import Provisioner

if not sys.stdin.isatty():
    json_data = sys.stdin.read()
else:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-e', '--environment', help='read environment from argument')
    args = parser.parse_args()
    if args.environment:
        with open(args.environment, 'rb') as json_file:
            json_data = json_file.read()
        
env = json.loads(json_data)
pprint(env)

p = Provisioner()
p.provision(env)



