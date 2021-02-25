<template>
<div class="container">
  <nav class="navbar bg-transparent fixed-top navbar-light bg-primary">
    <a class="navbar-brand" href="">Deep SFU</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="text-dark navbar-light navbar-toggler-icon border-dark"></span>
    </button>
    <div class="collapse navbar-collapse  text-dark " id="navbarSupportedContent">
      <ul class="col navbar-nav " >
         <li class="nav-item text-dark">
          <router-link class="nav-link text-dark" to="/sticky">Old version</router-link>
        </li>
      </ul>
    </div>
  </nav>
 </div>
</template>

<script>

  export default {
    name: "Navbar",
   watch: {
    '$route' () {
      $('#navbarSupportedContent').collapse('hide');
      console.log('Hide collapse')
    }
  }
  }
</script>

<style scoped>
  span {
    font-size: 10px
  }
</style>
