function tab() {
    var oNav = document.getElementsByClassName('nav')[0];
    var aLi1 = oNav.getElementsByTagName('li');
    var oCon = document.getElementById('content');
    var aLi2 = oCon.getElementsByTagName('li');
    var num;
    aLi1[0].style.backgroundColor = "rgba(0,0,0,.5)";
    aLi2[0].style.display = "block";
    for (var i = 0; i < aLi1.length; i++) {
        aLi1[i].index = i;
        aLi1[i].onclick = function () {
            num = this.index;
            for (var i = 0; i < aLi1.length; i++) {//先让所有按钮类名清除
                aLi2[i].style.display = "none";
                aLi1[i].style.backgroundColor = "rgba(0,0,0,.2)";
            }
            ;
            aLi1[this.index].style.backgroundColor = "rgba(0,0,0,.5)";
            aLi2[num].style.display = 'block';
        }
    }
}

tab()


function showtime() {
    //创建Date对象
    var today = new Date();
    //分别取出年、月、日、时、分、秒
    var year = today.getFullYear();
    var month = today.getMonth() + 1;
    var day = today.getDate();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    var weekDays = today.getDay();
    var weekDaysArray = ["日", "一", "二", "三", "四", "五", "六"];
    for (var i = 0; i < 7; i++) {
        if (weekDays == i) {
            //将dayCycleArray的数赋值到系统星期几里面中去;
            weekDays = weekDaysArray[i];
        }
    }
    //如果是单个数，则前面补0
    month = month < 10 ? "0" + month : month;
    day = day < 10 ? "0" + day : day;
    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    //构建要输出的字符串
    var str = year + "年" + month + "月" + day + "日 " + hours + ":" + minutes + ":" + seconds + "&nbsp;" + "星期" + weekDays;
    //获取id=result的对象
    var obj = document.getElementById("time");
    //将str的内容写入到id=result的<div>中去
    obj.innerHTML = "北京时间:" + str;
    window.setTimeout("showtime()", 1000);
}

showtime();
