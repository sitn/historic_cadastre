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
      landscape: true
      backgroundPdf: 'file:///<%text>$</%text>{configDir}/A4_paysage.pdf'
      marginTop: 50
      items:
        - !map
          width: 810
          height: 470
          align:center
        - !columns
          absoluteX: 345
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
          absoluteX: 14
          absoluteY: 70
          width: 250
          items:
            - !text
              text: 'Cadastre: <%text>$</%text>{cadastre} - Plan n° <%text>$</%text>{no_plan}, <%text>$</%text>{type_plan}'
              fontSize: 8
              align: left
              vertAlign: top
        - !columns
          absoluteX: 14
          absoluteY: 40
          width: 200
          items:
            - !text
              text: 'Impression du : <%text>$</%text>{now dd.MM.yyyy HH:mm:ss}'
              fontSize: 8
              align: left
              vertAlign: top
        # Title
        - !columns
          absoluteX: 14
          absoluteY: 55
          width: 118
          items:
            - !text
              text: '<%text>$</%text>{title}'
              fontSize: 10
        # Comment
        - !columns
          absoluteX: 600
          absoluteY: 55
          width: 200
          items:
            - !text
              text: '<%text>$</%text>{comment}'
              fontSize: 7
              align: left
        # Scale
        - !columns
          absoluteX: 345
          absoluteY: 40
          width: 150
          items:
            - !text
              text: 'Échelle 1:<%text>$</%text>{scale}'
              fontSize: 9
              align: center

## the backslash tell mako To Not write a new line at the end
<%def name="title()">\
1 A4 paysage\
</%def>
