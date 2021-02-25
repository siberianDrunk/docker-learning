<template>
  <div>
    <full-page  ref="fullpage" :options="options" id="fullpage" :skip-init="true">
      <Header></Header>
      <div class="section" v-show="componentsLoaded" v-for="(direction, index) in directions" :key="direction.title" :id="['section'+direction.importance]">
        <div class="slide" >
          <div class="row">
            <div class="col-sm text-center ">
              <h1> {{direction.title}}  </h1>
            </div>
          </div>
          <div class="row">
            <div class="col-sm text-center">
              <button class="btn" @click="$refs.fullpage.api.moveSlideRight()"> <i class="fa fa-fast-forward"> Старт </i></button>
            </div>
          </div>
        </div>
        <GradesRender :grades="grades" :direction="direction.id"></GradesRender>
      </div>
      <Footer v-show="componentsLoaded"></Footer>
    </full-page>
    <modal v-show="modalOpen" @close="modalOpen = false" :data="modalData"></modal>
    <div v-show="!componentsLoaded" class="section">
      <div class="container" >
      <div class="row">
        <div class="col-sm my-auto d-flex justify-content-center align-content-center">
          <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
  import GradesRender from './GradesRender'
  import Header from './Header'
  import Footer from './Footer'
  import modal from './Modal'
  import $ from 'jquery'
  import axios from 'axios'
  import velocity from 'velocity-animate'

  export default {
      components: {
      'Header': Header,
      'modal' : modal,
      'Footer': Footer,
      'GradesRender' : GradesRender,
    },
    name: "Main",
    data () {
      return {
        checkLastSlide: true,
        apiReady : false,
        grades: [],
        directions: [],
        modalOpen : false,
        componentsLoaded: false,
        headerLoaded: false,
        modalData : [],
        options: {
          licenseKey: 'OPEN-SOURCE-GPLV3-LICENSE',
          controlArrows: false,
          scrollingSpeed: 700,
          afterSlideLoad: this.afterSlideLoad,
          onSlideLeave: this.onSlideLeave,
          onLeave: this.onLeave,
          afterLoad: this.afterLoad,
        },
      }
    },
    methods: {

      afterSlideLoad(origin, destination, direction) {
        var $slideLength = $('.fp-section.active .fp-slide').length;
        this.$root.$emit('progressBar', direction.index, $slideLength)

        if (direction.index === ($slideLength - 1)) {
          this.checkLastSlide = true;
        }
      },
      onSlideLeave(origin, destination, direction){
        this.checkLastSlide = false;
      },

      onLeave(orgin,destination,direction) {
        this.checkLastSlide =false;
        if (destination.index == 1) {
          this.$root.$emit('hideHeader', destination.index);
        }
        if (destination.index == 7) {
          this.$root.$emit('hideFooter', destination.index);
        }
      },

      afterLoad(orgin,destination,direction) {
        fullpage_api.setAllowScrolling(false, 'left');
        fullpage_api.setAllowScrolling(false, 'right');
        fullpage_api.setKeyboardScrolling(false);
        if (destination.index == 0) {
          this.$root.$emit('showHeader', destination.index);
        }
        if (destination.index == 8) {
          this.$root.$emit('showFooter', destination.index);
        }

      },

      getApiData: function () {
        axios.all([
          axios.get(`http://localhost:${process.env.API_PORT}/api/grades/`)
            .then( response => {
              this.grades = response.data
            }),
          axios.get(`http://localhost:${process.env.API_PORT}/api/directions/`)
            .then( response => {
              this.directions = response.data
            }),
        ]);
        setTimeout(()=> {
          this.$nextTick(() => {
            if (this.grades.length > 0 && this.directions.length > 0) {
              this.componentsReady()
              this.componentsLoaded = true;
            }else {
              this.grades = [];
              this.directions = [];
              setTimeout(()=> {
                console.log('Retry to connect API');this.getApiData()
              }, 1500)
            }
          })}, 300)
      },
      moveRight : function() {
        if (this.checkLastSlide) {
          fullpage_api.moveSectionDown();
        } else {
          fullpage_api.setScrollingSpeed(0);
          fullpage_api.moveSlideRight();
          fullpage_api.setScrollingSpeed(700);
        }
      },
      moveLeft : function() {
        fullpage_api.setScrollingSpeed(0);
        fullpage_api.moveSlideLeft();
        fullpage_api.setScrollingSpeed(700);
      },
      showModal (item) {
        this.modalData = item;
        this.modalOpen = !this.modalOpen
      },
      componentsReady () {
        this.$refs.fullpage.init()
      }
     },


    mounted() {

      this.$root.$on('moveRight', () => {
        this.moveRight()
      });
      this.$root.$on('showModal', (data) => {
        this.showModal(data)
      });
      this.$root.$on('moveLeft', () => {
        this.moveLeft()
      });
      this.$root.$on('initFP', () => {
        this.componentsReady()
      });
      this.getApiData()

    },

    created() {




    },

    updated() {

    }

  }
</script>

<style scoped>
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

</style>
