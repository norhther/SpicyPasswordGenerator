# SpicyPasswordGenerator
Password generator made with python with spicy features. Can be used to generate giantjson password files for testing purposes.

## Usage
```
  python3 spicyPasswordGenerator.py -h
  
  -s, -S         Use special letters for generating the password
  -c, -C         Use capital letters for generating the password
  -n, -N         Use numbers for generating the password
  --size SIZE    Indicates the size of the generated password, default = 10
  --save FILE    Saves the generated password in FILE, with json format. If the file exists, the passwords are
                 appended
  -d, --display  Display the generated passwords (not recommended with -it)
  --it IT        Iterates the passGenerator IT times, adding IT passwords to the database indicated. --store
                 has to be used with this command to indicate the file. If not, this argument is ignored.
```

## Performance
Generating a json with 1M passwords of size 100
  * Intel core i5 7th gen (laptop)
  * 8Gb RAM
  * Ubuntu 20.04 LTS
  ```
  norhther@norhther-ThinkPad-X1-Carbon-5th:~/Escritorio$ time ./spicyPassGenerator.py -scn --size 100 --save pass.txt --it 1000000
      real	0m23,416s
      user	0m22,221s
      sys	0m0,784s
```
