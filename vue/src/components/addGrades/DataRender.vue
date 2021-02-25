<template>
<div class="container">
  <div class="row">
    <div class="col">
      <ul class="list-group">
        <li class="list-group-item-text" v-for="grade in grades">
          {{grade.title}}
        </li>
      </ul>
    </div>
  </div>
</div>
</template>

<script>
  import axios from 'axios'
    export default {
      name: "DataRender",
      data () {
        return {
          grades: []
        }
      },
      methods : {
          populateGrades () {
             axios.get('http://192.168.0.9:8000/api/grades/')
            .then( response => {
                this.grades = response.data
              });
          },
      },


      mounted() {
        this.populateGrades()
        this.$root.$on('populateGrades', () => {
        this.populateGrades()
      });
      }
    }
</script>

<style scoped>

</style>
