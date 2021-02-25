<template>
  <div data-aos-easing="ease" data-aos-duration="1000" data-aos-delay="0">
    <div v-show="componentsLoaded">
      <app-navbar></app-navbar>
      <full-page class="mt-3" ref="fullpage" :options="options" id="fullpage" :skip-init="true">
        <app-header></app-header>
        <div v-for="grade in grades" class="section section-container">
          <div class="row">
            <div data-aos="fade-down" class="col title justify-content-center d-flex align-content-center ">
              <span class="text-block text-break text-center d-inline-block mainFont">{{grade.title}}</span>
            </div>
          </div>
          <div class="justify-content-center d-flex align-content-center row data-container">
            <div class="col-xs justify-content-center d-flex align-cont ent-center">
              <img id="main-image" class="main" :src="grade.img">
            </div>
          </div>
          <div class="row justify-content-center d-flex align-content-center">
            <div data-aos="zoom-in" class=" col-sm-3 col-xs-3 col-md-4 desc-block title  ">
              <span class="text-block  text-break text-center d-inline-block mainFont">{{grade.desc}}</span>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="container">
            <div class="row">
              <div class="col-sm d-flex justify-content-center align-content-center mt-4">
                <transition name="image">
                  <img data-aos="zoom-in" class="main footer-img" align="center" src="src/assets/img/41%20КОНЕЦ.png">
                </transition>
              </div>
            </div>
          </div>
        </div>

      </full-page>
    </div>
    <div v-show="!componentsLoaded" class="section">
      <div class="container">
        <div class="row">
          <div class="col-sm my-auto d-flex justify-content-center align-content-center">
            <div class="lds-ring">
              <div></div>
              <div></div>
              <div></div>
              <div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
  import AOS from 'aos'
  import 'aos/dist/aos.css'
  import $ from 'jquery'
  import Navbar from "../Navbar";
  import Header from "../Header";
  import Footer from "../Footer";
  import axios from "axios";

  export default {
    components: {
      appNavbar: Navbar,
      appHeader: Header,
      appFooter: Footer,
    },
    name: "StickyMain",
    data() {
      return {
        componentsLoaded: false,
        grades: [],
        directions: [],
        options: {
          licenseKey: 'OPEN-SOURCE-GPLV3-LICENSE',
          afterSlideLoad: this.afterSlideLoad,
          scrollingSpeed: 0,
          autoScrolling: true,
          onSlideLeave: this.onSlideLeave,
          onLeave: this.onLeave,
          afterLoad: this.afterLoad,
        },
      }
    },

    methods: {
      afterLoad(origin, destination, direction) {
        this.$root.$emit('showHeader', destination.index)
        $('.section.active [data-aos]').each(function () {
          $(this).addClass("aos-animate")
        });
        fullpage_api.setAllowScrolling(false);
        setTimeout(() => fullpage_api.setAllowScrolling(true), 600)
      },

      onLeave(origin, destination, direction) {
        $('.section [data-aos]').each(function () {
          $(this).removeClass("aos-animate")
        });
        console.log(destination.index)
        if (destination.index === 0 && direction === 'up' ||
          destination.index === 1 && direction === 'down' ||
          destination.index === 39 && direction === 'up' ||
          destination.index === 40 && direction === 'down') {
          fullpage_api.setScrollingSpeed(600)
        } else {
          fullpage_api.setScrollingSpeed(0);
        }
      },
      getApiData: function () {
        axios.all([
          axios.get(`http://localhost:${process.env.API_PORT}/api/grades/`)
            .then(response => {
              this.grades = response.data
            }),
          axios.get(`http://localhost:${process.env.API_PORT}/api/directions/`)
            .then(response => {
              this.directions = response.data
            }),
        ]);
        setTimeout(() => {
          this.$nextTick(() => {
            if (this.grades.length > 0 && this.directions.length > 0) {
              this.componentsReady()
              this.componentsLoaded = true;
            } else {
              this.grades = [];
              this.directions = [];
              setTimeout(() => {
                console.log('Retry to connect API');
                this.getApiData()
              }, 800)
            }
          })
        }, 300)
      },
      componentsReady() {
        this.$refs.fullpage.init()
      },
    },
    mounted() {
      this.getApiData()
       console.log(process.env.API_PORT)
    },
    created() {
      AOS.init({
        delay: 500
      });
      $('[data-aos]').each(function () {
        $(this).addClass("aos-init");
      });
    }
  }
</script>

<style scoped>

  .main-img {
    height: 300px;

  }

  .title {
    margin-top: auto;
    margin-bottom: auto;
  }

  .data-container {
    margin-left: auto;
    margin-right: auto
  }

  .desc-block {
    height: 80px;
    width: 400px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: white;
    border-radius: 2px;

    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);

    font-family: Helvetica, Arial, sans-serif, italic;
    font-size: 1rem;
    color: black;
    text-align: center;

  }

  .section-container {
    margin-top: 60px
  }

  .my-auto {
    position: fixed;
    top: 50%;
    left: 50%;
    /* bring your own prefixes */
    transform: translate(-50%, -50%);
  }

  .lds-ring {
    display: inline-block;
    position: relative;
    width: 30px;
    height: 30px;
  }

  .lds-ring div {
    box-sizing: border-box;
    display: block;
    position: absolute;
    width: 30px;
    margin-left: auto;
    margin-right: auto;
    height: 30px;
    border: 4px solid gray;
    border-radius: 50%;
    animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    border-color: gray transparent transparent transparent;
  }

  .lds-ring div:nth-child(1) {
    animation-delay: -0.45s;
  }

  .lds-ring div:nth-child(2) {
    animation-delay: -0.3s;
  }

  .lds-ring div:nth-child(3) {
    animation-delay: -0.15s;
  }

  @keyframes lds-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  /*iphone 5 */
  @media only screen and (min-width: 320px)  and (orientation: portrait) and (-webkit-min-device-pixel-ratio: 2) {
    .mainFont {
      font-size: 1rem;

    }

    .main-font {
      font-size: 0.75rem;
    }
  }

  @media only screen
  and (min-width: 320px)
  and (max-width: 568px)
  and (orientation: landscape)
  and (-webkit-min-device-pixel-ratio: 2) {

    .mainFont {
      font-size: 1rem;

    }

    .main-font {
      font-size: 0.7rem;
    }

    .main-arrow {
      font-size: 10px;

    }
  }

  /*iphone 6 */
  @media only screen and (min-width: 375px) and (orientation: portrait) and (-webkit-min-device-pixel-ratio: 2) {
    .mainFont {
      font-size: 0.9rem;
    }

    .main-font {
      font-size: 0.8rem;
    }
  }

  @media only  screen
  and (min-width: 375px)
  and (max-width: 667px)
  and (orientation: landscape)
  and (-webkit-min-device-pixel-ratio: 2) {

    .mainFont {
      font-size: 1.2rem;
    }

    .main-text {
      font-size: 20px;
    }

  }

  /*iphone 8+ */
  @media only screen and  (min-width: 414px) and (orientation: portrait) and (-webkit-min-device-pixel-ratio: 3) {
    .mainFont {
      font-size: 1.2rem;
    }
  }

  @media only screen
  and (min-width: 414px)
  and (max-width: 736px)
  and (orientation: landscape)
  and (-webkit-min-device-pixel-ratio: 3) {

    .mainFont {
      font-size: 1rem;
    }

  }

  /*iphone x */
  @media only screen and  (min-width: 375px) and (orientation: portrait) and (-webkit-min-device-pixel-ratio: 3) {
    .mainFont {
      font-size: 1rem;
    }
  }


</style>
