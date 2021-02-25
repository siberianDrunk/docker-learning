<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-md-8 text-input">
        <p>Quote</p>
        <div class="input-group">
          <textarea  v-model="quote" class="form-control" aria-label="With textarea"></textarea>
        </div>
      </div>
    </div>
      <div class="row mt-2 align-content-center d-flex justify-content-center">
        <div class="col-md-8 d-flex justify-content-center ">
           <button class="btn btn-primary btn-input" @click.prevent="submitQuote">Add Quote</button>
        </div>
      </div>

    </div>

</template>

<script>
    export default {
      name: "QuotesInput",
      data () {
        return {
          quote : ''
        }
      },
      methods: {
        submitQuote () {
          this.$root.$emit('submitQuote', this.quote)
          this.quote = ''
        }
      }
    }
</script>

<style scoped>
.text-input {
  margin: auto;
}
  .button-input {
    margin: auto;
  }
</style>
