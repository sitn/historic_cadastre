﻿$(document).ready(function() {

    jQuery.extend( jQuery.fn.dataTableExt.oSort, {
        "date-euro-pre": function ( a ) {
            var x;

            if ( $.trim(a) !== '' ) {
                var frDatea = $.trim(a).split(' ');
                var frDatea2 = frDatea[0].split('.');
                x = (frDatea2[2] + frDatea2[1] + frDatea2[0]) * 1;
            }
            else {
                x = Infinity;
            }

            return x;
        },

        "date-euro-asc": function ( a, b ) {
            return a - b;
        },

        "date-euro-desc": function ( a, b ) {
            return b - a;
        }
    });

     /* Build the DataTable with third column using our custom sort functions */
    $('#historic_parcel_doc').dataTable({
        "iDisplayLength": 25,
        "aaSorting": [[0, 'asc'], [1, 'asc']],
        "aoColumns": [
            {"sType": 'numeric'},
            {"sType": 'numeric'},
            null,
            null,
            null,
            {"sType": 'date-euro'},
            {"sType": 'date-euro'},
            {"sType": 'date-euro'},
            null,
            null
        ],
        "oLanguage": {
            "sInfo": "affiché _START_ à _END_ sur _TOTAL_ enregistrements",
            "sSearch": "Rechercher :",
            "sInfoEmpty": "Pas d'enregistrement correspondant",
            "sEmptyTable": "Pas de données dans la table",
            "sInfoFiltered": " - filtre sur _MAX_ enregistrements",
            "sLengthMenu": 'Affichage<select>'+
                '<option value="25">25</option>'+
                '<option value="50">50</option>'+
                '<option value="100">100</option>'+
                '<option value="150">150</option>'+
                '</select>Enregistrement',
            "sZeroRecords": "Pas d'enregistrement à afficher",
            "oPaginate": {
                "sPrevious": "Page précédente",
                "sNext": "Page suivante"
            }
        }
    });
});
