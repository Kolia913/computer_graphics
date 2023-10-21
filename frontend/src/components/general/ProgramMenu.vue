<template>
  <div
    class="flex flex-col justify-between items-start menu bg-white p-5 w-fit rounded-md border border-solid border-stroke"
  >
    <ul class="flex flex-col justify-start items-start gap-3">
      <li
        v-for="link in menuItems"
        :key="link.type"
        class="flex flex-row justify-start items-center gap-2 cursor-pointer"
      >
        <div class="w-5 h-5 pt-0.5">
          <component :is="{ ...link.icon }" />
        </div>
        <span class="text-xl font-light border-b border-secondary text-secondary">{{
          link.title
        }}</span>
      </li>
    </ul>
    <OutlineButton text="<- back" @click="onBackBtnClick" />
  </div>
</template>
<script>
import OutlineButton from '../atoms/buttons/OutlineButton.vue';
import BookIcon from '../icons/BookIcon.vue';
import InfoIcon from '../icons/InfoIcon.vue';
import PlayIcon from '../icons/PlayIcon.vue';

export default {
  name: 'ProgramMenu',
  components: { InfoIcon, OutlineButton },
  data() {
    return {
      menuItems: [
        {
          title: 'assignment info',
          type: 'ai',
          icon: InfoIcon,
        },
        {
          title: 'reading list',
          type: 'rl',
          icon: BookIcon,
        },
        {
          title: 'watching list',
          type: 'wl',
          icon: PlayIcon,
        },
      ],
    };
  },
  methods: {
    onBackBtnClick() {
      this.$emit('onBackClick');
    },
  },
};
</script>
<style scoped lang="scss">
.menu {
  height: 680px;
}
</style>
