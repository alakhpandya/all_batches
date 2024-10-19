$('.owl-carousel').owlCarousel({
    loop:true,
    // margin:10,
    nav:true,
    dots:false,
    // autoplay:true,
    // autoplayTimeout: 3000,
    // autoplayHoverPause:true,
    navText: [$('.owl-nav-prev'),$('.owl-nav-next')],
    responsive:{
        0:{
            items:1
        },
        768:{
            items:2
        },
        1024:{
            items:3
        }
    }
})