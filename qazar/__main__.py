import sys
import json
import argparse
from provisioner import Provisioner

if not sys.stdin.isatty():
    env_obj = json.loads(sys.stdin.read())
else:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-e', '--environment', help='read environment from argument')
    args = parser.parse_args()
    if args.environment:
        with open(args.environment, 'rb') as env_file:
            env_obj = json.loads(env_file.read())

sys.stdout.write(json.dumps(env_obj)) #used for testing
p = Provisioner()
p.provision(env=env_obj)
