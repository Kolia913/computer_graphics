<template>
  <div class="flex flex-col justify-start items-start w-full">
    <div class="flex flex-row justify-start items-end">
      <div
        class="border border-solid border-stroke border-b-0 rounded-tl-md cursor-pointer px-4 py-0.5 hover:text-white hover:bg-primary"
        :class="fractal === 'mandelbrot' ? 'text-white bg-primary' : 'bg-white'"
        @click="onFractalSelect('mandelbrot')"
      >
        <span class="font-light underline underline-offset-2">Mandelbrot</span>
      </div>
      <div
        class="border border-l-0 border-b-0 border-solid border-stroke cursor-pointer px-4 py-0.5 hover:text-white hover:bg-primary"
        :class="fractal === 'vicsek' ? 'text-white bg-primary' : 'bg-white'"
        @click="onFractalSelect('vicsek')"
      >
        <span class="font-light underline underline-offset-2">Vicsek</span>
      </div>
      <div
        class="border border-l-0 border-b-0 border-solid border-stroke rounded-tr-md cursor-pointer px-4 py-0.5 hover:text-white hover:bg-primary"
        :class="fractal === 'julia' ? 'text-white bg-primary' : 'bg-white'"
        @click="onFractalSelect('julia')"
      >
        <span class="font-light underline underline-offset-2">Zhulin</span>
      </div>
    </div>
    <div
      class="bg-white w-full fractal-image rounded-md border border-solid border-stroke rounded-tl-none p-3"
    >
      <img :src="image" class="w-full h-full object-contain overflow-scroll" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'Fractals',
  props: ['image'],
  data() {
    return {
      fractal: 'mandelbrot',
    };
  },
  methods: {
    onFractalSelect(fractal) {
      this.fractal = fractal;

      this.$emit('onFractalSelect', fractal);
    },
  },
};
</script>
<style scoped lang="scss">
.fractal-image {
  height: 446px;
}
</style>
