<template>
  <div class="flex flex-row justify-center">
    <button
      type="button"
      :class="
        this.selectedVariant === 'hsv'
          ? 'rounded-md bg-primary w-20 text-white -mr-1 p-2 z-10'
          : 'p-2 rounded-tl-md rounded-bl-md border border-solid border-stroke border-r-0 w-20 bg-white z-5'
      "
      @click="onHsvClick"
    >
      HSV
    </button>
    <button
      type="button"
      :class="
        this.selectedVariant === 'rgb'
          ? 'rounded-md bg-primary w-20 text-white p-2 z-10 -mr-1 -ml-1'
          : 'p-2 border border-solid border-stroke w-20 bg-white z-5'
      "
      @click="onRgbClick"
    >
      RGB
    </button>
    <button
      type="button"
      :class="
        this.selectedVariant === 'cmyk'
          ? 'rounded-md bg-primary w-20 text-white -ml-1 p-2 z-10'
          : 'p-2 rounded-tr-md rounded-br-md border border-l-0 border-solid border-stroke w-20 bg-white z-5 '
      "
      @click="onCmykClick"
    >
      CMYK
    </button>
  </div>
</template>
<script>
export default {
  name: 'SwitchButton',
  props: ['value'],
  data() {
    return {
      variants: ['hsv', 'cmyk', 'rgb'],
      selectedVariant: this.value ? this.value : 'rgb',
    };
  },
  watch: {
    value(e) {
      this.selectedVariant = e;
    },
  },
  methods: {
    onHsvClick() {
      this.selectedVariant = this.variants[0];
      this.$emit('schemeChange', this.selectedVariant);
    },
    onCmykClick() {
      this.selectedVariant = this.variants[1];
      this.$emit('schemeChange', this.selectedVariant);
    },
    onRgbClick() {
      this.selectedVariant = this.variants[2];
      this.$emit('schemeChange', this.selectedVariant);
    },
  },
};
</script>
<style lang="scss" scoped></style>
