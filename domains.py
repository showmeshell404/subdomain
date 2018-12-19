# coding=utf-8
import os
import sys
import argparse
from utils.Crt import Crt
from utils.ilink import ILink
from common import save_result, read_json
from utils.brutedns import BruteDns

domain = 'ichunqiu.com'


def run(args):
    domain = args.domain
    if not domain:
        print "Usage:domains,py -d test.com"
        sys.exit(1)
    outfile = '{0}.log'.format(domain)

    script_path = os.path.dirname(os.path.abspath(__file__))
    _cache_path = os.path.join(script_path, 'result/{0}'.format(domain))
    if not os.path.exists(_cache_path):
        os.makedirs(_cache_path, 0777)

    print '[*]Starting CRT fetch........'
    result = Crt(domain=domain).run()
    _cache_file = os.path.join(_cache_path, 'crt.json')
    save_result(_cache_file, result)
    print '\t [-]Fetch Complete | Found {}'.format(len(result))

    print '[*]Starting ILink fetch........'
    result = ILink(domain=domain).run()
    _cache_file = os.path.join(_cache_path, 'ilink.json')
    save_result(_cache_file, result)
    print '\t [-]Fetch Complete | Found {}'.format(len(result))

    print '[*]Starting Brute........'
    result = BruteDns(domain=domain).run()
    _cache_file = os.path.join(_cache_path, 'brute.json')
    save_result(_cache_file, result)
    print '\n\t [-]Fetch Complete | Found {}'.format(len(result))

    _cache_files = ['crt.json', 'ilink.json', 'brute.json']

    subdomains = []

    for file in _cache_files:
        _cache_file = os.path.join(_cache_path, file)
        json_data = read_json(_cache_file)
        if json_data:
            subdomains.extend(json_data)

    subdomains = list(set(subdomains))

    _result_file = os.path.join(script_path, outfile)
    save_result(_result_file, subdomains)

    print '\n[*]{0} {1} subdomains \n\tsave to {2}'.format(domain, len(subdomains), _result_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Domain Scan Ver:1.0")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    args = parser.parse_args()
    print '''
 _                   _   _ 
| |    _____   _____| | | |
| |   / _ \ \ / / _ \ | | |
| |__| (_) \ V /  __/ |_| |
|_____\___/ \_/ \___|\___/ 
                           

    '''
    print ' Author:ShowMeShell Version=1.0'

    try:
        run(args)
    except KeyboardInterrupt:
        sys.exit(1)
