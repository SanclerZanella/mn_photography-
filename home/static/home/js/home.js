$('.portfolio_dropdown').click(() => {
    let caret_up = $('.fa-caret-up');
    let caret_down = $('.fa-caret-down');

    $('.portfolio-items').toggle(500);

    if(caret_up.hasClass('hiden')) {
        caret_up.removeClass('hiden');
        caret_down.addClass('hiden');
    } else if(caret_down.hasClass('hiden')) {
        caret_down.removeClass('hiden');
        caret_up.addClass('hiden');
    }
});
