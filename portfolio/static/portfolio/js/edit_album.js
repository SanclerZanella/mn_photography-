$(document).on('click', '.photoCollapsible', (e) => {
    var parentEl = $(e.target).parent();
    var content = $(e.target).next();

    if ($(e.target).hasClass('active')){
        $(e.target).removeClass('active');
        $(".photoCollapsible").css({
            "opacity": "1",
            "pointer-events": "auto",
        });
        $(".previewImages").css({
            "padding-bottom": "0",
        });
        $(e.target).css({
            "border": "0",
        });
        $(content).hide("slow")
    } else {
        $(e.target).addClass("active");
        $(".photoCollapsible").css({
            "opacity": "0.5",
            "pointer-events": "none",
            "z-index": "10",
        });
        $(".previewImages").css({
            "padding-bottom": "3.2em",
            "transform": "scale(1)",
            "transition": "1s all ease",
        });
        $(e.target).css({
            "opacity": "1",
            "pointer-events": "auto",
            "border": "3px solid #ff7a33",
        });
        parentEl.siblings().children().removeClass('active');
    };
    
    $('.photoCollapsible').each((key, value) => {
        var content = $(value).next();
        if ($(value).hasClass("active")) {
            $(content).show("slow")
        } else {
            $(content).hide("slow")
        };
    });

});


