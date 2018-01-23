#!/usr/bin/env python

import sys
import socket

host = {
       'servername1': ('127.0.0.1','127.0.0.2'), 
       'servername2': ('127.0.0.3')
}

ipaddr = socket.gethostbyname(sys.argv[1])

for server,ip in host.iteritems():
  if ipaddr in ip:
    print sys.argv[1],"got ip address",ipaddr,".It is in",server,"server."
