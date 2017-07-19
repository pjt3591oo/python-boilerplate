#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="package를 생성")
parser.add_argument("-p", help="생성할 패키지 명")
parser.add_argument("--package", help="생성할 패키지 명")
args = parser.parse_args()

print(args)