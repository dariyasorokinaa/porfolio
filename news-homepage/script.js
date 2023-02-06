$(() => {
    $("#burger").click(() => {
        $(".mobile-menu").toggle().css('z-index', '999999');
        $("#main").css({
        'opacity': '0.4',
    })

    });
});

$(() => {
    $("#close").click(() => {
        $(".mobile-menu").hide();
        $("#main").css({
            'opacity': 1,
        })
    });


});
