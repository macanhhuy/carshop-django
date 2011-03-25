function showMask(){  
	var width=document.body.scrollWidth;  
	var height=document.body.scrollHeight;  
	var left=width/2-$("#maskDisplay").width()/2;  
	$("#mask").css("width",width).css("height",height);  
	//$(document.body).css("overflow","hidden");  
	$("#mask").show();  
	$("#maskDisplay").show();  
}  

function hiddenMask(){  
	$("#mask").hide();  
	$("#maskDisplay").hide();  
} 