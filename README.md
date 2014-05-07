DRTV
====

A command-line interface to download videos from http://www.dr.dk/tv/

Installation
---------
**Ubuntu**

    sudo apt-get install python3.3
    sudo apt-get install wget
    wget https://github.com/Fr3d-/DRTV/raw/master/DRTV.py
    sudo chmod +x DRTV.py
    sudo mv DRTV.py /usr/bin/
    
Syntax
---------
    DRTV.py url [quality]
    
    Available qualities:
		0 - Best
		1 - High
		2 - Average
		3 - Low
**Example**

    DRTV.py www.dr.dk/tv/se/monte-carlo-elsker-usa/monte-carlo-elsker-usa-8-8 0
Requirements
---------
* Python 3.3.2
* GNU Wget 1.14
