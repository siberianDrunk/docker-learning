<template>
  <div class="row">
    <div class="col">
      <app-input></app-input>
    </div>
    <div class="col">
      <app-data-render></app-data-render>
    </div>
  </div>

</template>

<script>
  import Input from './Input'
  import DataRender from "./DataRender";
    export default {
        name: "InputMain",
        components : {
          appInput : Input,
          appDataRender : DataRender
        }
    }
</script>

<style scoped>

</style>
