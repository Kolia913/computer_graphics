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
            <Fractals
              :image="'data:image/png;base64, ' + fractalImage"
              @onFractalSelect="selectFractal"
            />

            <div class="pt-2">
              <SliderInput @onChange="zoomChange" />
            </div>
            <VeeForm
              @submit="onSubmit"
              :validation-schema="jScheme"
              class="pt-8 flex flex-row justify-between"
              v-if="currentFractal === 'julia'"
              :initial-values="{ iterations: 100, real_c: -0.7, imag_c: 0.4 }"
            >
              <div class="flex flex-col justify-start items-stretch gap-4">
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Iterations:</span>
                  <div>
                    <PlainInput name="iterations" type="number" />
                  </div>
                </div>
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Colour:</span>
                  <div>
                    <SelectInput :options="colorsSchemes" @onChange="colorChangeJ" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-start items-stretch gap-4">
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Reals C:</span>
                  <div>
                    <PlainInput name="real_c" type="number" />
                  </div>
                </div>
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Imag C:</span>
                  <div>
                    <PlainInput name="imag_c" type="number" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-between items-start">
                <ActionButton text="Submit" type="submit">
                  <SaveIcon />
                </ActionButton>
              </div>
            </VeeForm>
            <VeeForm
              @submit="onSubmit"
              :validation-schema="mScheme"
              class="pt-8 flex flex-row justify-between"
              :initial-values="{ iterations: 100 }"
              v-if="currentFractal === 'mandelbrot'"
            >
              <div class="flex flex-col justify-start items-stretch gap-4">
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Iterations:</span>
                  <div>
                    <PlainInput name="iterations" type="number" />
                  </div>
                </div>
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Colour:</span>
                  <div>
                    <SelectInput :options="colorsSchemes" @onChange="colorChangeM" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-between items-start">
                <!-- <span class="text-base font-light underline underline-offset-4">
                  Fractal formula:<br />f(z) = z * z + c</span
                > -->
                <ActionButton text="Submit" type="submit">
                  <SaveIcon />
                </ActionButton>
              </div>
            </VeeForm>
            <VeeForm
              @submit="onSubmit"
              :validation-schema="vScheme"
              class="pt-8 flex flex-row justify-between"
              v-if="currentFractal === 'vicsek'"
              :initial-values="{ levels: 4 }"
            >
              <div class="flex flex-col justify-start items-stretch gap-4">
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Levels:</span>
                  <div>
                    <PlainInput name="levels" type="number" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-between items-start">
                <!-- <span class="text-base font-light underline underline-offset-4">
                  Fractal formula:<br />f(z) = z * z + c</span
                > -->
                <ActionButton text="Submit" type="submit">
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
import { useToast } from 'vue-toastification';

const toast = useToast();

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
      zoom: 0,
      color_scheme_m: 'hot',
      color_scheme_j: 'hot',
      fractalImage: '',
      jScheme: {
        iterations: 'required|min_value:1|max_value:9999',
        real_c: 'required|max_value:9999',
        imag_c: 'required|max_value:9999',
      },
      mScheme: {
        iterations: 'required|min_value:1|max_value:9999',
      },
      vScheme: {
        levels: 'required|min_value:1|max_value:4',
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
  },
  mounted() {
    this.getColorSchemes();
    this.selectFractal({ currentFractal: 'mandelbrot' });
    this.getMandlebrot({
      max_iterations: 100,
      zoom_percentage: this.zoom / 100,
      color_map: 'hot',
      save_to_file: false,
    }).then(() => (this.fractalImage = this.mandelbrotImage));
  },
  methods: {
    selectFractal(fractal) {
      this.fractalImage = '';
      switch (fractal) {
        case 'vicsek':
          this.setCurrentFractal({ currentFractal: 'vicsek' });
          break;
        case 'julia':
          this.setCurrentFractal({ currentFractal: 'julia' });
          break;
        default:
          this.setCurrentFractal({ currentFractal: 'mandelbrot' });
          break;
      }
    },
    zoomChange(value) {
      this.zoom = value;
    },
    colorChangeM(value) {
      this.color_scheme_m = value;
    },
    colorChangeJ(value) {
      this.color_scheme_j = value;
    },

    goBack() {
      this.$router.back();
    },
    async onSubmit(values) {
      switch (this.currentFractal) {
        case 'vicsek':
          this.setCurrentFractal({ currentFractal: 'vicsek' });
          await this.getVicsek({
            levels: values.levels,
          });
          this.fractalImage = this.vicsekImage;
          break;
        case 'julia':
          this.setCurrentFractal({ currentFractal: 'julia' });
          if (!this.color_scheme_j) {
            toast.error('Select color scheme!');
            return;
          }
          await this.getJulia({
            max_iterations: values.iterations,
            zoom_percentage: this.zoom / 100,
            color_map: this.color_scheme_j,
            c_real: values.real_c,
            c_imag: values.imag_c,
            save_to_file: false,
          });
          this.fractalImage = this.juliaImage;
          break;
        default:
          this.setCurrentFractal({ currentFractal: 'mandelbrot' });
          if (!this.color_scheme_m) {
            toast.error('Select color scheme!');
            return;
          }
          await this.getMandlebrot({
            max_iterations: values.iterations,
            zoom_percentage: this.zoom / 100,
            color_map: this.color_scheme_m,
            save_to_file: false,
          });
          this.fractalImage = this.mandelbrotImage;
          break;
      }
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
