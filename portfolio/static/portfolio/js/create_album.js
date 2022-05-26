function previewPictures(inputId, previewContainer, imgContainerId, imgElId) {

    const uploadedFiles = $(inputId)[0].files;
    const numberPhotos = Object.keys(uploadedFiles);

    if(numberPhotos.length == 0) {
        $(previewContainer).hide(500);
        $(`#${imgElId}`).remove();
    } else {
        $(previewContainer).show(500);
        $(`#${imgElId}`).remove();
        $(uploadedFiles).each((key, value) => {
            let img_url = URL.createObjectURL(value);
            $(`<div>
                    <img id=${imgElId} class="previewPicture img-centered" src="${img_url}" alt="">
                </div>`).appendTo(imgContainerId);
        });
    };

};

$('#id_cover').change(() => {
    previewPictures('#id_cover', '.previewCoverImage', '#newAlbumCoverPrev', 'previewCoverPicture')
});

$('#id_photos').change(() => {
    previewPictures('#id_photos', '.previewImages', '#newAlbumPhotosPrev', 'previewPictureAlbum')
});

// Show loading animation on form submition
const form = $('#create-album-form'); 

form.submit((e) => {
    $('.btn-mn').attr('disabled', true);
    $('#create-album-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
});