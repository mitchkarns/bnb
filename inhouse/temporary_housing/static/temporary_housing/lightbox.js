$(".show-lightbox").click(function(){
    $('.background-fill').fadeIn();
    $('.lightbox').fadeIn();
});
$(".hide-lightbox").click(function(){
    $('.lightbox').fadeOut();
    $('.background-fill').fadeOut();
});
