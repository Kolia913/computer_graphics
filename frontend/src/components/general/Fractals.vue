<template>
  <div class="flex flex-col justify-start items-start w-full">
    <div class="flex flex-row justify-start items-end">
      <div
        class="border border-solid border-stroke border-b-0 rounded-tl-md bg-white cursor-pointer px-4 py-0.5 hover:text-white hover:bg-primary"
      >
        <span class="font-light underline underline-offset-2">Mandelbrot</span>
      </div>
      <div
        class="border border-l-0 border-b-0 border-solid border-stroke rounded-tr-md bg-white cursor-pointer px-4 py-0.5 hover:text-white hover:bg-primary"
      >
        <span class="font-light underline underline-offset-2">Zhulin</span>
      </div>
    </div>
    <div
      class="bg-white w-full fractal-image rounded-md border border-solid border-stroke rounded-tl-none p-3"
    >
      <img src="../../assets/images/fractal.png" class="w-full h-full" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'Fractals',
};
</script>
<style scoped lang="scss">
.fractal-image {
  height: 424px;
}
</style>
