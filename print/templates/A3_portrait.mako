# -*- coding: utf-8 -*-
  #===========================================================================
  ${self.title()}:
  #===========================================================================
    metaData:
      title: '<%text>$</%text>{title}'

    #-------------------------------------------------------------------------
    mainPage:
      pageSize: A3
      rotation: true
      backgroundPdf: 'file:///<%text>$</%text>{configDir}/A3_portrait.pdf'
      marginTop: 76
      items:
        - !map
          width: 785
          height: 1020
          align: center
        - !columns
          absoluteX: 313
          absoluteY: 78
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
          absoluteX: 27
          absoluteY: 93
          width: 400
          items:
            - !text
              text: '<%text>$</%text>{txtDescription}'
              fontSize: 8
              align: left
              vertAlign: top
        - !columns
          absoluteX: 27
          absoluteY: 55
          width: 200
          items:
            - !text
              text: 'Impression du : <%text>$</%text>{now dd.MM.yyyy HH:mm:ss}'
              fontSize: 6
        - !columns
          absoluteX: 20
          absoluteY: 78
          width: 200
          items:
            - !text
              text: '<%text>$</%text>{title}'
              fontSize: 9
        - !columns
          absoluteX: 614
          absoluteY: 78
          width: 195
          items:
            - !text
              text: '<%text>$</%text>{comment}'
              fontSize: 9
        - !columns
          absoluteX: 365
          absoluteY: 55
          width: 195
          items:
            - !text
              text:  'Échelle 1:<%text>$</%text>{scale}'
              fontSize: 9

## end of global template code
## start of block specific code

## the backslash tell mako To Not write a new line at the end
<%def name="title()">\
3 A3 portrait\
</%def>
