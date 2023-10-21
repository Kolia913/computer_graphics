<template>
  <p class="text-xl whitespace-normal text-white">
    <span class="text-green">{{ user }}</span
    >:<span class="text-blue">~</span>$&nbsp;
    {{ text }}
  </p>
</template>
<script>
export default {
  name: 'TerminalText',
  props: ['user', 'text'],
};
</script>
