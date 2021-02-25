<template>
  <div  class="container quotesBody mt-5">
      <app-progress :quotes-length="quotes.length"></app-progress>
      <app-input></app-input>
      <app-render :quotes="quotes"></app-render>
  </div>
</template>



<script>
  import Progress from './Progress'
  import QuotesInput from './QuotesInput'
  import QuotesRender from './QutoesRender'


    export default {
      components: {
        'appProgress': Progress,
        'appInput': QuotesInput,
        'appRender': QuotesRender,
      },
      name: "QuotesMain",
      data () {
        return{
          quotes: []
        }
      },
      methods : {
        submitQuote (quote) {
          if(this.quotes.length < 10) {
            if (quote != ''){
              this.quotes.push(quote)
            } else {
              alert('Your input is empty')
            }
          } else{
            alert('You have submit 10 quotes already')
          }
        },
        deleteQuote(quote) {
          this.quotes.splice(this.quotes.indexOf(quote), 1);
        }
      },
      created() {
        this.$root.$on('submitQuote', (quote) => {
        this.submitQuote(quote)
      });
        this.$root.$on('deleteQuote', (quote) => {
        this.deleteQuote(quote)
      });

      }
    }
</script>

<style scoped>
  .quotesBody {
  }
</style>
