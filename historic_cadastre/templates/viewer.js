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
    
    var map = new OpenLayers.Map();
    
    var mapPanel = new GeoExt.MapPanel({
        title: "GeoExt MapPanel",
        renderTo: "mappanel",
        stateId: "mappanel",
        height: 400,
        width: 600,
        map: map,
        center: new OpenLayers.LonLat(5, 45),
        zoom: 4
    });
    
    
    
    Ext.get('loading').remove();
    Ext.fly('loading-mask').fadeOut({
        remove: true
    });
    
});