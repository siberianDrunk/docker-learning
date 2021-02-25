<template>
  <div class="container">
    <div class="row">
      <div class="col-xs-12">
        <h3>Quotes Added</h3>
      </div>
    </div>
      <div class="row">
        <div class="progress">
          <div class="progress-bar bg-info" role="progressbar" :style="{width: quotesLength * 10 +'%'}" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"><span>{{quotesLength}}/10</span></div>
        </div>
      </div>
    </div>

</template>

<script>
    export default {
        props: ['quotesLength'],
        name: "Progress"
    }
</script>

<style scoped>
.progress {
  height: 20px
}
</style>
