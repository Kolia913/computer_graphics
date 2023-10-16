<template>
  <main>
    <RouterView />
  </main>
</template>

<script>
import { RouterView } from 'vue-router'
export default {
  name: 'TerminalLayout',
  components: { RouterView }
}
</script>