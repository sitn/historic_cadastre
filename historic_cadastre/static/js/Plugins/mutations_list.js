
$(document).ready(function() {
    /* Build the DataTable with third column using our custom sort functions */
    $('#mutation').dataTable({
        "aaSorting": [[0, 'asc'], [1, 'asc']],
        "aoColumns": [
            {"sType": 'numeric'},
            {"sType": 'numeric'},
            null,
            null,
            null,
            null,
            null,
            null,
            null
        ],
        "oLanguage": {
            "sInfo": "affiché _START_ à _END_ sur _TOTAL_ enregistrements",
            "sSearch": "Rechercher :",
            "sInfoEmpty": "Pas d'enregistrement correspondant",
            "sEmptyTable": "Pas de données dans la table",
            "sInfoFiltered": " - filtre sur _MAX_ enregistrements",
            "sLengthMenu": "Affichage _MENU_ enregistrements",
            "sZeroRecords": "Pas d'enregistrement à afficher",
            "oPaginate": {
                "sPrevious": "Page précédente",
                "sNext": "Page suivante"
            }
        }
    });
});
