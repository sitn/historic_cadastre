/**
* @include GeoExt/widgets/Action.js
* @include GeoExt/data/PrintProvider.js
* @include GeoExt/plugins/PrintProviderField.js
* @include GeoExt.ux/SimplePrint.js
*/

Ext.namespace('historic_cadastre');

historic_cadastre.PrintWindow = function(mapPanel, url) {
    var printWin = new Ext.Window({
        width: 260,
        renderTo: Ext.getBody(),
        closeAction: 'hide',
        border: false,
        draggable: false,
        unstyled: true,
        resizable: false,
        shadow: false,
        cls: 'subtoolbar',
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

    var extentLayer = new OpenLayers.Layer.Vector(null, {
        displayInLayerSwitcher: false,
        styleMap: new OpenLayers.StyleMap({
            "default": new OpenLayers.Style({
                fillColor: '#ee9900',
                fillOpacity: 0.4,
                strokeWidth: 0
            }),
            "temporary": new OpenLayers.Style({
                fillColor: "#ffffff",
                fillOpacity: 1,
                strokeColor: "#000000",
                strokeOpacity: 1,
                strokeWidth: 1,
                pointRadius: 5,
                cursor: "${role}"
            }),
            "rotate": new OpenLayers.Style({
                externalGraphic: OpenLayers.Util.getImagesLocation() +
                    "print-rotate.png",
                fillOpacity: 1.0,
                graphicXOffset: 8,
                graphicYOffset: 8,
                graphicWidth: 20,
                graphicHeight: 20,
                cursor: "pointer",
                display: "${display}",
                rotation: "${rotation}"
            }, {
                context: {
                    display: function(f) {
                        return f.attributes.role == "se-rotate" ? "" : "none";
                    },
                    rotation: function(f) {
                        //return printPanel.printPage.rotation;
                        return printForm.printPage.rotation;
                    }
                }
            })
        })
    });

    var printForm = new GeoExt.ux.SimplePrint({
        mapPanel: mapPanel,
        layer: extentLayer, // optional
        autoFit: true,
        printProvider: printProvider,
        bodyStyle: {padding: "5px"},
        labelWidth: 80,
        defaults: {width: 130},
        region: "east",
        border: false,
        width: 230,
        printExtentOptions: {
            transformFeatureOptions: {
                rotationHandleSymbolizer: "rotate"
            }
        }
    });

    var onLoadCaps = function() {
        // add custom fields to the form
        printForm.insert(0, {
            xtype: "textfield",
            name: "title",
            fieldLabel: OpenLayers.i18n("Title"),
            emptyText: OpenLayers.i18n('Add a title'),
            plugins: new GeoExt.plugins.PrintProviderField({
                printProvider: printProvider
            })
        });
        printForm.insert(1, {
            xtype: "textarea",
            fieldLabel: OpenLayers.i18n("Comment"),
            name: "comment",
            emptyText:  OpenLayers.i18n("Add a comment"),
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
