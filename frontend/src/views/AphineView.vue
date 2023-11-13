<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <ProgramWindow
      title="Lab 4 - Aphine Transformations"
      :isClosable="false"
      :transparentHeader="visibleModal.length > 0"
    >
      <template #content>
        <div class="flex flex-row justify-center items-start w-full gap-4">
          <ProgramMenu @onBackClick="goBack" @onLinkClick="onLinkClick" />
          <div class="w-full flex justify-start items-center pt-3 h-full">
            <div class="colors-image flex justify-center items-center flex-1 text-gray-400">
              <img
                src="../assets/images/aphine.png"
                alt="Selected file will appear here:)"
                class="w-full h-full object-contain overflow-auto"
              />
            </div>
            <VeeForm
              class="felx flex-col justify-start items-center gap-y-4 w-1/3 flex-1/3"
              @submit="onSubmit"
              :validation-schema="validations"
              :initial-values="initialValues"
            >
              <div class="flex flex-row justify-start gap-10">
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">X1: </span>
                  <PlainInput name="x1" type="number" />
                </div>
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">Y1:</span>
                  <PlainInput name="y1" type="number" />
                </div>
              </div>
              <div class="flex flex-row justify-start gap-10 pt-4">
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">X2: </span>
                  <PlainInput name="x2" type="number" />
                </div>
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">Y2: </span>
                  <PlainInput name="y2" type="number" />
                </div>
              </div>
              <div class="pt-4">
                <span class="font-light underline underline-offset-2">Transformation:</span>
                <SelectInput class="mt-2" />
              </div>
              <div class="flex flex-row justify-start gap-10 pt-4">
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">X: </span>
                  <PlainInput name="x2" type="number" />
                </div>
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">Y: </span>
                  <PlainInput name="y2" type="number" />
                </div>
              </div>
              <div class="pt-4">
                <ActionButton text="Submit" type="submit" />
              </div>
            </VeeForm>
          </div>
        </div>
      </template>
    </ProgramWindow>
  </div>
  <div
    class="absolute top-0 left-0 right-0 bottom-0 flex justify-center items-center"
    v-if="visibleModal.length > 0"
  >
    <AssignmentList
      v-if="visibleModal === 'ai'"
      :name="modalsContent.assignmentIfno.name"
      :goal="modalsContent.assignmentIfno.goal"
      :step-list="modalsContent.assignmentIfno.stepList"
      @onCloseClick="onCloseClick"
      class="ml-20 -mt-4"
    />
    <ReadingList
      v-if="visibleModal === 'rl'"
      :text1="modalsContent.readingList.text1"
      :text2="modalsContent.readingList.text2"
      :text3="modalsContent.readingList.text3"
      :links="modalsContent.readingList.links"
      @onCloseClick="onCloseClick"
      class="ml-20 mt-8"
    />
    <WatchingList
      v-if="visibleModal === 'wl'"
      :text1="modalsContent.watchingList.text1"
      :text2="modalsContent.watchingList.text2"
      :text3="modalsContent.watchingList.text3"
      :links="modalsContent.watchingList.links"
      @onCloseClick="onCloseClick"
      class="ml-20 mt-8"
    />
  </div>
</template>
<script>
import ActionButton from '../components/atoms/buttons/ActionButton.vue';
import PlainInput from '../components/atoms/inputs/PlainInput.vue';
import ProgramMenu from '../components/general/ProgramMenu.vue';
import AssignmentList from '../components/general/lists/AssignmentList.vue';
import ReadingList from '../components/general/lists/ReadingList.vue';
import WatchingList from '../components/general/lists/WatchingList.vue';
import ProgramWindow from '../components/general/windows/ProgramWindow.vue';
import { mapActions, mapState } from 'pinia';
import useAphineStore from '../stores/aphine';
import { useToast } from 'vue-toastification';
import SelectInput from '../components/atoms/inputs/SelectInput.vue';

const toast = useToast();

export default {
  name: 'AphineView',
  components: {
    ProgramWindow,
    ProgramMenu,
    AssignmentList,
    WatchingList,
    ReadingList,
    ActionButton,
    PlainInput,
    SelectInput,
  },
  data() {
    return {
      initialValues: {
        x1: 0,
        y1: 0,
        x2: 0,
        y2: 0,
      },
      validations: {
        x1: 'required|min_value:0',
        x2: 'required|min_value:0',
        y1: 'required|min_value:0',
        y2: 'required|min_value:0',
        // file: 'required',
      },
      visibleModal: '',
      options: [],
      modalsContent: {
        assignmentIfno: {
          name: 'Lab 4. Build Aphine moves for Lab 4',
          goal: 'To have the best fractal at the world   ',
          stepList: [
            'Build frontend',
            'Build backend',
            'Vizualize fractal',
            'Prepare the best report',
            'Get max mark',
          ],
        },
        readingList: {
          text1: 'Here we go again! It is never too late to study new staff.',
          text2:
            'This is a page, that will help you to get familiar with all the theoretic data you need to understand the task.',
          text3: 'Please select the link you want to open:',
          links: [
            {
              title: 'Fractals',
              url: '#',
              description:
                'This page contains general data what fractals are and where can them be useful.',
            },
            {
              title: 'Math',
              url: '#',
              description:
                'This page contains data about basic math knowledge required to understand what is going on here',
            },
            {
              title: 'Code',
              url: '#',
              description:
                'This page contains data about technologies used to build such a great fractal :)',
            },
          ],
        },
        watchingList: {
          text1: 'It is never too late to study. But let’s now do it another way!',
          text2:
            'This is a page, that will help you to get familiar with all the theoretic data you need to understand the task by watching and listening to it.',
          text3: 'Please select the link you want to open:',
          links: [
            {
              title: 'Intro to Computer Graphics',
              url: '#',
            },
            {
              title: 'Intro to Fractals Theory',
              url: '#',
            },
            {
              title: 'Intro to Fractals Vizualization',
              url: '#',
            },
          ],
        },
      },
    };
  },
  computed: {},
  methods: {
    changeScheme(value) {
      this.colorScheme = value;
    },
    onSubmit(values) {},

    goBack() {
      this.$router.back();
    },
    onLinkClick(type) {
      this.visibleModal = type;
    },
    onCloseClick() {
      this.visibleModal = '';
    },
  },
};
</script>
<style scoped lang="scss">
.colors-image {
  height: 486px;
}
</style>
