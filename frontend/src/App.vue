<template>
  <component :is='layout'>
    <RouterView />
  </component>
</template>

<script>
import { RouterView } from 'vue-router'
export default  {
  name: 'App',
  components: {
    RouterView
  },
  computed: {
    layout() {
      return (this.$route.meta.layout || 'empty') + '-layout';
    }
  }
}
</script>