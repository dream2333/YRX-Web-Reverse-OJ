var s = r("encrypt");
function n() {
    void 0 !== s && (this.jsencrypt = new s.JSEncrypt,
    this.jsencrypt.setPublicKey("-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDq04c6My441Gj0UFKgrqUhAUg+kQZeUeWSPlAU9fr4HBPDldAeqzx1UR99KJHuQh/zs1HOamE2dgX9z/2oXcJaqoRIA/FXysx+z2YlJkSk8XQLcQ8EBOkp//MZrixam7lCYpNOjadQBb2Ot0U/Ky+jF2p+Ie8gSZ7/u+Wnr5grywIDAQAB-----END PUBLIC KEY-----"))
}
n.prototype.encode = function(t, e) {
    var i =  + "|" + t 
    return encodeURIComponent(this.jsencrypt.encrypt(i))
}
