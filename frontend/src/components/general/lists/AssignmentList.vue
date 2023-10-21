<template>
  <TerminalWindow :isClosable="true" :title="username">
    <template #closeIcon>
      <div
        @click="onCloseClick"
        class="bg-red h-5 w-5 rounded-full flex items-center justify-center cursor-pointer"
      >
        <CloseIcon class="h-4 w-4" />
      </div>
    </template>
    <template #content>
      <TerminalText :user="username" text="echo assignment_info.txt" />
      <div class="w-full py-14 flex flex-row justify-center items-start pl-8 gap-20 text-white">
        <pre class="text-green text-4xl">
    \_/
  --(_)--  .
    / \   /_\
          |Q|
    .-----' '-----.
   /____[SCHOOL]___\
    | [] .-.-. [] |
  ..|____|_|_|____|
          </pre
        >
        <div>
          <pre class="w-full">
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
|<span class="text-green">$name_</span>  {{ name }}
~~~~~~~~~~~~~~~~~~~  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
|<span class="text-green">$goal_</span>  {{ goal }}
~~~~~~~~~~~~~~~~~~~  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|<span class="text-green">$task_</span>
<span v-for="(item, idx) in stepList" :key="idx"><pre>|        {{ idx +1 }}. {{ item }}</pre></span>   
~~~~~~~~~~~~~~~~~~~    
          </pre>
        </div>
      </div>
    </template>
  </TerminalWindow>
</template>
<script>
import CloseIcon from '../../icons/CloseIcon.vue';
import TerminalText from '../../../components/general/TerminalText.vue';
import TerminalWindow from '../../../components/general/windows/TerminalWindow.vue';

export default {
  name: 'WatchingList',
  components: { TerminalWindow, TerminalText, CloseIcon },
  props: ['name', 'goal', 'stepList'],
  data() {
    return {
      username: 'computer-graphics@assignment',
    };
  },
  methods: {
    onCloseClick() {
      this.$emit('onCloseClick');
    },
  },
};
</script>
