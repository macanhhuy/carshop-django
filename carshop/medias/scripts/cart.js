

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
                            var divMsg = $('<div id="pdivMsg" style="overflow:hidden;position:absolute; top:10px; left:10px; display:block;background-color:#0F3; width:0px; height:25px;line-height:25px;float:left;"><strong>Success</strong></div>');
                            
                            //var divMsg = document.createElement("div");
                            //divMsg.setAttribute('style', 'display:none;background-color:#0F3; width:100px; height:25px;line-height:25px;');
                            //divMsg.innerHTML = "Success";
                            
                            //$("#pdivMsg" + id).clearQueue();
                            
                            $("#pdiv" + id).append(divMsg);
                            divMsg.animate({width:80},"slow", function(){
                                //$("#pdivMsg" + id).stop(true, false);
                                //$("#pdivMsg" + id).animate({width:0},"slow");

                            });
                            divMsg.fadeOut(4000, function(){
                                    //$("#pdivMsg" + id).style.width=0;
                                    //$("#pdivMsg" + id).show();
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
