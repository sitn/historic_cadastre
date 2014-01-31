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
            new OpenLayers.Control.ScaleLine({
                geodesic: true,
                bottomInUnits: false,
                bottomOutUnits: false
            }),
            new OpenLayers.Control.MousePosition({numDigits: 0})
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

    map.events.register('zoomend', this, function() {
            var scale = map.getScale();
    });
        
    map.addLayer(image_layer);

    // Ext & GeoExt
    var mapPanel = new GeoExt.MapPanel({
        stateId: "map",
        map: map,
        center: new OpenLayers.LonLat(0, 0),
        zoom: 3,
        region: "center",
        tbar: new Ext.Toolbar({
            cls: 'map-toolbar'
        })
    });

    var tbar = mapPanel.getTopToolbar();

    tbar.addButton(historic_cadastre.Measure(mapPanel));

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