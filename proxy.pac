function FindProxyForURL(url, host) {
    if (dnsDomainIs(host, "example.com") || shExpMatch(host, "(*.aptoide.com)") || shExpMatch(host, "(*.*)"))
        return "DIRECT";
    return "PROXY 192.168.56.1:8080";
}
