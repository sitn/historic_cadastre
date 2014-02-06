Ext.onReady(function() {
    // Ext global settings
    Ext.BLANK_IMAGE_URL = "${request.static_url('historic_cadastre:static/lib/ext/resources/images/default/s.gif')}";
    Ext.QuickTips.init();

   // OpenLayers global settings
    OpenLayers.Number.thousandsSeparator = ' ';
    OpenLayers.IMAGE_RELOAD_ATTEMPTS = 2;
    OpenLayers.DOTS_PER_INCH = 72;
    OpenLayers.ImgPath = "${request.static_url('historic_cadastre:static/images/ol/')}";
    OpenLayers.Lang.setCode("fr");
    // GeoExt global settings
    GeoExt.Lang.set("fr");

    var scales = [100, 250, 500, 1000, 2000, 5000, 10000];

    var map = new OpenLayers.Map({
        theme: null,
        units: "m",
        projection: "EPSG:21781",
        maxExtent: [-10000,-10000,10000,10000],
        center: new OpenLayers.LonLat(0, 0),
        scales: scales,
        controls: [
            new OpenLayers.Control.Navigation({
                dragPanOptions: {enableKinetic: true}
            }),
            new OpenLayers.Control.PanZoomBar({panIcons: false}),
//            new OpenLayers.Control.MousePosition({numDigits: 0}),
            new OpenLayers.Control.ScaleLine({
                geodesic: true,
                bottomInUnits: false,
                bottomOutUnits: false
            })
        ]
    });

    // IMAGE SECTION //
    // Define the bounds (we place the 0, 0 coordinates in the middle of the image.)
    var xmin = - Math.ceil(${plan_largeur}/2);
    var ymin = - Math.ceil(${plan_hauteur}/2);
    var xmax = ${plan_largeur} + xmin;
    var ymax = ${plan_hauteur} + ymin;
    xmin = xmin * ${plan_resolution};
    ymin = ymin * ${plan_resolution};
    xmax = xmax * ${plan_resolution};
    ymax = ymax * ${plan_resolution};

    var image_layer = new OpenLayers.Layer.Image(
        'the_image',
        '${plan_url}',
        new  OpenLayers.Bounds(xmin, ymin, xmax, ymax),
        new OpenLayers.Size(${plan_largeur},${plan_hauteur})
    );

    map.addLayer(image_layer);

    var bbar = new Ext.Toolbar({
        cls: 'map-toolbar',
        items: [{
            xtype: 'tbtext',
            text: [
                'Information dépourvues de foi publique, &copy; ',
                'SGRF, ',
                'République et Canton de Neuchâtel'
            ].join('')
        },
        '-',
        {
            xtype: 'tbtext',
            text: [
                '<span style="color:red;font-weight:bold;">ATTENTION</span>: ces plans ne sont pas orientés, le Nord ne se trouve pas forcèmenent en haut de la carte!'
            ]
        },
        '->',
        {
            xtype: 'tbtext',
            id: 'scale_text'
        }]
    });

    // Show map Scale
    map.events.register('zoomend', this, function() {
        var scale = Math.round(map.getScale());
        var tbtext = Ext.getCmp('scale_text');
        tbtext.setText('Échelle: 1:'+scale);
    });

    // Ext & GeoExt
    var mapPanel = new GeoExt.MapPanel({
        stateId: "map",
        map: map,
        center: new OpenLayers.LonLat(0, 0),
        zoom: 3,
        region: "center",
        tbar: new Ext.Toolbar({
            cls: 'map-toolbar'
        }),
        bbar: bbar
    });

    var tbar = mapPanel.getTopToolbar();

    tbar.addItem({
            xtype: 'tbtext',
            text: '<b>Cadastre</b>: ${nomcad} - <b>Plan</b> n° ${no_plan}, ${type_plan}',
            style: 'font-size:11.5px;'
    });
    tbar.addItem(' ');
    tbar.addItem('-');
    var id_measure = 'measure_text';
    tbar.addButton(historic_cadastre.Measure(mapPanel, id_measure));
    tbar.addItem('-');
    tbar.addItem({
        xtype: 'tbtext',
        id: id_measure,
        style: 'color:red;font-size:11.5px;font-weight:bold;'
    });
    // Add print Window
    tbar.addItem('->');
    tbar.addItem('-');
    
    var url = "${request.route_url('printproxy')}";
    var print_window;

% if nomcad:
    var options = {
        'cadastre': '${nomcad}'.trim(),
        'no_plan': '${no_plan}',
        'type_plan': '${type_plan}'
    };
% else:
    var option;
% endif

    tbar.addButton(
        new Ext.Button({
            iconCls: "print",
            text: 'Imprimer',
            tooltip: "Impression",
            enableToggle: true,
            listeners: {
                toggle: function(button) {
                    if (button.pressed) {
                        print_window = historic_cadastre.PrintWindow(button, mapPanel, url, options);
                        print_window.show();
                        print_window.anchorTo(GeoExt.MapPanel.guess().body, 'tr-tr', [0, -1]);
                    } else {
                        print_window.hide();
                    }
                }
            }
        })
    );

    var headerPanel = new Ext.Panel({
        region: 'north',
        height: 57,
        border: false,
        contentEl: 'header'
    });

    var viewport = new Ext.Viewport({
        layout: 'border',
        renderTo:'main',
        id:'viewPort',
        border:true,
        items: [
            headerPanel,
            mapPanel
        ]
    });

    // Refait la mise en page si la fenêtre change de taille
    //pass along browser window resize events to the panel
    Ext.EventManager.onWindowResize(viewport.doLayout, viewport);

    Ext.get('loading').remove();
    Ext.fly('loading-mask').fadeOut({
        remove: true
    });

});