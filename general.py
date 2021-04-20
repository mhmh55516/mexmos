import os
import sys
import time , os
#from subprocess import Popen

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from lib.core import utils

from modules import subdomain
from modules import probing
from modules import formatting
from modules import fingerprint
from modules import stoscan
from modules import screenshot
from modules import linkfinding
from modules import ipspace
from modules import portscan
from modules import vulnscan
from modules import dirbscan
from modules import corscan

def handle(options):
    if utils.isFile(options.get('TARGET')):
        targets = utils.just_read(options.get('TARGET'), get_list=True)
        # loop through each target
        for target in targets:
            options['TARGET'] = target
            options['OUTPUT'] = target
            single_handle(options)
    else:
        single_handle(options)

def scan_ip_nmap(option):
	f = open('/root/.osmedeus/workspaces/'+option+'/portscan/formatted-'+option+'.txt', "r")
	for x in f:
		ipadd = x.split(';;ports|')[0].replace("ip_address|", "")
		portadd = x.split(';;ports|')[1]
		os.system("nmap '"+ipadd+"' -p '"+portadd+"' -Pn -sV -sC -A -oN '/root/.osmedeus/workspaces/"+option+"/portscan/nmap-"+option+".txt' --append-output --min-rate=1000 --max-retries=1")
		
def brute_subdomain(option):
    os.system("/root/go/bin/gobuster dns -d '{0}' -t 5000 -w '/root/Desktop/uploads/wordlist/sub_list_9.6M/all.txt' -o '/root/.osmedeus/workspaces/{0}/subdomain/force-{0}-gobuster.txt' && sed -i 's/Found: //g' 'force-{0}-gobuster.txt' && cat 'final-{0}.txt' 'force-{0}-gobuster.txt' | sort -u -o 'final-{0}.txt'".format(option))
def single_handle(options):
    subdomain.SubdomainScanning(options)
    brute_subdomain(options['TARGET'])
    probing.Probing(options)
    # formatting.Formatting(options)
    fingerprint.Fingerprint(options)
    stoscan.StoScan(options)
    screenshot.ScreenShot(options)
    linkfinding.LinkFinding(options)
    ipspace.IPSpace(options)
    portscan.PortScan(options)
    # vulnscan.VulnScan(options)
    #dirbscan.DirbScan(options)
    corscan.CORScan(options)
    scan_ip_nmap(options['TARGET'])
    os._exit(os.EX_OK)
