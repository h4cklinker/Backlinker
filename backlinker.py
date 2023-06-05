import json
import requests
import re
import sys
import argparse


def add_backlinks(site):
    try:
        with open("urlbacklinks.json", "r") as file:
            data = json.loads(file.read())
            for backlink in data:
                url = backlink['url'].replace("h4link.duckdns.org", site)
                try:
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f"{site} => Backlink Eklendi ==> {url} status: {r.status_code}")
                    else:
                        print(f"{site} => Error adding backlink ==> {url} status: {r.status_code}")
                except KeyboardInterrupt:
                    sys.exit()
                except Exception as e:
                    print(f"{site} => Error adding backlink ==> {url} Exception: {str(e)}")
    except FileNotFoundError:
        print("urlbacklinks.json file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backlink Kasilcak Site")
    parser.add_argument("site", help="Website for backlink")
    args = parser.parse_args()

    print("""
            _ ____             _    _ _       _
           | |  _ \           | |  | (_)     | |
 _   _ _ __| | |_) | __ _  ___| | _| |_ _ __ | | _____ _ __
| | | | '__| |  _ < / _` |/ __| |/ / | | '_ \| |/ / _ \ '__|
| |_| | |  | | |_) | (_| | (__|   <| | | | | |   <  __/ |
 \__,_|_|  |_|____/ \__,_|\___|_|\_\_|_|_| |_|_|\_\___|_|
                                              H4-cklinker - wmdark.com
    """)

    add_backlinks(args.site)

