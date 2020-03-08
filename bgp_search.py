# v.0.1 - Written by SI9INT (https://twitter.com/si9int) | 2020-03
#!/usr/bin/env python3
import requests, argparse
from bs4 import BeautifulSoup as bs

ipv4 = []
ipv6 = []

def search(term):
    # https://bgp.tools
    result = requests.get('https://bgp.tools/search?q=' + term).text
    html = bs(result, 'html.parser')
    
    for tr in html.find_all('tr'):
        try:
            inetnum = tr.find('a').text
            desc = tr.find_all('td', {'class' : 'nowrap'})[1].text
            cc = tr.find_all('td', {'class' : 'nowrap'})[0].img.get('alt')
            
            if not inetnum.startswith('AS'):
                if '::' in inetnum:
                    ipv6.append((inetnum, desc, cc))
                else:
                    ipv4.append((inetnum, desc, cc))
        except AttributeError:
            pass
        
    print('[!] Result | \033[93mIPv4\033[0m\n')
    
    for inetnum in ipv4:
        print('\t+ [{}] {}\t ({})'.format(inetnum[2], inetnum[0], inetnum[1]))
        
    print('\n[!] Result | \033[93mIPv6\033[0m\n')
    
    for inetnum in ipv6:
        print('\t+ [{}] {}\t ({})'.format(inetnum[2], inetnum[0], inetnum[1]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A small script which allows to search for netblocks on bgp.tools')
    parser.add_argument('-s', '--search', required=True, help='search string, e.g. "DoD"')
    
    args = parser.parse_args()
    
    if args.search:
        print('[-] Requesting data for {} ..'.format(args.search))      
        search(args.search)
        
    print('\n[-] Finished! Good bye ..')
