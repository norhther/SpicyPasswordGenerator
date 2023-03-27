#!/usr/bin/python3
import argparse
import json
import pathlib
import random
import hashlib
import string
from datetime import datetime

__author__ = "norhther"

def generate(parser_results):
    words_to_use = string.ascii_lowercase
    if parser_results.use_special:
        words_to_use += string.punctuation
        # do not use the following characters: " ' ` \ /
        char = '"\'`\\/'
        table = str.maketrans(char, len(char) * '\0')
        words_to_use = words_to_use.translate(table)

    if parser_results.use_capital:
        words_to_use += string.ascii_uppercase
    if parser_results.use_numbers:
        words_to_use += string.digits

    password = "".join(random.choices(words_to_use, k=parser_results.size))
    if parser_results.display:
        print(password)

    if parser_results.file is not None:
        it = int(parser_results.it) if parser_results.it else 1
        p = pathlib.Path(parser_results.file)
        res = {"passwords": []}

        if p.is_file():
            with open(parser_results.file, "r") as f:
                res = json.load(f)

        for i in range(it):
            password = "".join(random.choices(words_to_use, k=parser_results.size))

            if parser_results.display:
                print(f"index: {len(res['passwords']) + 1}, pwd: {password}")

            password_hash = {
                algorithm: hashlib.new(algorithm, password.encode('utf-8')).hexdigest()
                for algorithm in ["md5", "sha256", "sha512", "sha3_224", "sha3_512", "blake2s", "blake2b"]
            }

            res["passwords"].append({
                "id": len(res["passwords"]) + 1,
                "size": parser_results.size,
                "created": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "password": password,
                **password_hash
            })

        with open(parser_results.file, "w") as f:
            json.dump(res, f, indent=4)
                

    
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