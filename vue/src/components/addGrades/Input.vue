<template>
  <div class="container">
    <form @submit="formSubmit">
      <div class="form-group">
        <label for="inputGrade"></label>
        <input v-model="grade.title" type="text" class="form-control" id="inputGrade" placeholder="Введите название предмета">
      </div>
      <div class="form-group">
        <label for="directionSelect">Выберите направление</label>
        <select v-model="grade.direction_id" class="form-control" id="directionSelect">
          <option v-for="item in directions" :value="item.id">{{item.title}}</option>
        </select>
      </div>
        <div class="form-group">
        <label for="inputDesc">Описание предмета</label>
        <input v-model="grade.desc" type="text" class="form-control" id="inputDesc" placeholder="Введите описание">
      </div>
      <div class="form-group">
        <label for="exampleFormControlFile1">Загрузите картинку вашего предмета</label>
        <input type="file" class="form-control-file" @change="syncImage($event)" id="exampleFormControlFile1">
      </div>
      <button type="submit" class="btn btn-primary">Отправить предмет</button>
    </form>

  </div>
</template>

<script>
  import axios from 'axios'
    export default {
        name: "Input",
        data() {
          return {
            directions: [],
            grade: {
              title : '',
              direction_id: '',
              desc : '',
              img : null,
              position: 1
            }
          }
        },
        methods : {
          syncImage (event) {
            this.grade.img = event.target.files[0]
            console.log(this.grade)
          },
          populateDirections () {
             axios.get('http://192.168.0.9:8000/api/directions/')
            .then( response => {
                this.directions = response.data
              });
          },
          formSubmit(e) {
            e.preventDefault();
            let data = new FormData()
            data.append('title', this.grade.title)
            data.append('desc', this.grade.desc)
            data.append('direction_id', this.grade.direction_id)
            data.append('img', this.grade.img)
            data.append('position', this.grade.position)
            console.log(data.get('direction'))
            axios({
              method: 'post',
              url: 'http://192.168.0.9:8000/api/grades/',
              data
            }).then(response => {
              console.log(response);
              this.$root.$emit('populateGrades')
            })
            .catch(error => (console.log(error.response)))
          }
        },
        mounted () {
          this.populateDirections()
        },


    }
</script>

<style scoped>

</style>
