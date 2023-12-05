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
      <div class="w-full py-14 flex flex-row justify-center items-start pl-8 text-white">
        <div class="flex w-full self-center">
          <pre class="text-green text-4xl">
_______________
|,----------.  |\
||           |=| |
||          || | |
||       . _o| | | __
|`-----------' |/ /~/
 ~~~~~~~~~~~~~~~ / /
                 ~~
          </pre>
        </div>
        <div class="flex flex-col justify-center items-start gap-12 w-full">
          <TextLinkButton
            v-for="link in links"
            :key="link.url"
            :text="link.title"
            maxSymbols="21"
            @click="onLinkClick(link.url)"
          />
        </div>
      </div>
    </template>
  </TerminalWindow>
</template>
<script>
import TextLinkButton from '../../atoms/buttons/TextLinkButton.vue';
import TerminalText from '../../../components/general/TerminalText.vue';
import TerminalWindow from '../../../components/general/windows/TerminalWindow.vue';
import CloseIcon from '../../icons/CloseIcon.vue';

export default {
  name: 'WatchingList',
  components: { TerminalWindow, TerminalText, TextLinkButton, CloseIcon },
  props: ['text1', 'text2', 'text3', 'links'],
  data() {
    return {
      username: 'computer-graphics@watching',
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
