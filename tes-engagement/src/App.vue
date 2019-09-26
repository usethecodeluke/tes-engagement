<template>
  <div id="app">
    <section class="hero grad is-fullheight is-bold">
      <div class="hero-head">
        <header class="navbar">
          <div class="container">
            <div class="navbar-brand">
              <h3 class="navbar-item title is-italic has-text-white" href="../">
                rackers 4 rackers
              </h3>
            </div>
          </div>
        </header>
      </div>
      <div class="hero-body">
        <div class="container has-text-centered">
          <FeedbackForm/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import FeedbackForm from './components/FeedbackForm.vue'

export default {
  name: 'app',
  components: {
    FeedbackForm
  }
}
</script>

<style>
.grad {
  background: rgb(235,1,2);
  background: linear-gradient(146deg, rgba(235,1,2,1) 0%, rgba(53,0,251,1) 100%);
}
</style>
