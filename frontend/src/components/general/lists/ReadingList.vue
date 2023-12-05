<template>
  <TerminalWindow :isClosable="true" :title="username" @onCloseClick="onCloseClick">
    <template #closeIcon>
      <div
        @click="onCloseClick"
        class="bg-red h-5 w-5 rounded-full flex items-center justify-center cursor-pointer"
      >
        <CloseIcon class="h-4 w-4" />
      </div>
    </template>
    <template #content>
      <TerminalText :user="username" :text="text1" />
      <TerminalText :user="username" :text="text2" class="max-w-4xl" />
      <TerminalText :user="username" :text="text3" />
      <div class="w-full py-14 flex flex-col gap-14 justify-start items-start pl-8 text-white">
        <div
          class="flex flex-row justify-start items-center gap-10 pl-20"
          v-for="link in links"
          :key="link.url"
        >
          <TextButton :text="link.title" maxSymbols="21" @click="onLinkClick(link.url)" />
          <p class="text-xl max-w-lg">
            {{ '-->' }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ link.description }}
          </p>
        </div>
      </div>
    </template>
  </TerminalWindow>
</template>
<script>
import TextButton from '../../../components/atoms/buttons/TextButton.vue';
import TerminalText from '../../../components/general/TerminalText.vue';
import TerminalWindow from '../../../components/general/windows/TerminalWindow.vue';
import CloseIcon from '../../icons/CloseIcon.vue';

export default {
  name: 'ReadingList',
  components: { TerminalWindow, TerminalText, TextButton, CloseIcon },
  props: ['text1', 'text2', 'text3', 'links'],
  data() {
    return {
      username: 'computer-graphics@reading',
    };
  },
  methods: {
    onCloseClick() {
      this.$emit('onCloseClick');
    },
    onLinkClick(url) {
      window.open(url, '_blank');
    },
  },
};
</script>
