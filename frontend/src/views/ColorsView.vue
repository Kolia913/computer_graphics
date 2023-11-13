<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <ProgramWindow
      title="Lab 3 - Color Scheme"
      :isClosable="false"
      :transparentHeader="visibleModal.length > 0"
    >
      <template #content>
        <div class="flex flex-row justify-center items-center w-full gap-4">
          <ProgramMenu @onBackClick="goBack" @onLinkClick="onLinkClick" />
          <div class="w-full flex justify-start items-center pt-3 h-full">
            <div class="colors-image flex justify-center items-center flex-1 text-gray-400">
              <img
                :src="imageBase64"
                alt="Selected file will appear here:)"
                class="w-full h-full object-contain overflow-auto"
              />
            </div>
            <VeeForm
              class="felx flex-col justify-start items-center gap-y-4 w-1/4 flex-1/4"
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
              <div class="pt-6">
                <div class="flex justify-between pb-2">
                  <span class="font-light underline underline-offset-2">Saturation:</span>
                  <span class="bg-gray-300 px-2">{{ saturation }}</span>
                </div>
                <SliderInput @onChange="changeSaturation" />
              </div>
              <div class="pt-6">
                <div class="flex justify-between pb-2">
                  <span class="font-light underline underline-offset-2">Lightness:</span>
                  <span class="bg-gray-300 px-2">{{ lightness }}</span>
                </div>
                <SliderInput @onChange="changeLightness" />
              </div>
              <div class="pt-8">
                <SwitchButton @schemeChange="changeScheme" :value="colorScheme" />
              </div>
              <div class="pt-10">
                <RegularButton text="Choose image" @click="openFileDialog" />
                <input
                  class="hidden"
                  type="file"
                  @change="changeFile"
                  ref="fileInput"
                  accept="image/png, image/jpeg"
                />
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
import RegularButton from '../components/atoms/buttons/RegularButton.vue';
import SwitchButton from '../components/atoms/buttons/SwitchButton.vue';
import PlainInput from '../components/atoms/inputs/PlainInput.vue';
import SliderInput from '../components/atoms/inputs/SliderInput.vue';
import ProgramMenu from '../components/general/ProgramMenu.vue';
import AssignmentList from '../components/general/lists/AssignmentList.vue';
import ReadingList from '../components/general/lists/ReadingList.vue';
import WatchingList from '../components/general/lists/WatchingList.vue';
import ProgramWindow from '../components/general/windows/ProgramWindow.vue';
import { mapActions, mapState } from 'pinia';
import useColorsStore from '../stores/colors';
import { useToast } from 'vue-toastification';

const toast = useToast();

export default {
  name: 'ColorsView',
  components: {
    ProgramWindow,
    ProgramMenu,
    AssignmentList,
    WatchingList,
    ReadingList,
    SliderInput,
    RegularButton,
    ActionButton,
    PlainInput,
    SwitchButton,
  },
  data() {
    return {
      initialValues: {
        x1: 0,
        y1: 0,
        x2: 0,
        y2: 0,
        file: null,
      },
      previewBase64: '',
      saturation: 0,
      lightness: 0,
      colorScheme: 'hsv',
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
          name: 'Lab 3. Build color schemes for Lab 3',
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
  computed: {
    ...mapState(useColorsStore, ['imageBase64']),
  },
  methods: {
    changeSaturation(value) {
      this.saturation = value;
    },
    changeLightness(value) {
      this.lightness = value;
    },
    changeScheme(value) {
      this.colorScheme = value;
    },
    onSubmit(values) {
      if (!this.file) {
        toast.error('Please select file');
        return;
      }
      try {
        this.sendImageWithChanges({
          ...values,
          saturation: this.saturation,
          lightness: this.lightness,
          file: this.file,
          scheme: this.colorScheme,
        }).then(() => {
          toast.success('Congrats!');
        });
      } catch (e) {
        toast.error(e.message ? e.message : 'Invalid form data!');
      }
    },
    async changeFile(event) {
      this.file = event.target.files[0];
      const previewBase64 = await this.toBase64(this.file);
      this.changeImageBase64(previewBase64);
    },
    toBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        if (!file) {
          return alert(`You have to choose file!`);
        }
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
      });
    },
    openFileDialog() {
      this.$refs.fileInput.click();
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
    ...mapActions(useColorsStore, ['sendImageWithChanges', 'changeImageBase64']),
  },
};
</script>
<style scoped lang="scss">
.colors-image {
  height: 486px;
}
</style>
