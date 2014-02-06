Ext.namespace('historic_cadastre');

historic_cadastre.Measure = function(mapPanel, id_measure) {

    var styleMap = new OpenLayers.StyleMap({
        "default": new OpenLayers.Style(null, {
            rules: [new OpenLayers.Rule({
                symbolizer: Ext.apply({
                    "Point": {
                        pointRadius: 4,
                        graphicName: "square",
                        fillColor: "white",
                        fillOpacity: 1,
                        strokeWidth: 1,
                        strokeOpacity: 1,
                        strokeColor: "#333333"
                    },
                    "Line": {
                        strokeWidth: 3,
                        strokeOpacity: 1,
                        strokeColor: "#666666",
                        strokeDashstyle: "dash"
                    },
                    "Polygon": {
                        strokeWidth: 2,
                        strokeOpacity: 1,
                        strokeColor: "#666666",
                        fillColor: "white",
                        fillOpacity: 0.3
                    }
                }, this.symbolizers)
            })]
        })
    });

    var length = new OpenLayers.Control.Measure(OpenLayers.Handler.Path, {
        handlerOptions: {layerOptions: {styleMap: styleMap}},
        eventListeners: {
            measure: function(evt) {
                var tbtext = Ext.getCmp(id_measure);
                tbtext.setText('Distance mesurée: '+Math.round(evt.measure*10)/10+' m');
            }
        }
    });

    var area = new OpenLayers.Control.Measure(OpenLayers.Handler.Polygon, {
        handlerOptions: {layerOptions: {styleMap: styleMap}},
        eventListeners: {
            measure: function(evt) {
                var tbtext = Ext.getCmp(id_measure);
                tbtext.setText('Surface mesurée: '+Math.round(evt.measure*10)/10+' m<sup>2</sup>');
            }
        }
    });

    mapPanel.map.addControl(length);
    mapPanel.map.addControl(area);

    var toggleGroup = "measure controls";

    var lengthButton = new Ext.Button({
        iconCls: "measureLength",
        cls: 'img-btn',
        overCls: 'over',
        tooltip: "Mesure de distance",
        enableToggle: true,
        toggleGroup: toggleGroup,
        listeners: {
            toggle: function(btn, pressed) {
                if (pressed === true) {
                    length.activate();
                } else {
                    length.deactivate();
                    var tbtext = Ext.getCmp(id_measure);
                    tbtext.setText('');
                }
            }
        }
    });

    var areaButton = new Ext.Button({
        iconCls: "measureArea",
        cls: 'img-btn',
        overCls: 'over',
        tooltip: "Mesure de surface",
        enableToggle: true,
        toggleGroup: toggleGroup,
        listeners: {
            toggle: function(btn, pressed) {
                if (pressed === true) {
                    area.activate();
                } else {
                    area.deactivate();
                    var tbtext = Ext.getCmp(id_measure);
                    tbtext.setText('');
                }
            }
        }
    });

    return [
        lengthButton,
        areaButton
    ];

};
