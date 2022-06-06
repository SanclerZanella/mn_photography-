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
        $(content).hide("slow");

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


function openChangeModal(button, modal) {
    const changeModal = $(modal);
    const changeModalPreview = $('#changePhotoPrev');

    $(document).on('click', button, (e) => {
        changeModal.show(500);
        photo_src = $(e.target).data('photo');
        photo_url = $(e.target).data('url');
        changeModalPreview.html(
            `<img src="${photo_src}" alt="">`
        );
        $('#changePhoto_form').attr('action', `${photo_url}`);
    });

    const span = $('.close');
    span.click(() => {
        changeModal.hide(500);
    });

    $(window).click((e) => {
        if (e.target.id == changeModal.attr('id')) {
            changeModal.hide(500);
        };
    });
};

openChangeModal('.changeBtn', '#changePhotoModal');
