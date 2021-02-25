<template>
  <div class="section" id="section8">

    <div  class="container">
      <div class="row">
        <div class="col-sm d-flex justify-content-center align-content-center mt-4">
          <transition name="image">
          <img v-if="showFooterImg" class="main footer-img" align="center" src="src/assets/img/41%20КОНЕЦ.png">
            </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
    export default {
      name: "Footer",
      data () {
        return {
         showFooterImg:false
        }
      },
      methods : {
        showFooter(destinationIndex) {
          if (destinationIndex == 8) {
            this.showFooterImg = true

          }
        },
        hideFooter(destinationIndex) {
          if (destinationIndex == 7) {
            this.showFooterImg = false
          }
        }
      },
      mounted () {
        this.$root.$on('showFooter', (directionIndex) => {
        this.showFooter(directionIndex)
        });
        this.$root.$on('hideFooter', (directionIndex) => {
        this.hideFooter(directionIndex)
        });
      }
    }
</script>

<style scoped>
 .image-enter {
    opacity:0
  }

  .image-enter-active {

    transition: opacity 0.5s;
  }
  .image-leave {

  }
  .image-leave-active {
    transition: opacity 0.5s;
    opacity: 0;
  }

</style>
