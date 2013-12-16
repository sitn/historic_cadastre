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
      landscape: true
      backgroundPdf: 'file:///<%text>$</%text>{configDir}/A3_paysage.pdf'
      marginTop: 62
      items:
        - !map
          condition: showMap
          width: 1146
          height: 690
          align:center
        - !columns
          condition: showAttr
          absoluteX: 28
          absoluteY: 764
          width: 1135
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
          absoluteX: 488
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
          absoluteX: 778
          absoluteY: 78
          width: 30
          items:
            - !image
              align: center
              maxWidth: 15
              url: 'file:///<%text>$</%text>{configDir}/north.png'
              rotation: '<%text>$</%text>{rotation}'
        - !columns
          absoluteX: 23
          absoluteY: 50
          width: 200
          items:
            - !text
              text: 'Impression du : <%text>$</%text>{now dd.MM.yyyy HH:mm:ss}'
              fontSize: 8
              align: left
              vertAlign: top
        # Title
        - !columns
          absoluteX: 23
          absoluteY: 78
          width: 118
          items:
            - !text
              text: '<%text>$</%text>{title}'
              fontSize: 10
        # Comment
        - !columns
          absoluteX: 849
          absoluteY: 78
          width: 200
          items:
            - !text
              text: '<%text>$</%text>{comment}'
              fontSize: 7
              align: left
        # Scale
        - !columns
          condition: showScalevalue
          absoluteX: 488
          absoluteY: 57
          width: 150
          items:
            - !text
              text: 'Échelle 1:<%text>$</%text>{scale}'
              fontSize: 9
              align: center
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
3 A3 paysage\
</%def>
