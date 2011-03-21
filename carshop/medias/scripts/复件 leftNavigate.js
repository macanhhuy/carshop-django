var OFFSET = 0;

function ddMenu(id,d){
	var h = document.getElementById('ddheader'+id);
	var c = document.getElementById('ddcontent'+id);
	if(d == 1){
		//alert(h.width)
		c.style.display = 'block';
		c.style.left = (h.parentNode.scrollWidth + OFFSET) + 'px';
		//document.getElementById("titler"+id).style.background='#BCDAFF';
	}else{
		document.getElementById("titler"+id).style.background='';
		c.style.display = 'none';
	}
}



function cancelHide(id){
	var h = document.getElementById('ddheader'+id);
	var c = document.getElementById('ddcontent'+id);
	c.style.display = 'block';
	c.style.left = (h.parentNode.scrollWidth + OFFSET) + 'px';
	document.getElementById("titler" + id).style.background='#BCDAFF';
	
}