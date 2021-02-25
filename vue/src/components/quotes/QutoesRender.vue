<template>
  <div>
  <div class="row mt-5">
    <div v-for="quote in quotes" class="col-md-3 mb-2 text-wrap text-break">
      <button @click.prevent="deleteQuote(quote)"class="btn border shadow-btn ">
        <p class="quote">{{quote}}</p>
      </button>
    </div>
  </div>
    <div class="row mt-3 text-center">
      <div class="alert alert-primary container-fluid" role="alert">
      Info: Click on quote to delete
    </div>
    </div>
   </div>
</template>

<script>
    export default {
      props: ['quotes'],
      name: "QutoesRender",

      methods: {
         deleteQuote (quote) {
          this.$root.$emit('deleteQuote', quote)
        }
      }
    }
</script>

<style scoped>
.shadow-btn {
  border: 1px solid black;
  box-shadow : 0 0 15px rgba(0.5,0,0,0.2);
  width: 100%;
  word-wrap: break-word;

}
button:hover {
  background-color: #dbabb5;

}
.quote {
  font-size: 20px;
  font-family: "Brush Script MT", cursive;
}
</style>
