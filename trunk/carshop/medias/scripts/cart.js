function checkNum(obj){
	if(!obj.value.match(/^\d+$/)){
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
                        
                        if("true" == data){
                            var divMsg = $('<div style="overflow:hidden;position:absolute; top:10px; left:10px; display:block;background-color:#0F3; width:0px; height:25px;line-height:25px;float:left;"><strong>Success</strong></div>');

                            $("#pdiv" + id).append(divMsg);
                            divMsg.animate({width:80},"slow");
                            divMsg.fadeOut(3000);
                            
                        }
                    },
                    error: function(xhr, desc, err) {
                        //alert(xhr);
                        //alert("Desc: " + desc + "\nErr:" + err);
                        
                        var divMsg = $('<div style="overflow:hidden;position:absolute; top:10px; left:10px; display:block;background-color:#F00; width:0px; height:25px;line-height:25px;float:left;"><strong>Error</strong></div>');

                        $("#pdiv" + id).append(divMsg);
                        divMsg.animate({width:80},"slow");
                        divMsg.fadeOut(3000);

                    }
                });
    }
