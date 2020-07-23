#!/usr/bin/env python
import requests
import os
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def main():
    token = os.environ["NETBOX_TOKEN"]
    token = "Token {}".format(token)
    url = "https://netbox.lasthop.io/api/dcim/devices"
    http_headers = {"accept": "application/json; version=2.4;", "authorization": token}
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    print()
    pprint(response)
    print()


if __name__ == "__main__":
    main()
