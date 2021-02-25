
var checkLastSlide = false;

new fullpage('#fullPage', {
    scrollingSpeed: 700,
    controlArrows:false,

    afterSlideLoad: function(origin, destination, direction) {

        var $isAnimatedFirst = $('.is-animated-buttons');
        if (destination.index == 0) {
         $isAnimatedFirst.addClass('animated fadeInUpBig');
         $isAnimatedFirst.css('visibility', 'visible')
        }

        var $progressBar = $('.progress-bar');
        var $slideLength = $('.fp-section.active .fp-slide').length;
        var calc = ( (direction.index) / ( $slideLength- 1) ) * 100;
        $progressBar.css('width', calc + '%').attr('aria-valuenow', calc );
        if (direction.index === ($slideLength - 1)) {
            checkLastSlide = true;
              }
        },
    onSlideLeave: function(origin, destination, direction){
        var $isAnimatedFirst = $('.is-animated-buttons');
        var $isAnimatedSecond = $('.is-animated-button');
        if (destination.index == 0) {
            $isAnimatedFirst.css('visibility', 'hidden');
        }
        $isAnimatedFirst.removeClass('animated fadeInUpBig');
        $isAnimatedSecond.removeClass('animated fadeOutDownBig delay-1s')
        checkLastSlide = false;
    },

    onLeave: function (orgin,destination,direction) {
        checkLastSlide =false;
        if (destination.index == 1) {
        var $headImage = $('.head-img');
        $headImage.addClass('animated fadeOut')
        }
        if (destination.index == 7) {
        var $footerImage = $('.footer-img');
        $footerImage.removeClass('animated fadeInUpBig ');
        $footerImage.addClass('animated fadeOutDownBig ');
         console.log('index 6')
        }

         },

    afterLoad: function (orgin,destination,direction) {
        fullpage_api.setAllowScrolling(false, 'left');
        fullpage_api.setAllowScrolling(false, 'right');
        console.log(destination.index);
        if (destination.index == 0) {
        var $headImage = $('.head-img');
        $headImage.removeClass('animated fadeOut');
        $headImage.addClass('animated fadeIn');
        }
        if (destination.index == 8) {
        var $footerImage = $('.footer-img');
        $footerImage.css('visibility', 'visible');
        $footerImage.removeClass('animated fadeOutDownBig ');
        $footerImage.addClass('animated fadeInUpBig');
        console.log('Footer is visible')
        }

    },




});

$(document).on('click', '#moveRight', function(){
  if (checkLastSlide) {
      fullpage_api.moveSectionDown();
  } else {
      fullpage_api.setScrollingSpeed(0);
      fullpage_api.moveSlideRight();
      fullpage_api.setScrollingSpeed(700);
  }
});

$(document).on('click', '#start', function(){
      fullpage_api.moveSlideRight();
});




$(document).on('click', '#moveLeft', function(){
      fullpage_api.setScrollingSpeed(0);
      fullpage_api.moveSlideLeft();
      fullpage_api.setScrollingSpeed(700);
});

