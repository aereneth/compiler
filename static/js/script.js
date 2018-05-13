$(window).on('load resize', function() {
    resizeFullPage();
});


function resizeFullPage() {
    if($(window).height() > $('.full-page').height()) {
        $('.full-page').height($(window).height());
    }
}