#!/usr/bin/env python

URL="http://www.pythonchallenge.com/pc/def/0.html"

def main():
	print(URL.replace("0", str(2**38)))

if __name__ == '__main__':
	main()