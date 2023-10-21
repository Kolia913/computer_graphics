<template>
  <button
    @mouseenter="isHover = true"
    @mouseleave="isHover = false"
    @click="onClick"
    class="text-white hover:text-primary h-20 duration-200"
  >
    <pre class="button-content"
      >{{ '#'.repeat(maxSymbols) }}
#{{ ' '.repeat(maxSymbols) }}#
{{ !isHover ? 0 : `&lt;` }}{{ content }}{{ !isHover ? 0 : `&gt;` }}
#{{ ' '.repeat(maxSymbols) }}#
{{ '#'.repeat(maxSymbols) }}
      </pre
    >
  </button>
</template>
<script>
export default {
  name: 'TextButton',
  props: ['text', 'maxSymbols'],
  computed: {
    content() {
      const textLength = this.text.length;

      const spaces = Math.floor((this.maxSymbols - textLength) / 2);

      return `${' '.repeat(spaces)}${this.text}${' '.repeat(spaces + 1)}`;
    },
  },
  data() {
    return {
      isHover: false,
    };
  },
  methods: {
    onClick() {
      this.$emit('click');
    },
  },
};
</script>
<style scoped lang="scss">
.button-content {
  line-height: 18px;
}
</style>
