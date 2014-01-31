Ext.namespace('historic_cadastre');

historic_cadastre.Measure = function(mapPanel) {

    var length = new OpenLayers.Control.Measure(OpenLayers.Handler.Path, {
        eventListeners: {
            measure: function(evt) {
                alert("The length was " + evt.measure + evt.units);
            }
        }
    });

    var area = new OpenLayers.Control.Measure(OpenLayers.Handler.Polygon, {
        eventListeners: {
            measure: function(evt) {
                alert("The area was " + evt.measure + evt.units);
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
                }
            }
        }
    });

    return [
        lengthButton,
        areaButton
    ];

};
