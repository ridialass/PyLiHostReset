#!/usr/bin/python3

import socket
import subprocess
import os
import sys
import shutil
import netifaces

'''
Retrieving the IP address
''' 
iface = "enp0s3"
def get_ip_address(iface):
	ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
	print("The host IP address is: "+ ip)
	return(ip)
'''
Get the two last bits of IP by converting it into list
'''
ip4 = get_ip_address(iface)
li = list(ip4.split("."))
numh = li[-1]
numd = li[2]

def set_hostname(numd):
	'''
	Updating the /etc/hosname file
	'''
	if(numd == "0"):
		n_hostn = ("abeille" + numh)
		with open("/etc/hostname", "w") as f:
			f.write(n_hostn)
		return n_hostn
	elif(numd == "122"):
		n_hostn = ("baobab" + numh)
		with open("/etc/hostname", "w") as f:
			f.write(n_hostn)
		return n_hostn
	else:
		print("This IP address is not in your domain.")
		sys.exit()

new_hostname = set_hostname(numd)


def set_hosts(new_hostname):
	'''
	Updating the /etc/hosts file
	'''
	with open("/etc/hosts", "w") as f:
		f.write("127.0.0.1\tlocalhost\n")
		f.write(ip4 + "\t" + new_hostname + "\n")
	print("The new hostname is: " + new_hostname)


def get_users():
	'''
	Looking for an existing user to be deleted
	'''
	users = []
	src = r"/etc/passwd"
	dst = r"/tmp/users.txt"
	shutil.copyfile(src, dst)
	with open(dst, "r") as f:
		for line in f:
			words = users.append(line.split(":x:")[0])
	word = "stagiaire"
	old_user = [x for x in users if x.startswith(word)]
	if len(old_user):
		account = old_user[0]
		subprocess.run(['userdel', '-r', account])
		print("The user "+ account +" has been deleted.")
	else:
		print("No Stagiare account found.")


def add_user():
	'''	
	Creating a user with default password
	'''
	username = ("stagiaire" + numh)
	password = ("Password")
	subprocess.run(['useradd', '-mp', password, username])
	print("The new user created is: " + username)

if __name__ == '__main__':
	get_ip_address(iface)
	set_hostname(numd)
	set_hosts(new_hostname)
	get_users()
	add_user()
