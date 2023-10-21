<template>
  <button class="h-8 w-56 rounded-md bg-grey-light hover:bg-grey-light-darker" @click="onClick">
    <span>{{ text }}</span>
  </button>
</template>
<script>
export default {
  name: 'RegularButton',
  props: ['text'],
  methods: {
    onClick() {
      this.$emit('click');
    },
  },
};
</script>
<style scoped lang="scss"></style>
