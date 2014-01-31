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
    
    // ${plan_url}
    
    
    var create_map = function() {

        var extend = [-215,-16,215,15];
        var restrictedExtent = [1,530,3,31];
    
        var map = new OpenLayers.Map({
            theme: null,
            units: "m",
            projection: "EPSG:21781",
            maxExtent: [-1000,-1000,1000,1000],
            controls: [
                new OpenLayers.Control.Navigation(),
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
        var image_url ='ola';
        image_url = "${request.static_url('historic_cadastre:static/images/testimg.png')}"
    
        var image_layer = new OpenLayers.Layer.Image(
            'roro',
            image_url,
            new  OpenLayers.Bounds(-215,-16,215,15),
            new OpenLayers.Size(530,31),
            {
                numZoomLevels: 5
        });
    
        map.addLayer(image_layer);

        var mapPanel = new GeoExt.MapPanel({
            //title: "GeoExt MapPanel",
            stateId: "mappanel",
            map: map,
            center: new OpenLayers.LonLat(5, 45),
            zoom: 4,
            region: "center"
        });
    
    
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
        
        viewport.doLayout();
        // Refait la mise en page si la fenêtre change de taille
        //pass along browser window resize events to the panel
        Ext.EventManager.onWindowResize(viewport.doLayout, viewport);
    };

    
        Ext.get('loading').remove();
            Ext.fly('loading-mask').fadeOut({
                remove: true
            });
    

    
});