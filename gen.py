import os
import sys
import time
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
'''
def scan_ip_nmap(option):
	f = open('/root/.osmedeus/workspaces/'+option+'/portscan/formatted-'+option+'.txt', "r")
	for x in f:
		ipadd = x.split(';;ports|')[0].replace("ip_address|", "")
		portadd = x.split(';;ports|')[1]
		os.system("nmap '"+ipadd+"' -p '"+portadd+"' -Pn -sV -sC -A -oN '/root/.osmedeus/workspaces/"+option+"/portscan/nmap-"+option+".txt' --append-output --min-rate=1000 --max-retries=1")
'''		
def brute_subdomain(option):
    os.system("/root/go/bin/gobuster -m dns -u '{0}' -t 5000 -w '/root/all.txt' -o '/root/.osmedeus/workspaces/{0}/subdomain/force-{0}-gobuster.txt'".format(option))
    os.system("python3 /root/get_subx.py '{0}'".format(option))
    os.system("sed -i 's/Found: //g' '/root/.osmedeus/workspaces/{0}/subdomain/force-{0}-gobuster.txt' && cat '/root/.osmedeus/workspaces/{0}/subdomain/final-{0}.txt' '/root/.osmedeus/workspaces/{0}/subdomain/force-{0}-gobuster.txt' | tr '[A-Z]' '[a-z]' | sort -u -o '/root/.osmedeus/workspaces/{0}/subdomain/final-{0}.txt'".format(option))
    os.system("ssh 'port@last-one.duckdns.org' -o 'StrictHostKeyChecking no' -o ServerAliveInterval=60 -i '/tmp/516.pem' -f \"find /root/chaos/ -type f -name '{0}*' -exec cat {{}} + > /home/port/sent/{0}.txt\"".format(option))
    os.system("rsync -avz -e \"ssh -o 'StrictHostKeyChecking no' -i '/tmp/516.pem'\" port@last-one.duckdns.org:\"/home/port/sent/{0}.txt\" '/root/.osmedeus/workspaces/{0}/subdomain/chaos-{0}.txt'".format(option))
    os.system("cat '/root/.osmedeus/workspaces/{0}/subdomain/final-{0}.txt' '/root/.osmedeus/workspaces/{0}/subdomain/chaos-{0}.txt' | tr '[A-Z]' '[a-z]' | sort -u -o '/root/.osmedeus/workspaces/{0}/subdomain/final-{0}.txt'".format(option))
    os.system("cat '/root/.osmedeus/workspaces/{0}/subdomain/final-{0}.txt' | grev -v \"@\" > '/root/.osmedeus/workspaces/{0}/subdomain/final-{0}.txt'".format(option))
def single_handle(options):
    subdomain.SubdomainScanning(options)
    brute_subdomain(options['TARGET'])
    probing.Probing(options)
    # formatting.Formatting(options)
    fingerprint.Fingerprint(options)
    #stoscan.StoScan(options)
    screenshot.ScreenShot(options)
    linkfinding.LinkFinding(options)
    ipspace.IPSpace(options)
    #portscan.PortScan(options)
    # vulnscan.VulnScan(options)
    # dirbscan.DirbScan(options)
    #corscan.CORScan(options)
    # scan_ip_nmap(options['TARGET'])
    os._exit(os.EX_OK)
