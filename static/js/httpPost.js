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