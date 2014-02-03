/**
* @include GeoExt/widgets/Action.js
* @include GeoExt/data/PrintProvider.js
* @include GeoExt/plugins/PrintProviderField.js
* @include GeoExt.ux/SimplePrint.js
*/

Ext.namespace('historic_cadastre');

historic_cadastre.PrintWindow = function(mapPanel, url) {
    var printWin = new Ext.Window({
        width: 250,
        bodyStyle: 'padding: 5px',
        renderTo: Ext.getBody(),
      //  title: this.printwindowTitle,
        border: false,
        layout: 'fit',
        autoHeight: false,
        height: 350,
        closeAction: 'hide',
        autoScroll: true,
        cls: 'toolwindow printpanel',
        listeners: {
            show: function(panel) {
                var printPanel = new historic_cadastre.Print(mapPanel, printWin, {
                    width: 240,
                    labelWidth: 80,
                    fieldsWidth: 140,
                    printUrl: url
                }).printPanel;
            },
            hide: function() {
                var map = mapPanel.map;
                if (map.getLayersByName('print').length > 0) {
                    map.removeLayer(map.getLayersByName('print')[0]);
                }
            }
        }
    });
    return printWin;
 
};

historic_cadastre.Print = function(mapPanel, printWin, options) {

    var  printProvider = new GeoExt.data.PrintProvider({
        // using get for remote service access without same origin restriction.
        // For asynchronous requests, we would set method to "POST".
        //method: "GET",
        method: "POST",
        
        // capabilities from script tag in Printing.html. For asynchonous
        // loading, we would configure url (and autoLoad) instead of
        // capabilities.
        //capabilities: printCapabilities,
        //url: "/geoserver/pdf/",
        //autoLoad: true
        url: options.printUrl,
        autoLoad: true,
        baseParams: {
            url: options.printUrl
        }
    });
    
    var map = mapPanel.map;

    if (map.getLayersByName('print').length > 0) {
        map.removeLayer(map.getLayersByName('print')[0]);
    }
        
    var extentLayer = new OpenLayers.Layer.Vector("print", {
        displayInLayerSwitcher: false,
        styleMap: new OpenLayers.StyleMap(new OpenLayers.Style(Ext.applyIf({
            pointRadius: 4,
            graphicName: "square",
            rotation: "${getRotation}",
            strokeColor: "${getStrokeColor}",
            fillOpacity: "${getFillOpacity}"
        }, OpenLayers.Feature.Vector.style["default"]), {
            context: {
                getRotation: function(feature) {
                    return printForm.printPage.rotation;
                },
                getStrokeColor: function(feature) {
                    return feature.geometry.CLASS_NAME == "OpenLayers.Geometry.Point" ?
                        "#000" : "#ee9900";
                },
                getFillOpacity: function(feature) {
                    return feature.geometry.CLASS_NAME == "OpenLayers.Geometry.Point" ?
                        0 : 0.4;
                }
            }
        })
    )});
   
    var printForm = new GeoExt.ux.SimplePrint({
        mapPanel: mapPanel,
        layer: extentLayer, // optional
        autoFit: true,
        printProvider: printProvider,
        bodyStyle: {padding: "5px"},
        labelWidth: 65,
        defaults: {width: 115},
        region: "east",
        border: false,
        width: 200
    });

    var onLoadCaps = function() {
        // add custom fields to the form
        printForm.insert(0, {
            xtype: "textfield",
            name: "title",
            fieldLabel: "Title",
            value: "A custom title",
            plugins: new GeoExt.plugins.PrintProviderField({
                printProvider: printProvider
            })
        });
        printForm.insert(1, {
            xtype: "textarea",
            fieldLabel: "Comment",
            name: "comment",
            value: "A custom comment",
            plugins: new GeoExt.plugins.PrintProviderField({
                printProvider: printProvider
            })
        });
        // add the print form to its container
        printWin.add(printForm);
        printWin.doLayout();
    }
    
        /* use this code block instead of the above line if you configured the
     * printProvider with url instead of capabilities
    */
    var myMask = new Ext.LoadMask(printWin.body, {msg:"Loading data..."});
    myMask.show();
    printProvider.on("loadcapabilities", function() {
        myMask.hide();
        onLoadCaps();
    });
    
};
