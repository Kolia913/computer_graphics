<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <ProgramWindow title="Lab 2 - Fractals" :isClosable="false">
      <template #content>
        <div class="flex flex-row justify-center items-start w-full gap-4">
          <ProgramMenu @onBackClick="goBack" />
          <div class="w-full">
            <Fractals />
            <div class="pt-2">
              <SliderInput />
            </div>
            <VeeForm
              @submit="onSubmit"
              :validation-schema="schema"
              class="pt-16 flex flex-row justify-between"
            >
              <div class="flex flex-col justify-center items-stretch">
                <div class="flex flex-row justify-between items-center gap-8">
                  <span class="text-lg font-light underline underline-offset-2">Constant C:</span>
                  <div>
                    <PlainInput name="constant" type="number" />
                  </div>
                </div>
                <div class="flex flex-row justify-between items-center pt-8">
                  <span class="text-lg font-light underline underline-offset-2">Colour:</span>
                  <div>
                    <SelectInput :options="options" />
                  </div>
                </div>
              </div>
              <div class="flex flex-col justify-between items-start">
                <span class="text-base font-light underline underline-offset-4">
                  Fractal formula:<br />f(z) = z * z + c</span
                >
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
</template>

<script>
import ActionButton from '../components/atoms/buttons/ActionButton.vue';
import PlainInput from '../components/atoms/inputs/PlainInput.vue';
import SelectInput from '../components/atoms/inputs/SelectInput.vue';
import SliderInput from '../components/atoms/inputs/SliderInput.vue';
import Fractals from '../components/general/Fractals.vue';
import ProgramMenu from '../components/general/ProgramMenu.vue';
import ProgramWindow from '../components/general/windows/ProgramWindow.vue';
import SaveIcon from '../components/icons/SaveIcon.vue';

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
  },
  data() {
    return {
      schema: {
        constant: 'required|min_value:1|max_value:9999',
      },
      options: [
        {
          label: 'Red & Black',
          code: 'rb',
        },
        {
          label: 'Yellow & Blue',
          code: 'yb',
        },
        {
          label: 'Gray & Pink',
          code: 'gp',
        },
      ],
    };
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    onSubmit(values) {
      console.log(values);
    },
  },
};
</script>
