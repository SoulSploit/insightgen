<template>
  <div id="app">
    <h1>Business Insights</h1>
    <Insights />
  </div>
</template>

<script>
import Insights from './components/Insights.vue'

export default {
  name: 'App',
  components: {
    Insights
  }
}
</script>