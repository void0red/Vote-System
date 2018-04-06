function vote() {
    var id = checkVote();
    var url = window.location.href;
    var title_hash = url.split('/').pop();
    var key = $("#verify").val();
    httpPost('/tp/' + title_hash, {'id': id, 'key': key.toLocaleUpperCase(), 'enc': enc(key)});
}
function checkVote(){
    var obj = document.getElementsByName('shareOption');
    var check_val = [];
    for(k in obj){
        if(obj[k].checked)
            check_val.push(obj[k].value);
    }
    return check_val;
}