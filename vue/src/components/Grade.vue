<template>
  <div class="container">
    <div class="row border">
      <div class="col border"><img class="test" :src="grade.img"> </div>
      <div class="col">
        <h3 class="text-center">{{grade.title}}</h3>
        <p style="width:50%;font-size: 10px">{{grade}}</p>S
      </div>

    </div>
      <button id="show-modal" @click="">Show Modal</button>
      <!-- use the modal component, pass in the prop -->
      <modal v-if="showModal" @close="showModal = false">
        <!--
      you can use custom content here to overwrite
      default content
    -->
        <h3 slot="header">custom header</h3>
      </modal>
  </div>
</template>

<script>
    import axios from "axios";
    import modal from './Modal'
    export default {
      components: {
        'modal' : modal
      },
        name: "Grade",
        data () {
          return {
          grade : [],
          showModal :false,
          }
        },
      created() {
          this.getApiData()
      },
      methods : {
           getApiData: function () {
        axios.get('http://localhost/api/grades/'+ this.$route.params.id + '/')
          .then( response => {
            this.grade = response.data
          });
      },
        }
    }
</script>

<style scoped>
.container {
  vertical-align: middle;
}
  .test{
    height:400px
  }
</style>
