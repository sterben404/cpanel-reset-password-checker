import os,sys,re
import requests
import ssl
import socket
import httplib
import urllib2
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[36m'
purple = '\033[35m'
reset = '\033[0m'
#initialize OS for display clear
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
pass
print(red+"""
                          .,---.
                        ,/XM#MMMX;,
                      -%##########M%,
                     -@######%  $###@=
      .,--,         -H#######$   $###M:
   ,;$M###MMX;     .;##########$;HM###X=
 ,/@##########H=      ;################+
-+#############M/,      %##############+
%M###############=      /##############:
H################      .M#############;.
@###############M      ,@###########M:.
X################,      -$=X#######@:
/@##################%-     +######$-
.;##################X     .X#####+,
 .;H################/     -X####+.
   ,;X##############,       .MM/
      ,:+$H@M#######M#$-    .$$=
           .,-=;+$@###X:    ;/=.
                  .,/X$;   .::,
                      .,    ..
""")
print(yellow+"""_______________________________
< Mass cPanel Reset Password Checker >
 -------------------------------""")
print(blue+"Author By Sterben404"+reset)
print(green+"List : http://site.com/"+reset)
def error():
	try:
		requests.post('http://www.google.com')
		open(sys.argv[1], 'rb')
	except requests.exceptions.ConnectionError:
		print(red+"[ - ]"+reset+" Tidak Ada Koneksi Internet")
		exit()
	except IOError:
		print(red+"[ - ]"+reset+" File Tidak Di Temukan!")
		exit()
	except IndexError:
		print(red+"[ - ]"+reset+" Usage : python2 file.py list.txt")
		exit()
error()
def main(url):
	try:
		urls = url+'/cpanel/'.strip()
		req = urllib2.Request(urls, headers={'User-Agent': 'Mozilla/5.0'})
		sites = urllib2.urlopen(req,timeout=6)
		print(urls)
		regex = re.findall('(?=://)(.*?\d)(?=/")', sites.read())
		for u in regex:
			find = urllib2.urlopen('https'+u+'/', timeout=6)
			if 'Reset Password' in find.read():
				print(url+green+' --> Active'+reset)
				with open('active.txt','ab') as active:
					active.write(urls+'\n')
					active.close()
			else:
				print(url+red+' --> Disable'+reset)
			pass
	except(urllib2.URLError,ssl.CertificateError,socket.error,httplib.InvalidURL):
			print(url+yellow+' --> Cpanel Not Found'+reset)
	except ValueError:
		pass
pass

lists = open(sys.argv[1], 'rb').read().splitlines()
t = ThreadPool(25)
t.map(main, lists)
t.close()
t.join()

if __name__ == '__main__': 
 
    print("Site cPanel Active :"+green+" active.txt")
    print(blue+"Sterben404 - EXI2T Cyber Team"+reset)
