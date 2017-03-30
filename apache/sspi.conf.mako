# Configuration of the autologging under Windows and SITN Intranet instance
<IfModule !sspi_auth_module>
    LoadModule sspi_auth_module modules/mod_auth_sspi.so
</IfModule>
<Location /${instanceid}/>
    AuthName "A Protected Place"
    AuthType SSPI
    SSPIAuth On
    SSPIAuthoritative On
    SSPIOfferBasic On # For non IE users
    SSPIBasicPreferred On
    SSPIUsernameCase lower
    require valid-user
    SSPIDomain localhost/${instanceid}/
    Order allow,deny
    Allow from all
</Location>
<Location /${instanceid}/img>
    Satisfy any
</Location>
