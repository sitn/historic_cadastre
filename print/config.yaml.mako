# -*- coding: utf-8 -*-
#===========================================================================
dpis: [254]

#===========================================================================
# the allowed scales
#===========================================================================
scales:
  - 50
  - 100
  - 200
  - 500
  - 1000
  - 2000
  - 2500
  - 5000
  - 10000
  - 25000
  - 50000
  - 100000
  - 200000
  - 500000

#===========================================================================
# the list of allowed hosts
#===========================================================================
hosts:
  - !localMatch
    dummy: true
  - !dnsMatch
    host: ${host}
    port: 80 
  - !dnsMatch
    host: ${host}
    port: 80
  - !dnsMatch
    host: ${host}
    port: ${waitress_port}
  - !dnsMatch
    host: ${proxy_host}
    port: 80

localHostForward:
    from:
        - ${print_localhost_forward_from}
        ${print_localhost_forward_from_ssl}
    https2http: True

#===========================================================================
# the output filename
#===========================================================================
outputFilename: impression_sitn

#===========================================================================
# supported output formats
#===========================================================================
formats:
  - "pdf"
  - "png"

globalParallelFetches: 1

layouts:

## A4 portrait default
<%include file="templates/A4_portrait.mako" />

## A4 landscape default
<%include file="templates/A4_landscape.mako" />

## A3 landscape default
<%include file="templates/A3_landscape.mako" />

## A3 portrait default
<%include file="templates/A3_portrait.mako" />
