const form = $('#edit-index-form'); 

form.submit((e) => {
    $('.btn-mn').attr('disabled', true);
    $('#edit-index-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
});