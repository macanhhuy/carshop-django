function countryChange(countrySelect) {
    if (countrySelect.value != -1) {
        $.ajax({url:'/findStateOrCity/' + countrySelect.value,
                    type: 'get',
                    success: function(data, status) {
                        var jsonData = eval("(" + data + ")");
                        $('#id_state').empty();
                        $('#id_city').empty();
                        $('#id_state').append("<option value='-1'>Select...</option>");
                        $('#id_city').append("<option value='-1'>Select...</option>");
                        for (var i = 0; i < jsonData.length; i++) {
                            $("<option value='" + jsonData[i].pk + "'>" + jsonData[i].fields.name + "</option>").appendTo('#id_state');
                        }
                    },
                    error: function(xhr, desc, err) {
                        alert(err);
                    }
                });
    }
    else {
        $('#id_state').empty();
        $('#id_state').append("<option value='-1'>Select...</option>");
    }
}

function stateChange(stateSelect) {
    if (stateSelect.value != -1) {
        $.ajax({url:'/findStateOrCity/' + stateSelect.value,
                    type: 'get',
                    success: function(data, status) {
                        var jsonData = eval("(" + data + ")");
                        $('#id_city').empty();
                        $('#id_city').append("<option value='-1'>Select...</option>");
                        for (var i = 0; i < jsonData.length; i++) {
                            $("<option value='" + jsonData[i].pk + "'>" + jsonData[i].fields.name + "</option>").appendTo('#id_city');
                        }
                    },
                    error: function(xhr, desc, err) {
                        alert(err);
                    }
                });
    }
    else {
        $('#id_city').empty();
        $('#id_city').append("<option value='-1'>Select...</option>");
    }
}