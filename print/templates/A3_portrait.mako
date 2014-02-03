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
          width: 750
          height: 989
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
          absoluteX: 20
          absoluteY: 55
          width: 200
          items:
            - !text
              text: 'Impression du : <%text>$</%text>{now dd.MM.yyyy HH:mm:ss}'
              fontSize: 6
        - !columns
          absoluteX: 20
          absoluteY: 78
          width: 195
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
4 A3 portrait\
</%def>

<%def name="block_logo()">
        - !columns
          absoluteX: 648
          absoluteY: 88
          width: 124
          config:
            cells:
              - padding: 1
          items:
            - !text
              text: 'Put your logo here'
              fontSize: 10
</%def>

<%def name="block_text_misc()">
        - !columns
          absoluteX: 51
          absoluteY: 104
          width: 250
          config:
            cells:
              - padding: 8
          items:
            - !text
              text: 'Here some miscellaneous text'
              fontSize: 10
</%def>
## end of block specific code
