# -*- coding: utf-8 -*-
  #===========================================================================
  ${self.title()}:
  #===========================================================================
    metaData:
      title: '<%text>$</%text>{title}'

    #-------------------------------------------------------------------------
    mainPage:
      pageSize: A4
      rotation: true
      backgroundPdf: 'file:///<%text>$</%text>{configDir}/A4_portrait.pdf'
      marginTop: 69
      items:
        - !map
          width: 530
          height: 692
          align: center
        - !columns
          absoluteX: 221
          absoluteY: 55
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
              fontSize: 5
              labelDistance: 2
              barBgColor: #FFFFFF
        - !columns
          condition: showDescription
          absoluteX: 20
          absoluteY: 70
          width: 250
          items:
            - !text
              text: 'Cadastre: <%text>$</%text>{cadastre} - Plan n° <%text>$</%text>{no_plan}, <%text>$</%text>{type_plan}'
              fontSize: 8
              align: left
              vertAlign: top
        # Date
        - !columns
          absoluteX: 20
          absoluteY: 40
          width: 200
          items:
            - !text
              text: 'Impression du : <%text>$</%text>{now dd.MM.yyyy HH:mm:ss}'
              fontSize: 6
        # Title
        - !columns
          absoluteX: 20
          absoluteY: 55
          width: 118
          items:
            - !text
              text: '<%text>$</%text>{title}'
              fontSize: 10
        # Comment
        - !columns
          absoluteX: 434
          absoluteY: 55
          width: 118
          items:
            - !text
              text: '<%text>$</%text>{comment}'
              fontSize: 7
        # Scale
        - !columns
          absoluteX: 258
          absoluteY: 40
          width: 150
          items:
            - !text
              text: 'Échelle 1:<%text>$</%text>{scale}'
              fontSize: 9

## the backslash tell mako To Not write a new line at the end
<%def name="title()">\
2 A4 portrait\
</%def>

<%def name="block_logo()">
            - !text
              text: 'Put your logo here'
              fontSize: 6
</%def>

<%def name="block_text_misc()">
            - !text
              text: 'Here some miscellaneous text'
              fontSize: 6
</%def>
