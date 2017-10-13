# -*- coding: utf-8 -*-
  #===========================================================================
  ${self.title()}:
  #===========================================================================
    metaData:
      title: '<%text>$</%text>{title}'

    #-------------------------------------------------------------------------
    mainPage:
      pageSize: A2
      rotation: true
      backgroundPdf: 'file:///<%text>$</%text>{configDir}/A2_portrait.pdf'
      marginTop: 83
      items:
        - !map
          width: 1130
          height: 1486
          align: center
        - !columns
          absoluteX: 524
          absoluteY: 85
          width: 500
          items:
            - !scalebar
              maxSize: 200
              type: bar_sub
              intervals: 5
              textDirection: up
              barDirection: up
              align: left
              barSize: 3
              lineWidth: 0.3
              fontSize: 8
              labelDistance: 4
              barBgColor: #FFFFFF
        - !columns
          condition: showDescription
          absoluteX: 30
          absoluteY: 93
          width: 400
          items:
            - !text
              text: '<%text>$</%text>{txtDescription}'
              fontSize: 10
              align: left
              vertAlign: top
        - !columns
          absoluteX: 30
          absoluteY: 55
          width: 200
          items:
            - !text
              text: 'Impression du : <%text>$</%text>{now dd.MM.yyyy HH:mm:ss}'
              fontSize: 8
        - !columns
          absoluteX: 30
          absoluteY: 78
          width: 195
          items:
            - !text
              text: '<%text>$</%text>{title}'
              fontSize: 11
        - !columns
          absoluteX: 814
          absoluteY: 78
          width: 250
          items:
            - !text
              text: '<%text>$</%text>{comment}'
              fontSize: 11
        - !columns
          absoluteX: 1080
          absoluteY: 55
          width: 195
          items:
            - !text
              text:  'Échelle 1:<%text>$</%text>{scale}'
              fontSize: 11

## end of global template code
## start of block specific code

## the backslash tell mako To Not write a new line at the end
<%def name="title()">\
5 A2 portrait\
</%def>

