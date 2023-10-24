<template>
  <v-select
    class="select w-full bg-white"
    :options="options"
    @option:selected="onChange"
    v-model="value"
  />
</template>
<script>
export default {
  name: 'FormSelect',
  props: ['options'],
  data() {
    return {
      value: 'hot',
    };
  },
  methods: {
    onChange(e) {
      this.$emit('onChange', e);
    },
  },
};
</script>
<style scoped>
.select {
  min-width: 193px;
  --vs-controls-color: #b8b8b8;
  --vs-border-color: #b8b8b8;
  --vs-border-radius: 6px;

  --vs-dropdown-bg: #fff;
  --vs-dropdown-color: #d9d9d9;
  --vs-dropdown-option-color: #000;

  --vs-selected-bg: #d9d9d9;
  --vs-selected-color: #000;

  --vs-search-input-color: #fff;

  --vs-dropdown-option--active-bg: #d9d9d9;
  --vs-dropdown-option--active-color: #000;
  --vs-dropdown-max-height: 90px;
}
</style>
