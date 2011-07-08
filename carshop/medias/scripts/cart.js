function checkNum(obj) {
    if (!obj.value.match(/^\d+$/)) {
        obj.value = "";
    }
}

function joinCart(id) {
    var qty = $('#qty' + id).attr("value");

    $.ajax({url:'/cart/' + id + "/" + qty,
                type: 'post',
                success: function(data, status) {
                    //alert(data);
                    //alert(status);
                    var responseResult = eval("("+data+")");
                    if ("true" == responseResult.result) {
                        var divMsg = $('<div style="opacity:0.6;filter:alpha(opacity=60);overflow:hidden;position:absolute; top:0px; left:0px; display:block;background-color:#00B2EE; width:0px; height:25px;line-height:25px;float:left;"><strong>Added</strong></div>');

                        $("#pdiv" + id).append(divMsg);
                        divMsg.animate({width:80}, "slow");
                        $("#cartCount").text(responseResult.cartCount);
                        divMsg.fadeOut(3000);
                    }
                },
                error: function(xhr, desc, err) {
                    //alert(xhr);
                    //alert("Desc: " + desc + "\nErr:" + err);

                    var divMsg = $('<div style="overflow:hidden;position:absolute; top:0px; left:0px; display:block;background-color:#F00; width:0px; height:25px;line-height:25px;float:left;"><strong>Error</strong></div>');

                    $("#pdiv" + id).append(divMsg);
                    divMsg.animate({width:80}, "slow");
                    divMsg.fadeOut(3000);

                }
            });
}
