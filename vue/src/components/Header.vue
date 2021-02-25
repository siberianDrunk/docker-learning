<template>
  <div class="section" id="section0">
    <div class="container">
      <div class="row mt-5">
        <div class="col-sm d-flex justify-content-center align-content-center">
          <transition name="image">
          <h4 v-if="showHeaderImg" style="margin-right: 20px" class="main-text text-center text-justify"> Студент</h4>
          </transition>
        </div>
      </div>
      <div class="row">
        <div class="col-sm d-flex justify-content-center align-content-center mt-4">
          <transition name="image">
          <img v-if="showHeaderImg"  class="main head-img" align="center" src="src/assets/img/1%20студентик.png">
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: "Header",
    data () {
      return {
        showHeaderImg:false
      }
    },
    methods : {
      showHeader(destinationIndex) {
        if (destinationIndex == 0) {
          this.showHeaderImg = true
        }
      },
      hideHeader(destinationIndex) {
        if (destinationIndex == 1) {
           this.showHeaderImg = false
        }
      }
    },
    created () {
      this.$root.$on('showHeader', (directionIndex) => {
        this.showHeader(directionIndex)
      });
      this.$root.$on('hideHeader', (directionIndex) => {
        this.hideHeader(directionIndex)
      });
    }
  }

</script>

<style scoped>
  .image-enter {
    opacity:0
  }

  .image-enter-active {

    transition: opacity 1s;
  }
  .image-leave {

  }
  .image-leave-active {
    transition: opacity 1s;
    opacity: 0;
  }

</style>
