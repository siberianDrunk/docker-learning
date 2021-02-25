<template>
  <div>
    <div v-for="(grade, index) in grades" v-if="grade.direction_id == direction"  class ="slide">
      <div class="container" >
        <div class="row">
          <div  class=" col-sm d-flex justify-content-center align-content-center ">
            <img class="main"  :src="grade.img">
          </div>
        </div>
        <div class="progress bg-transparent mb-1">
          <div class="progress-bar bg-dark" role="progressbar"  style="width: 0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="row mt-3">
          <div class="col-sm text-center animated "  >
            <button id="show-modal" class="btn border border-dark" @click="showModal(grade)"><span class="main-font">{{grade.title}}</span></button>
          </div>
        </div>

        <div class="row">
          <div class="col-sm text-center is-animated-div " >
            <button  class="main-arrow btn left "  @click="moveLeft"> <i  class="fa fa-arrow-circle-left"></i></button>
            <button  class="main-arrow btn is-animated-button" @click="moveRight"> <i class="fa fa-arrow-circle-right"></i></button>
          </div>
        </div>
      </div>

    </div>
    </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    components: {

    },
    props: ['grades', 'direction'],
    name: "GradesRender",

    data () {
      return {
        modalOpen: false,
        itCount: 0
      }
    },
    methods: {
      progressBar (directionIndex, slideLength) {
        var $progressBar = $('.progress-bar');
        var calc = ( (directionIndex) / ( slideLength- 1) ) * 100;
        $progressBar.css('width', calc + '%').attr('aria-valuenow', calc );
      },
      moveLeft () {
        this.$root.$emit('moveLeft')
        console.log(this.direction)
      },
      moveRight () {
        this.$root.$emit('moveRight')
      },
      showModal (data) {
        this.$root.$emit('showModal', data )

      },

    },
    mounted() {
      this.$root.$on('progressBar', (directionIndex, slideLength) => {
        this.progressBar(directionIndex, slideLength)
      });
      window.addEventListener('keydown', (e) => {
      if (e.key == 'ArrowLeft') {
        this.moveLeft()
      }
      if (e.key == 'ArrowRight') {
        this.moveRight()
      }
    });

    },


  }

</script>

<style scoped>
#show-modal {
  font-size: 20px;
}
.main-arrow {
  font-size: 30px;
}


</style>
