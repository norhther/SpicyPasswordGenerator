#!/usr/bin/python3
import argparse
import random
import string
import json
import pathlib
import hashlib
from datetime import datetime

__author__ = "norhther"

def generate(parser_results):
    words_to_use = string.ascii_lowercase
    if parser_results.use_special:
        words_to_use += string.punctuation
    if parser_results.use_capital:
        words_to_use += string.ascii_uppercase
    if parser_results.use_numbers:
        words_to_use += string.digits

    password = "".join(random.choices(words_to_use, k=parser_results.size))
    if parser_results.display:
        print(password)
    if parser_results.file is not None:
        it = 1
        if parser_results.it:
            it = int(parser_results.it)
        p = pathlib.Path(parser_results.file)
        if not p.is_file():
            res = {}
            if parser_results.display:
                print("index: 1, pwd: {}".format(password))
            res["passwords"] = []
            res["passwords"].append({
                "id" : 1,
                "size" : parser_results.size,
                "created" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "password" : password,
                "md5" : hashlib.new("md5", password.encode('utf-8')).hexdigest(),
                "sha256" : hashlib.new("sha256", password.encode('utf-8')).hexdigest(),
                "sha512" : hashlib.new("sha512", password.encode('utf-8')).hexdigest(),
                "sha3_224" : hashlib.new("sha3_224", password.encode('utf-8')).hexdigest(),
                "sha3_512" : hashlib.new("sha3_512", password.encode('utf-8')).hexdigest(),
                "blake2s" : hashlib.new("blake2s", password.encode('utf-8')).hexdigest(),
                "blake2b" : hashlib.new("blake2b", password.encode('utf-8')).hexdigest()
            })
            it -= 1
            with open(parser_results.file, "w") as f:
                json.dump(res, f, indent = 4)
        res = None
        with open(parser_results.file, "r") as f:
            res = json.load(f)
        with open(parser_results.file, "w") as f:
            for _ in range(0, it):
                password = "".join(random.choices(words_to_use, k=parser_results.size))
                if parser_results.display:
                    print("index: {}, pwd: {}".format(res["passwords"][-1]["id"] + 1, password))
                res["passwords"].append({
                    "id": res["passwords"][-1]["id"] + 1,
                    "size" : parser_results.size,
                    "created" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "password" : password,
                    "sha256" : hashlib.new("sha256", password.encode('utf-8')).hexdigest(),
                    "sha512" : hashlib.new("sha512", password.encode('utf-8')).hexdigest(),
                    "sha3_224" : hashlib.new("sha3_224", password.encode('utf-8')).hexdigest(),
                    "sha3_512" : hashlib.new("sha3_512", password.encode('utf-8')).hexdigest(),
                    "blake2s" : hashlib.new("blake2s", password.encode('utf-8')).hexdigest(),
                    "blake2b" : hashlib.new("blake2b", password.encode('utf-8')).hexdigest()
                })
            f.write(json.dumps(res, indent = 4))
                

    
def buildParser():
    parser = argparse.ArgumentParser(
        description="Random passwords generator with spicy features, by norhther."
    )
    parser.add_argument("-s", "-S", action = "store_true", dest = "use_special", 
                        help = "Use special letters for generating the password",
                        default = False)

    parser.add_argument("-c", "-C", action = "store_true", dest = "use_capital", 
                        help = "Use capital letters for generating the password",
                        default = False)

    parser.add_argument("-n", "-N", action = "store_true", dest = "use_numbers", 
                        help = "Use numbers for generating the password",
                        default = False)

    parser.add_argument("--size", action = "store", dest = "size", type = int,
                        help = "Indicates the size of the generated password, default = 10",
                        default = 10)

    parser.add_argument("--save", action = "store", dest = "file",
                        help = """Saves the generated password in FILE, with json format.
                        If the file exists, the passwords are appended""",
                        default = None) 

    parser.add_argument("-d", "--display", action = "store_true", dest = "display",
                        help = "Display the generated passwords (not recommended with -it)",
                        default = None) 

    parser.add_argument("--it", action = "store", dest = "it",
                        help = """Iterates the passGenerator IT times, adding IT passwords
                        to the database indicated. --store has to be used with this command
                        to indicate the file. If not, this argument is ignored.""",
                        default = None) 
    return parser   



if __name__ == "__main__":
    results = buildParser().parse_args()
    generate(results)