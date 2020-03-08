# bgp.tool
A quick Python wrapper for searching on https://bgp.tools  

## BGP Search

- Requires "BeautifulSoup"
```
pip3 install bs4
```
**Usage**
```
bgp_search.py [-h] -s SEARCH

A small script which allows to search for netblocks on bgp.tools

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        search string, e.g. "DoD"
```

**Output**
```
[!] Result | IPv4

	+ 156.112.142.0/24    (DoD Network Information Center)
	+ 199.9.64.0/24	      (DoD Network Information Center)
	+ 156.112.128.0/23    (DoD Network Information Center)
	+ 156.112.84.0/24     (DoD Network Information Center)
	+ 199.9.86.0/24       (DoD Network Information Center)
	+ 199.9.71.0/24	      (DoD Network Information Center)
...
```
