

    function joinCart(id) {
        //$("#mouseMsgDiv").html("<img src='/medias/images/loading_icon.gif'>");
        //$("#mouseMsgDiv").show();
        //$(document).mousemove(function(e) {
        //    $("#mouseMsgDiv").css({
        //                top: (e.pageY) + "px",
        //                left: (e.pageX + 15) + "px"
        //            });
        //});

        var qty = $('#qty' + id).attr("value");

        $.ajax({url:'/cart/' + id + "/" + qty,
                    type: 'post',
                    success: function(data, status) {
                        //alert(data);
                        //alert(status);
                        //$("#mouseMsgDiv").html("<img src='/medias/images/yes.gif'>");
                        //$("#mouseMsgDiv").hide(3000);
                        //$(document).unbind("mousemove");
                        
                        //'
                        
                        if("true" == data){
                            //var divMsg = $('<div id="pdivMsg%s" style="display:none;background-color:#0F3; width:100px; height:25px;line-height:25px;"><strong>Success</strong></div>');
                            
                            var divMsg = document.createElement("div");
                            divMsg.setAttribute('style', 'display:none;background-color:#0F3; width:100px; height:25px;line-height:25px;');
                            divMsg.innerHTML = "Success";
                            
                            $("#pdiv" + id).append(divMsg);
                            divMsg.show(1500, function(){
                                divMsg.hide(2000, function(){
                                    $("#pdiv" + id).remove(divMsg);
                                });
                            });
                        }
                    },
                    error: function(xhr, desc, err) {
                        //alert(xhr);
                        //alert("Desc: " + desc + "\nErr:" + err);
                        //$("#mouseMsgDiv").html("<img src='/medias/images/no.gif'>");
                        /*$(document).mousemove(function(e) {
                         $("#mouseMsgDiv").hide("slow");
                         });*/
                        //$(document).unbind("mousemove");
                        
                        
                    }
                });
    }