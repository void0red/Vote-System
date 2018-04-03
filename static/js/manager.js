function addTP() {
    var title = $("#add-tp-title").val();
    var option = $("#add-tp-options").val();
    var o = option.split('\n');
    var options = [];
    for(var i = 0; i < o.length; i++){
        if(o[i] != ''){
            options.push(o[i])
        }
    }
    if(title == "" || options == null){
        return false;
    }
    var category = 0;
    var v = $('input:radio[name="optionsRadios"]:checked').val();
    if(v == 'option2'){
        category = 2;
    }else if(v == 'option1'){
        category = 1;
    }else {
        category = 0;
    }
    httpPost('/manager', {'ssid': 1, 'title': title, 'content': options, 'category': category});
}
function removeTP(a) {
    httpPost('/manager', {'ssid': 0, 'title_hash': a.id})
}