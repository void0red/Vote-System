function httpPost(url, params) {
    var temp = document.createElement("form");
    temp.action = url;
    temp.method = "POST";
    temp.style.display = "none";
    for(var x in params){
        var opt = document.createElement("textarea");
        opt.name = x;
        opt.value = params[x];
        temp.appendChild(opt);
    }
    document.body.appendChild(temp);
    temp.submit();
    return temp;
}
function enc(s) {
    t = (s + '').toLocaleUpperCase();
    return $.md5(t).substr(0, 5);
}
function refree() {
    $("#verify").attr('src', 'static/pic/verify.png?a=' + Math.random() * 1000);
    location.reload()
}