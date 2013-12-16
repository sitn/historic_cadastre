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
          condition: showMap
          width: 530
          height: 692
          align: center
        - !columns
          condition: showAttr
          absoluteX: 20
          absoluteY: 768
          width: 522
          config:
              borderWidth: 0.2
              borderColor: black
          items:
            - !attributes
              source: table
              tableConfig: 
                cells: 
                  - padding: 2
                    backgroundColor: #ffffff
                    borderWidthRight: 1
                    borderWidthBottom: 1
                    borderColor: black  
              columnDefs:
                col0:
                  header: !text
                    text: '<%text>$</%text>{col0}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col0}'
                        fontSize: 8
                        backgroundColor: #ffffff
                        borderColorBottom: #ffffff
                        borderWidthBottom: 1
                col1:
                  header: !text
                    text: '<%text>$</%text>{col1}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col1}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col2:
                  header: !text
                    text: '<%text>$</%text>{col2}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col2}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col3:
                  header: !text
                    text: '<%text>$</%text>{col3}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col3}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col4:
                  header: !text
                    text: '<%text>$</%text>{col4}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col4}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col5:
                  header: !text
                    text: '<%text>$</%text>{col5}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col5}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col6:
                  header: !text
                    text: '<%text>$</%text>{col6}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col6}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col7:
                  header: !text
                    text: '<%text>$</%text>{col7}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col7}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col8:
                  header: !text
                    text: '<%text>$</%text>{col8}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col8}'
                        fontSize: 8
                        backgroundColor: #ffffff
                col9:
                  header: !text
                    text: '<%text>$</%text>{col9}'
                    font: Helvetica-Bold
                    fontSize: 8
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col9}'
                        fontSize: 8
                        backgroundColor: #ffffff
        - !columns
          condition: showScale
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
          condition: showNorth
          absoluteX: 389
          absoluteY: 55
          width: 30
          items:
            - !image
              align: center
              maxWidth: 15
              url: 'file:///<%text>$</%text>{configDir}/north.png'
              rotation: '<%text>$</%text>{rotation}'
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
          condition: showScalevalue
          absoluteX: 258
          absoluteY: 40
          width: 150
          items:
            - !text
              text: 'Échelle 1:<%text>$</%text>{scale}'
              fontSize: 9
    lastPage:
      items:
         - !columns
          condition: legends
          absoluteX: 51
          absoluteY: 808
          width: 511
          items:
            - !legends
              inline: false
              defaultScale: 0
              maxHeight: 400
              maxWidth: 250
              maxIconHeight: 0
              maxIconWidth: 0
              columnMargin: 10
              classIndentation: 3
              classSpace: 5
              backgroundColor: white
              layerFontSize: 9

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
