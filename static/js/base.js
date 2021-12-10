// Mobile nav icon
$('#expand-menu-icon').click(() => {
    $('.mobile-nav').removeClass('display-mobile-nav');
    $('.mobile-nav').show(300);
    $('.mobile-nav').children().show(300);
});

// Cole mobile nav bar
$('.close-menu > p').click(() => {
    $('.mobile-nav').addClass('display-mobile-nav');
    $('.mobile-nav').hide(300);
    $('.mobile-nav').children().hide(300);
});

// Bootstrap Message (from Boutique Ado)
$('.toast').toast('show');

// Update footer year
var currentYear= new Date().getFullYear(); 
$('#copyright-year').text(currentYear);

$('#portfolio-dropdown').click(() => {
    let caret_up = $('.fa-caret-up');
    let caret_down = $('.fa-caret-down');
    let sub_nav = $('.sub-nav');
    sub_nav.slideToggle("slow");

    if(caret_up.hasClass('hiden')) {
        caret_up.removeClass('hiden');
        caret_down.addClass('hiden');
    } else if(caret_down.hasClass('hiden')) {
        caret_down.removeClass('hiden');
        caret_up.addClass('hiden');
    }
});
