#!/usr/bin/python3.6
import os
import re
import urllib
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"


urllib._urlopener = AppURLopener()


def downloader(image_url, full_image_name):
    if not full_image_name:
        print('Url does not valid')
    else:
        urllib._urlopener.retrieve(image_url, full_image_name)
    exit()


def validateUrl():
    image_url = input("Enter image url? ")
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, image_url) is not None:
        image_name = input("Enter image name? ")
        cwd = os.getcwd()
        full_image_name = cwd + '/pictures/' + str(image_name) + '.jpg'
        downloader(image_url, full_image_name)
    else:
        print("Invalid URL: " + image_url)
        validateUrl()


def main():
    print('Image Downloader')
    validateUrl()


if __name__ == "__main__":
    main()
