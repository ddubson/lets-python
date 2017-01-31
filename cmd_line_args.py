import argparse

parser = argparse.ArgumentParser(description="This is a description.")
parser.add_argument("-i", type=str, help="Help parameter", required=True)
parser.add_argument("-o", type=str, help="Optional", required=False)
cmdargs = parser.parse_args()
print(cmdargs)