<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <ProgramWindow
      title="Lab 2 - Fractals"
      :isClosable="false"
      :transparentHeader="visibleModal.length > 0"
    >
      <template #content>
        <div class="flex flex-row justify-center items-start w-full gap-4">
          <ProgramMenu @onBackClick="goBack" @onLinkClick="onLinkClick" />
          <div class="w-full">
            <Fractals :image="fractalImage" @onFractalSelect="selectFractal" />
            <div class="pt-2">
              <SliderInput />
            </div>
            <VeeForm
              @submit="onSubmit"
              :validation-schema="schema"
              class="pt-8 flex flex-row justify-between"
            >
              <div class="flex flex-col justify-start items-stretch gap-4">
                <div
                  class="flex flex-row justify-between items-center gap-8"
                  v-if="currentFractal !== 'vicsek'"
                >
                  <span class="text-lg font-light underline underline-offset-2">Iterations:</span>
                  <div>
                    <PlainInput name="iterations" type="number" @onChange="iterationsChange" />
                  </div>
                </div>
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Colour:</span>
                  <div>
                    <SelectInput :options="options" @onChange="colorChange" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-start items-stretch gap-4">
                <div
                  class="flex flex-row justify-between items-center gap-8"
                  v-if="currentFractal === 'julia'"
                >
                  <span class="text-lg font-light underline underline-offset-2">Reals C:</span>
                  <div>
                    <PlainInput name="real_c" type="number" @onChange="realCChange" />
                  </div>
                </div>
                <div
                  class="flex flex-row justify-between items-center gap-8"
                  v-if="currentFractal === 'julia'"
                >
                  <span class="text-lg font-light underline underline-offset-2">Imag C:</span>
                  <div>
                    <PlainInput name="imag_c" type="number" @onChange="imagCChange" />
                  </div>
                </div>
                <div
                  class="flex flex-row justify-between items-center gap-8"
                  v-if="currentFractal === 'vicsek'"
                >
                  <span class="text-lg font-light underline underline-offset-2">Levels:</span>
                  <div>
                    <PlainInput name="levels" type="number" @onChange="levelsChange" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-between items-start">
                <!-- <span class="text-base font-light underline underline-offset-4">
                  Fractal formula:<br />f(z) = z * z + c</span
                > -->
                <ActionButton text="Save to file...">
                  <SaveIcon />
                </ActionButton>
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
import SelectInput from '../components/atoms/inputs/SelectInput.vue';
import SliderInput from '../components/atoms/inputs/SliderInput.vue';
import Fractals from '../components/general/Fractals.vue';
import ProgramMenu from '../components/general/ProgramMenu.vue';
import AssignmentList from '../components/general/lists/AssignmentList.vue';
import ReadingList from '../components/general/lists/ReadingList.vue';
import WatchingList from '../components/general/lists/WatchingList.vue';
import ProgramWindow from '../components/general/windows/ProgramWindow.vue';
import SaveIcon from '../components/icons/SaveIcon.vue';
import { mapActions, mapState } from 'pinia';
import useFractalsStore from '../stores/fractals';

export default {
  name: 'FractalView',
  components: {
    ProgramWindow,
    ProgramMenu,
    Fractals,
    SliderInput,
    PlainInput,
    SelectInput,
    ActionButton,
    SaveIcon,
    AssignmentList,
    WatchingList,
    ReadingList,
  },
  data() {
    return {
      schema: {
        iterations: 'required|min_value:1|max_value:9999',
        levels: 'required|min_value:1|max_value:5',
        real_c: 'required|min_value:1|max_value:9999',
        imag_c: 'required|min_value:1|max_value:9999',
      },
      visibleModal: '',
      options: [],
      modalsContent: {
        assignmentIfno: {
          name: 'Lab 2. Build fractal for Lab 2',
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
    ...mapState(useFractalsStore, [
      'colorsSchemes',
      'currentFractal',
      'mandelbrotImage',
      'juliaImage',
      'vicsekImage',
    ]),
    fractalImage() {
      if (this.currentFractal === 'mandelbrot') {
        return this.mandelbrotImage;
      } else if (this.currentFractal === 'juila') {
        return this.juliaImage;
      } else {
        return this.mandelbrotImage;
      }
    },
  },
  mounted() {
    this.getColorSchemes().then((res) => {
      console.log(res);
    });
  },
  methods: {
    async selectFractal(fractal) {
      switch (fractal) {
        case 'vicsek':
          this.setCurrentFractal({ currentFractal: 'vicsek' });
          await this.getVicsek({
            levels: 5,
          });
          break;
        case 'julia':
          this.setCurrentFractal({ currentFractal: 'julia' });
          await this.getJulia({
            max_iterations: 1000,
            zoom_percentage: 0.3,
            color_map: 'hot',
            c_real: -0.7,
            c_imag: 0.4,
            save_to_file: false,
          });
          break;
        default:
          this.setCurrentFractal({ currentFractal: 'mandelbrot' });
          await this.getMandlebrot({
            max_iterations: 100,
            zoom_percentage: 0,
            color_map: 'hot',
            save_to_file: false,
          });
          break;
      }
    },
    iterationsChange(value) {
      console.log(value);
    },
    colorChange(value) {
      console.log(value);
    },
    realCChange(value) {
      console.log(value);
    },
    imagCChange(value) {
      console.log(value);
    },
    levelsChange(value) {
      console.log(value);
    },
    goBack() {
      this.$router.back();
    },
    onSubmit(values) {
      console.log(values);
    },
    onLinkClick(type) {
      this.visibleModal = type;
    },
    onCloseClick() {
      this.visibleModal = '';
    },
    ...mapActions(useFractalsStore, [
      'getColorSchemes',
      'getMandlebrot',
      'getJulia',
      'getVicsek',
      'setCurrentFractal',
    ]),
  },
};
</script>
