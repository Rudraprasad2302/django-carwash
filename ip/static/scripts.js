let menuBtn = document.querySelector("#menu-btn");
let navbar = document.querySelector(".header .flex .navbar");

menuBtn.onclick = () =>{
    menuBtn.classList.toggle("fa-times");
    navbar.classList.toggle('active');

}

var swiper = new Swiper(".carwash-slider", {
    spaceBetween: 20,
    grabCursor:true,
    loop:true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
        540: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        
      },
  });

  var swiper = new Swiper(".bikewash-slider", {
    spaceBetween: 20,
    grabCursor:true,
    loop:true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
        540: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        
      },
  });

  

  document.getElementById('bookNowBtn').addEventListener('click', () => {
    alert('For booking call : 420-420-420');

});

document.getElementById('bookNowBtn2').addEventListener('click', () => {
  alert('For booking call : 420-420-420');

});

document.getElementById('bookNowBtn3').addEventListener('click', () => {
  alert('For booking call : 420-420-420');

});

document.getElementById('bookNowBtn4').addEventListener('click', () => {
  alert('For booking call : 420-420-420');

});



document.getElementById('bookNowBtn5').addEventListener('click', () => {
  alert('For booking call : 420-420-420');

});

document.getElementById('bookNowBtn6').addEventListener('click', () => {
  alert('For booking call : 420-420-420');

});

var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 20,
  grabCursor:true,
  loop:true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
      540: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      }
      
    },
});




