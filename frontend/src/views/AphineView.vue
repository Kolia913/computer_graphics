<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <ProgramWindow
      title="Lab 4 - Aphine Transformations"
      :isClosable="false"
      :transparentHeader="visibleModal.length > 0"
    >
      <template #content>
        <div class="flex flex-row justify-center items-center w-full gap-4">
          <ProgramMenu @onBackClick="goBack" @onLinkClick="onLinkClick" />
          <div class="w-full flex justify-start items-center pt-3 h-full">
            <div class="colors-image flex justify-center items-center flex-1 text-gray-400">
              <img
                :src="aphineChart"
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
              <div class="pt-4 w-1/2">
                <span class="font-light underline underline-offset-2">Transformation:</span>
              </div>
              <div class="flex flex-col justify-start gap-10 pt-4">
                <div class="flex flex-row justify-between gap-2 flex-wrap">
                  <span>Shift top: </span>
                  <PlainInput name="move_top" type="number" />
                </div>
                <div class="flex flex-row justify-between gap-2 flex-wrap">
                  <span>Shift right: </span>
                  <PlainInput name="move_right" type="number" />
                </div>
              </div>
              <div class="pt-4 w-1/2">
                <span class="font-light underline underline-offset-2">Scale:</span>
              </div>
              <div class="flex flex-row justify-start gap-10 pt-4">
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">A: </span>
                  <PlainInput name="scale_a" type="number" />
                </div>
                <div class="flex flex-row justify-start gap-4">
                  <span class="w-4">D: </span>
                  <PlainInput name="scale_d" type="number" />
                </div>
              </div>
              <div class="pt-4 w-1/2">
                <span class="font-light underline underline-offset-2">Rotation:</span>
              </div>
              <div class="flex flex-col justify-start gap-10 pt-4">
                <div class="flex flex-row justify-between gap-2 flex-wrap">
                  <span class="w-6">Angle: </span>
                  <PlainInput name="rotation" type="number" />
                </div>
              </div>
              <div class="pt-4">
                <ActionButton text="Apply" type="submit" class="w-full" />
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
  },
  data() {
    return {
      initialValues: {
        x1: 0,
        y1: 0,
        x2: 0,
        y2: 0,
        move_top: 0,
        move_right: 0,
        scale_a: 0,
        scale_d: 0,
        rotation: 0,
      },
      validations: {
        x1: 'required',
        x2: 'required',
        y1: 'required',
        y2: 'required',
        move_top: 'required',
        move_right: 'required',
        scale_a: 'required',
        scale_d: 'required',
        rotation: 'required',
      },
      visibleModal: '',
      options: [],
      modalsContent: {
        assignmentIfno: {
          name: 'Lab 4. Build Affine moves for Lab 4',
          goal: 'To have the best affine moves at the world   ',
          stepList: [
            'Build frontend',
            'Build backend',
            'Vizualize affine transforms.',
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
              title: 'Affine Transformation',
              url: 'https://www.machinelearningplus.com/linear-algebra/affine-transformation/',
              description: 'A Comprehensive Guide on Affine Transformation in Linear Algebra',
            },
            {
              title: 'Affine Transformation 2.0',
              url: 'https://www.mathworks.com/discovery/affine-transformation.html',
              description: 'What Is an Affine Transformation?',
            },
            {
              title: 'Affine Transformation 3.0',
              url: 'https://www.mathworks.com/discovery/affine-transformation.html',
              description: 'Illustrates the different affine transformations',
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
              title: '3x3 Image Transformations',
              url: 'https://youtu.be/B8kMB6Hv2eI?si=YzlQggalfWqX78dl',
            },
            {
              title: 'What are affine transformations?',
              url: 'https://youtu.be/E3Phj6J287o?si=SX2LBeOjDmfRQeBl',
            },
            {
              title: 'Affine transformations in 5 minutes',
              url: 'https://youtu.be/AheaTd_l5Is?si=aihLQJekkTJKW24_',
            },
          ],
        },
      },
    };
  },
  computed: {
    ...mapState(useAphineStore, ['aphineChart']),
  },
  methods: {
    changeScheme(value) {
      this.colorScheme = value;
    },
    onSubmit(values) {
      this.getAphineChart({ ...values })
        .then(() => {
          toast.success('Congrats!');
        })
        .catch((err) => {
          toast.error(err.response.data.error.message);
        });
    },

    goBack() {
      this.$router.back();
    },
    onLinkClick(type) {
      this.visibleModal = type;
    },
    onCloseClick() {
      this.visibleModal = '';
    },
    ...mapActions(useAphineStore, ['getAphineChart']),
  },
};
</script>
<style scoped lang="scss">
.colors-image {
  height: 486px;
}
</style>
