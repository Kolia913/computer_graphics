<template>
  <button
    @click="onClick"
    class="bg-primary hover:bg-primary-dark text-white rounded-md h-8 w-56 flex flex-row justify-center items-center gap-2"
  >
    <div class="h-5 w-5">
      <slot></slot>
    </div>
    <span>
      {{ text }}
    </span>
  </button>
</template>
<script>
export default {
  name: 'ActionButton',
  props: ['text'],
  methods: {
    onClick() {
      this.$emit('click');
    },
  },
};
</script>
<style scoped lang="scss"></style>
