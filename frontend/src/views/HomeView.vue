<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <TerminalWindow :isClosable="false" title="computer-graphics@labs" isTransparent>
      <template #content>
        <TerminalText :user="username" :text="'Hello World!'" />
        <TerminalText
          :user="username"
          :text="'This website is created by Roman and Mykola to demonstrate our knowledges in computer graphics'"
          class="max-w-4xl"
        />
        <TerminalText :user="username" :text="'Please select lab that you wand to see:'" />
        <div class="w-full py-14 flex flex-col gap-14 justify-start items-start pl-8 text-white">
          <div class="flex flex-row justify-start items-center gap-10">
            <TextButton text="Fractals" maxSymbols="21" @click="onFractalsClick" />
            <p class="text-xl">
              {{ '-->' }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This lab is about implementing design
              and some other stuff
            </p>
          </div>
          <div class="flex flex-row justify-start items-center gap-10">
            <TextButton text="Color Scheme" maxSymbols="21" @click="onColorsClick" />
            <p class="text-xl">
              {{ '-->' }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This lab is about implementing design
              and some math stuff
            </p>
          </div>
          <div class="flex flex-row justify-start items-center gap-10">
            <TextButton text="Rectangle Move" maxSymbols="21" />
            <p class="text-xl">
              {{ '-->' }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This lab is about implementive aphine
              movements
            </p>
          </div>
        </div>
      </template>
    </TerminalWindow>
  </div>
</template>

<script>
import TextButton from '../components/atoms/buttons/TextButton.vue';
import TerminalText from '../components/general/TerminalText.vue';
import TerminalWindow from '../components/general/windows/TerminalWindow.vue';

export default {
  name: 'HomeView',
  components: { TerminalWindow, TerminalText, TextButton },
  data() {
    return {
      username: 'computer-graphics@labs',
    };
  },
  methods: {
    onFractalsClick() {
      this.$router.push('/fractals');
    },
    onColorsClick() {
      this.$router.push('/colors');
    },
  },
};
</script>
