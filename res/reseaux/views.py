from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run, PIPE
import sys
import requests
import telnetlib

def home_page(request):
    return render(request, 'home.html')

def form1_page(request):
    return render(request, 'form1.html')

def form2_page(request):
    return render(request, 'form2.html')

def RouterConf(request):
    ip = request.POST.get('ip')
    mask = request.POST.get('mask')
    ip2= request.POST.get('ip2')
    mask2= request.POST.get('mask2')
    id_vlan1= request.POST.get('idv1')
    id_vlan2= request.POST.get('idv2')
    HOST = "192.168.17.133"
    user = "admin"
    password = "admin123"



    tn= telnetlib.Telnet()
    tn.open(HOST)


    tn.write(user.encode('ascii')+b"\n" )
    if password:
        tn.write(password.encode ('ascii')+b"\n" )

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    tn.write(b"interface fastEthernet 0/0\n")
    tn.write(b"no shutdown\n")
    tn.write(b"interface fastEthernet 0/0.1\n")
    tn.write(b"encapsulation dot1Q "+id_vlan1.encode('ascii') + b" \n")
    tn.write(b"ip address "+ ip.encode('ascii') + b" " + mask.encode('ascii') + b"\n")
    tn.write(b"interface fastEthernet 0/0.2\n")
    tn.write(b"encapsulation dot1Q "+id_vlan2.encode('ascii') + b" \n")
    tn.write(b"ip address "+ ip2.encode('ascii') + b" " + mask2.encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")


    print (tn.read_all().decode('ascii'))

    tn.close()
    
    return render(request, 'form1.html')
    

def SwitchConf(request):
    name_vlan1= request.POST.get('name1')
    id_vlan1= request.POST.get('id1')
    name_vlan2= request.POST.get('name2')
    id_vlan2= request.POST.get('id2')
    HOST2 = "192.168.17.135"
    user2 = "admin"
    password2 = "admin123"


    tn2= telnetlib.Telnet()
    tn2.open(HOST2)

    tn2.write(user2.encode('ascii')+b"\n" )
    if password2:
        tn2.write(password2.encode ('ascii')+b"\n" )

    tn2.write(b"enable\n")
    tn2.write(b"cisco\n")
    tn2.write(b"conf t\n")
    tn2.write(b"vlan "+id_vlan1.encode('ascii') + b" \n")
    tn2.write(b"name "+ name_vlan1.encode('ascii') +b" \n")
    tn2.write(b"vlan "+id_vlan2.encode('ascii') + b" \n")
    tn2.write(b"name "+ name_vlan2.encode('ascii') +b" \n")
    tn2.write(b"interface ethernet 0/1\n")
    tn2.write(b"switchport access vlan " +id_vlan1.encode('ascii') + b" \n" )
    tn2.write(b"interface ethernet 0/2\n")
    tn2.write(b"switchport access vlan " +id_vlan2.encode('ascii') + b" \n" )
    tn2.write(b"interface ethernet 0/0\n")
    tn2.write(b"switchport trunk encapsulation dot1q\n")
    tn2.write(b"switchport mode trunk\n")
    tn2.write(b"end\n")
    tn2.write(b"exit\n")

    print (tn2.read_all().decode('ascii'))

    tn2.close()

    return render(request, 'form2.html')