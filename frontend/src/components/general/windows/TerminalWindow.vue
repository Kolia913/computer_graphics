<template>
  <div
    class="max-w-7xl w-full terminal rounded-lg border border-solid border-terminal-stroke relative pt-10"
    :class="!!isTransparent ? 'bg-terminal/70' : 'bg-terminal/90'"
  >
    <div
      class="absolute top-0 left-0 bottom-0 h-10 w-full bg-terminal rounded-t-lg flex items-center border-b border-solid border-terminal-stroke"
      :class="isClosable ? 'justify-between' : 'justify-center'"
    >
      <div v-if="isClosable"></div>
      <div class="felx justify-center items-center">
        <span class="text-white text-xl">{{ title }}</span>
      </div>
      <div v-if="isClosable" class="pr-2">
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
  props: ['title', 'isClosable', 'isTransparent'],
};
</script>
<style>
.terminal {
  max-height: 820px;
}
</style>
