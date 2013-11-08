import unittest
import subprocess

class TestMain(unittest.TestCase):
    """Tests __main__.py's stdin and argparse"""
    def test_from_stdin(self):
        test_json = '{"charms": [{"name": "selenium"}, {"name": "jenkins"}]}'
        command = "cat test.json | python __main__.py"
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,).stdout.read()
        self.assertEqual(output, test_json)
    def test_from_arg(self):
        test_json = '{"charms": [{"name": "selenium"}, {"name": "jenkins"}]}'
        command = "python __main__.py --environment test.json"
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,).stdout.read()
        self.assertEqual(output, test_json)
        
