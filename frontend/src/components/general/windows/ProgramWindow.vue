<template>
  <div
    class="max-w-7xl w-full terminal rounded-lg rounded-t-none bg-milk border border-solid border-terminal-stroke relative mt-10"
  >
    <div
      class="absolute -top-10 left-0 bottom-0 h-10 w-full rounded-t-lg flex justify-center items-center border-b border-solid border-terminal-stroke"
      :class="transparentHeader ? 'bg-terminal/70' : 'bg-terminal'"
    >
      <div v-if="isClosable"></div>
      <div class="felx justify-center items-center">
        <span class="text-white text-xl">{{ title }}</span>
      </div>
      <div v-if="isClosable">
        <slot name="closeIcon"></slot>
      </div>
    </div>
    <div class="flex flex-col justify-start items-start p-4 pt-6">
      <slot name="content"></slot>
    </div>
  </div>
</template>
<script>
export default {
  name: 'TerminalWindow',
  props: ['title', 'isClosable', 'transparentHeader'],
};
</script>
<style>
.terminal {
  max-height: 820px;
}
</style>
