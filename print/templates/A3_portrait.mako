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
          condition: showMap
          width: 750
          height: 989
          align: center
        - !columns
          condition: showAttr
          absoluteX: 20
          absoluteY: 1087
          width:  800
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
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col0}'
                        fontSize: 5
                        backgroundColor: #ffffff
                        borderColorBottom: #ffffff
                        borderWidthBottom: 1
                col1:
                  header: !text
                    text: '<%text>$</%text>{col1}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col1}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col2:
                  header: !text
                    text: '<%text>$</%text>{col2}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col2}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col3:
                  header: !text
                    text: '<%text>$</%text>{col3}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col3}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col4:
                  header: !text
                    text: '<%text>$</%text>{col4}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col4}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col5:
                  header: !text
                    text: '<%text>$</%text>{col5}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col5}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col6:
                  header: !text
                    text: '<%text>$</%text>{col6}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col6}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col7:
                  header: !text
                    text: '<%text>$</%text>{col7}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col7}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col8:
                  header: !text
                    text: '<%text>$</%text>{col8}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col8}'
                        fontSize: 5
                        backgroundColor: #ffffff
                col9:
                  header: !text
                    text: '<%text>$</%text>{col9}'
                    fontSize: 6
                    backgroundColor: #ffffff
                  cell: !columns
                    items:
                      - !text
                        text: '<%text>$</%text>{col9}'
                        fontSize: 5
                        backgroundColor: #ffffff
        - !columns
          condition: showScale
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
          condition: showNorth
          absoluteX: 550
          absoluteY: 78
          width: 30
          items:
            - !image
              align: center
              maxWidth: 15
              url: 'file:///<%text>$</%text>{configDir}/north.png'
              rotation: '<%text>$</%text>{rotation}'
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
          condition: showScalevalue
          absoluteX: 365
          absoluteY: 55
          width: 195
          items:
            - !text
              text:  'Échelle 1:<%text>$</%text>{scale}'
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
