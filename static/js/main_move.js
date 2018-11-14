$(".btn").click(function () {
    $(".qq_show").animate({left: "160px"}, 1000, function () {
        $(".qq_hide").animate({right: 0}, 500);
    });
});
$(".qq_hide").click(function () {
    $(".qq_hide").animate({right: "-33px"}, 1000, function () {
        $(".qq_show").animate({left: 0}, 500);
    });
});
$(function () {
    var index = 0;
    var flag = true;
    $('.left').on('click', function () {
        if (!flag) return false;
        flag = false;
        index--;
        var angle = -index * 90;
        $('.inner-box').css('transform', 'rotateX(' + angle + 'deg)').each(function (i, item) {
            /*设置不同的延时*/
            $(this).css('transition-delay', i * 0.25 + 's');
        });
        console.log(flag)
    });
    $('.right').on('click', function () {
        if (!flag) return false;
        flag = false;
        index++;
        var angle = -index * 90;
        $('.inner-box').css('transform', 'rotateX(' + angle + 'deg)').each(function (i, item) {
            /*设置不同的延时*/
            $(this).css('transition-delay', i * 0.25 + 's');
        });
    });
    $('.inner-box:last').on('transitionend', function () {
        /*最后一部分图片旋转完毕*/
        flag = true;
    });
});