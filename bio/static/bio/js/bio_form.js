const form = $('#edit-bio-form'); 

form.submit((e) => {
    $('.btn-mn').attr('disabled', true);
    $('#edit-bio-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
});