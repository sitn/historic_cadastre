# -*- coding: utf-8 -*-
#===========================================================================
dpis: [254]

#===========================================================================
# the allowed scales
#===========================================================================
scales:
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
    host: localhost
    port: 80 
  - !dnsMatch
    host: localhost
    port: 80
  - !dnsMatch
    host: localhost
    port: 6543
  - !dnsMatch
    host: sitn.ne.ch
    port: 80

localHostForward:
    from:
        - localhost
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
<%include file="/A4_portrait.mako" />

## A4 landscape default
<%include file="/A4_landscape.mako" />

## A3 landscape default
<%include file="/A3_landscape.mako" />

## A3 portrait default
<%include file="/A3_portrait.mako" />