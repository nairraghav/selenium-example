import argparse
import subprocess

def parse_arguments():
    parser = argparse.ArgumentParser(description='Parsing arguments for running Selenium tests')
    parser.add_argument('-b', '--browser', default='chrome', help='Indicates the browser we want to use for tests')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    subprocess.run(["pytest", "tests/"])