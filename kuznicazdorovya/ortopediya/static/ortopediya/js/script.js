$(document).ready(function(){
    $('.slider').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3500,
    });
});

$(document).ready(function(){
    $('.slider_about').slick({
    slidesToShow: 4,
    speed:2000,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 0,
    wariableWidth:true,
    arrows:false,
    cssEase: 'linear',
    });
});