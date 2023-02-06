$(() => {
    $(".read").click(() => {
        $(".unread").removeClass("unread");
        $(".circle").fadeTo('normal', 0)
    });
});
