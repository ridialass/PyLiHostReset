# PyLiHostReset
Python-Linux-Host-Reset
Is a python script that reset the hostname and the user on a linux (Ubuntu, Debian) host.

# Use case
See the network map:
![Network_Map](https://user-images.githubusercontent.com/7754646/115961015-d0721b00-a514-11eb-82f1-7c857aed517d.JPG)


Pulling the IP addres of the host to know its localization (In which lan it belongs)
Fos example:
the network "Abeille" is 192.168.10.0/24 and "Baobab" has the network 192.168.20.0/24.
But can be modified for more sub-networks by triggering the If condition.

So with the third octet of the ip address we can know the domain of our host:
10 is Abeille and 20 is Baobab

From here we can set our hostname with the domain + the fourth octet as host number
192.168.10.13 will be Abeille13 
192.168.20.25 will be Baobab25

For the user we'll first look after an old user having the prefix "stagiaire".
If we find it, we are going to delete it before creating a new one with the fourth octet of the IP address
On 192.168.10.13 (Abeille13) we will create the account for "stagiaire13" having a default password. 
