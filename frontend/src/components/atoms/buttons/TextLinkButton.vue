<template>
  <button
    @mouseenter="isHover = true"
    @mouseleave="isHover = false"
    @click="onClick"
    class="text-white hover:text-primary duration-200 w-fit h-fit"
  >
    <pre class="button-content text-left">

 ###############
#
#      {{ isHover ? '>>' : '' }} {{ text }}   
#
################
      </pre
    >
  </button>
</template>
<script>
export default {
  name: 'TextLinkButton',
  props: ['text'],
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
