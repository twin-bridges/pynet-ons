#!/usr/bin/env python
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def main():
    url = "https://netbox.lasthop.io/api/"
    http_headers = {"accept": "application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)

    print()
    pprint(dir(response))
    print()
    pprint(response.text)
    print()
    pprint(response.json())
    print()
    print(response.ok)
    print()
    print(response.status_code)


if __name__ == "__main__":
    main()
