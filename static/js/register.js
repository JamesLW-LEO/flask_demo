//focus, blur
//alert($('form').first().user.value);
//$('form').form('user').value('bbb');
$(function () {

    $('form').first().reset();
    $('form').form('user').bind('focus', function () {
        $('#reg .info_user').css('display', 'block');
        $('#reg .error_user').css('display', 'none');
        $('#reg .succ_user').css('display', 'none');
    }).bind('blur', function () {
        if (trim($(this).value()) == '') {
            $('#reg .info_user').css('display', 'none');
            $('#reg .error_user').css('display', 'none');
            $('#reg .succ_user').css('display', 'none');
        } else if (!check_user()) {
            $('#reg .error_user').css('display', 'block');
            $('#reg .info_user').css('display', 'none');
            $('#reg .succ_user').css('display', 'none');
        } else {
            $('#reg .succ_user').css('display', 'block');
            $('#reg .error_user').css('display', 'none');
            $('#reg .info_user').css('display', 'none');
        }
    });

    function check_user() {
        if (/[\w]{2,20}/.test(trim($('form').form('user').value()))) return true;
    }


    //密码验证
    $('form').form('pass').bind('focus', function () {
        $('#reg .info_pass').css('display', 'block');
        $('#reg .error_pass').css('display', 'none');
        $('#reg .succ_pass').css('display', 'none');
    }).bind('blur', function () {
        if (trim($(this).value()) == '') {
            $('#reg .info_pass').css('display', 'none');
        } else {
            if (check_pass()) {
                $('#reg .info_pass').css('display', 'none');
                $('#reg .error_pass').css('display', 'none');
                $('#reg .succ_pass').css('display', 'block');
            } else {
                $('#reg .info_pass').css('display', 'none');
                $('#reg .error_pass').css('display', 'block');
                $('#reg .succ_pass').css('display', 'none');
            }
        }
    });

    //密码强度验证
    $('form').form('pass').bind('keyup', function () {
        check_pass();
    });

    //密码验证函数
    function check_pass() {
        var value = trim($('form').form('pass').value());
        var value_length = value.length;
        var code_length = 0;

        //第一个必须条件的验证6-20位之间
        if (value_length >= 6 && value_length <= 20) {
            $('#reg .info_pass .q1').html('●').css('color', 'green');
        } else {
            $('#reg .info_pass .q1').html('○').css('color', '#666');
        }

        //第二个必须条件的验证，字母或数字或非空字符，任意一个即可
        if (value_length > 0 && !/\s/.test(value)) {
            $('#reg .info_pass .q2').html('●').css('color', 'green');
        } else {
            $('#reg .info_pass .q2').html('○').css('color', '#666');
        }

        //第三个必须条件的验证，大写字母，小写字母，数字，非空字符 任意两种混拼即可
        if (/[\d]/.test(value)) {
            code_length++;
        }

        if (/[a-z]/.test(value)) {
            code_length++;
        }

        if (/[A-Z]/.test(value)) {
            code_length++;
        }

        if (/[^\w]/.test(value)) {
            code_length++;
        }

        if (code_length >= 2) {
            $('#reg .info_pass .q3').html('●').css('color', 'green');
        } else {
            $('#reg .info_pass .q3').html('○').css('color', '#666');
        }

        //安全级别
        if (value_length >= 10 && code_length >= 3) {
            $('#reg .info_pass .s1').css('color', 'green');
            $('#reg .info_pass .s2').css('color', 'green');
            $('#reg .info_pass .s3').css('color', 'green');
            $('#reg .info_pass .s4').html('高').css('color', 'green');
        } else if (value_length >= 8 && code_length >= 2) {
            $('#reg .info_pass .s1').css('color', '#f60');
            $('#reg .info_pass .s2').css('color', '#f60');
            $('#reg .info_pass .s3').css('color', '#ccc');
            $('#reg .info_pass .s4').html('中').css('color', '#f60');
        } else if (value_length >= 1) {
            $('#reg .info_pass .s1').css('color', 'maroon');
            $('#reg .info_pass .s2').css('color', '#ccc');
            $('#reg .info_pass .s3').css('color', '#ccc');
            $('#reg .info_pass .s4').html('低').css('color', 'maroon');
        } else {
            $('#reg .info_pass .s1').css('color', '#ccc');
            $('#reg .info_pass .s2').css('color', '#ccc');
            $('#reg .info_pass .s3').css('color', '#ccc');
            $('#reg .info_pass .s4').html(' ');
        }

        if (value_length >= 6 && value_length <= 20 && !/\s/.test(value) && code_length >= 2) {
            return true;
        } else {
            return false;
        }
    }


    //密码确认
    $('form').form('notpass').bind('focus', function () {
        $('#reg .info_notpass').css('display', 'block');
        $('#reg .error_notpass').css('display', 'none');
        $('#reg .succ_notpass').css('display', 'none');
    }).bind('blur', function () {
        if (trim($(this).value()) == '') {
            $('#reg .info_notpass').css('display', 'none');
        } else if (check_notpass()) {
            $('#reg .info_notpass').css('display', 'none');
            $('#reg .error_notpass').css('display', 'none');
            $('#reg .succ_notpass').css('display', 'block');
        } else {
            $('#reg .info_notpass').css('display', 'none');
            $('#reg .error_notpass').css('display', 'block');
            $('#reg .succ_notpass').css('display', 'none');
        }
    });

    function check_notpass() {
        if (trim($('form').form('notpass').value()) == trim($('form').form('pass').value())) return true;
    }


    //电子邮件
    $('form').form('email').bind('focus', function () {

        //补全界面
        if ($(this).value().indexOf('@') == -1) $('#reg .all_email').css('display', 'block');

        $('#reg .info_email').css('display', 'block');
        $('#reg .error_email').css('display', 'none');
        $('#reg .succ_email').css('display', 'none');
    }).bind('blur', function () {

        //补全界面
        $('#reg .all_email').css('display', 'none');

        if (trim($(this).value()) == '') {
            $('#reg .info_email').css('display', 'none');
        } else if (check_email()) {
            $('#reg .info_email').css('display', 'none');
            $('#reg .error_email').css('display', 'none');
            $('#reg .succ_email').css('display', 'block');
        } else {
            $('#reg .info_email').css('display', 'none');
            $('#reg .error_email').css('display', 'block');
            $('#reg .succ_email').css('display', 'none');
        }
    });

    function check_email() {
        if (/^[\w\-\.]+@[\w\-]+(\.[a-zA-Z]{2,4}){1,2}$/.test(trim($('form').form('email').value()))) return true;
    }


    //电子邮件补全系统键入
    $('form').form('email').bind('keyup', function (event) {
        if ($(this).value().indexOf('@') == -1) {
            $('#reg .all_email').css('display', 'block');
            $('#reg .all_email li span').html($(this).value());
        } else {
            $('#reg .all_email').css('display', 'none');
        }

        $('#reg .all_email li').css('background', 'none');
        $('#reg .all_email li').css('color', '#666');

        if (event.keyCode == 40) {
            if (this.index == undefined || this.index >= $('#reg .all_email li').length() - 1) {
                this.index = 0;
            } else {
                this.index++;
            }
            $('#reg .all_email li').eq(this.index).css('background', '#e5edf2');
            $('#reg .all_email li').eq(this.index).css('color', '#369');
        }

        if (event.keyCode == 38) {
            if (this.index == undefined || this.index <= 0) {
                this.index = $('#reg .all_email li').length() - 1;
            } else {
                this.index--;
            }
            $('#reg .all_email li').eq(this.index).css('background', '#e5edf2');
            $('#reg .all_email li').eq(this.index).css('color', '#369');
        }


        if (event.keyCode == 13) {
            $(this).value($('#reg .all_email li').eq(this.index).text());
            $('#reg .all_email').css('display', 'none');
            this.index = undefined;
        }

    });

    //电子邮件补全系统点击获取
    $('#reg .all_email li').bind('mousedown', function () {
        $('form').form('email').value($(this).text());
    });

    //电子邮件补全系统鼠标移入移出效果
    $('#reg .all_email li').hover(function () {
        $(this).css('background', '#e5edf2');
        $(this).css('color', '#369');
    }, function () {
        $(this).css('background', 'none');
        $(this).css('color', '#666');
    });


    //年
    var year = $('form').form('year');

    function check_birthday() {
        if (year.value() != 0) return true;
    }

    //提交
    $('form').form('sub').click(function () {
        var flag = true;

        if (!check_user()) {
            $('#reg .error_user').css('display', 'block');
            flag = false;
        }

        if (!check_pass()) {
            $('#reg .error_pass').css('display', 'block');
            flag = false;
        }

        if (!check_notpass()) {
            $('#reg .error_notpass').css('display', 'block');
            flag = false;
        }

        if (!check_email()) {
            $('#reg .error_email').css('display', 'block');
            flag = false;
        }

        if (!check_birthday()) {
            $('#reg .error_birthday').css('display', 'block');
            flag = false;
        }
        if (flag) {
            $('form').first().submit();
        }
    });
})