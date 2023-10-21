<template>
  <button
    class="h-8 w-56 border border-solid border-stroke rounded-md flex justify-center items-center text-center bg-gradient-to-b from-grey-light/0 to-grey-light hover:from-grey-light/0 hover:via-grey-light hover:to-grey-light"
    @click="onCLick"
  >
    <span>{{ text }}</span>
  </button>
</template>
<script>
export default {
  name: 'OutlineButton',
  props: ['text'],
  methods: {
    onCLick() {
      this.$emit('click');
    },
  },
};
</script>
<style scoped lang="scss"></style>
