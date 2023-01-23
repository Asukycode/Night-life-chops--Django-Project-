var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,

    loop: true,
    centerSlide:'true',
    fade:'true',
    grabCursor:'true',
    
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});