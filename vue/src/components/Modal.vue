<template>
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">
              <div class="modal-header text-wrap">
                  <div class="col"><h3 class="modal-title">{{data.title}}</h3></div>
              </div>
              <div class="modal-body">
                  <div class="col text-center"><p style="font-style:italic">{{data.desc}}</p></div>
              </div>
              <div class="modal-footer">
                <slot name="footer">
                  <button class="modal-default-button btn" @click="$emit('close')">
                    Close
                  </button>
                </slot>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </template>

    <script>
        export default {
          name: 'modal',

          props: {
            data : '',
          },

        };
    </script>


<style lang="css">
  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: table;
    transition: opacity 0.3s ease;
  }

  .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
  }

  .modal-container {
    width: 300px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;
    font-family: Helvetica, Arial, sans-serif;
  }

  .modal-header  {
    margin-top: 0;
    color: #42b983;
    text-align: center;
  }

  .modal-body {
    margin: 20px 0;
  }

  .modal-default-button {
    float: right;
  }

  .modal-enter {
    opacity: 0;
  }
  .modal-enter-active {
    transition: opacity 0.5s;
  }
  .modal-leave {

  }
  .modal-leave-active {
    transition: opacity 0.5s;
    opacity: 0;
  }

  .modal-enter-active, .modal-enter .modal-container,
  .modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
  }
  .modal-title {
    font-size: 1.3rem;
    text-align: center;
  }

</style>
