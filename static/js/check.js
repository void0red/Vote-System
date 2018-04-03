
function checkStrong(value) {
    var strength = 0;
    if (value.length > 5 && value.match(/[\da-zA-Z]+/)) {
        if (value.match(/\d+/)) {
            strength++;
        }
        if (value.match(/[a-z]+/)) {
            strength++;
        }
        if (value.match(/[A-Z]+/)) {
            strength++;
        }
        if (value.match(/[!@*$-_()+=&￥]+/)) {
            strength++;
        }
    }
    if (strength >= 3) {
        return true;
    }
    return false;
}
function checkPassword() {
    var passwordValue = $.trim($('#passwordValue').val());
    var rePasswordValue = $.trim($('#rePasswordValue').val());
    if ("" == passwordValue) {
        $("#passwordError").html("请输入密码");
        $("#passwordError").css("display", "inline-block");
        $("#register").attr("disabled", true);
        return false;
    }

    if (!checkStrong(passwordValue)) {
        $("#passwordError").html("6-20位数字、大小写字母或特殊字符(4选3)");
        $("#passwordError").css("display", "inline-block");
        $("#register").attr("disabled", true);
        return false;
    }

    if (rePasswordValue != "" && passwordValue != rePasswordValue) {
        $("#rePasswordError").html("输入的密码不一致");
        $("#rePasswordError").css("display", "inline-block");
        $("#register").attr("disabled", true);
        return false;
    } else {
        $("#rePasswordError").hide();
        $("#register").attr("disabled", false);
    }
    $("#passwordError").hide();
    $("#register").attr("disabled", false);
    return true;
}


function checkRePassword() {
    var passwordValue = $.trim($('#passwordValue').val());
    var rePasswordValue = $.trim($('#rePasswordValue').val());

    if ("" == rePasswordValue) {
        $("#rePasswordError").html("请再次输入密码");
        $("#rePasswordError").css("display", "inline-block");
        $("#register").attr("disabled", true);
        return false;
    }

    if (passwordValue != rePasswordValue) {
        $("#rePasswordError").html("输入的密码不一致");
        $("#rePasswordError").css("display", "inline-block");
        $("#register").attr("disabled", true);
        return false;
    }
    $("#rePasswordError").hide();
    $("#register").attr("disabled", false);
    return true;
}