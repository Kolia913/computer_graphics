<template>
  <slider
    class="border rounded-md border-stroke"
    color="#E95420"
    track-color="#FFF"
    :height="height"
    :flipTooltip="flipTooltip"
    v-model="value"
    :tooltip="tooltip"
    :tooltipText="tooltipText"
    :handleScale="handleScale"
    :alwaysShowHandle="alwaysShowHandle"
    @drag-end="onChange"
  />
</template>
<script>
export default {
  name: 'SliderInput',
  data() {
    return {
      min: 0,
      max: 100,
      step: 1,
      tooltip: true,
      value: 0,
      handleScale: 1.8,
      tooltipText: '%v %',
      flipTooltip: true,
      height: 8,
      alwaysShowHandle: true,
    };
  },
  methods: {
    onChange(value) {
      this.$emit('onChange', value);
    },
  },
};
</script>
<style>
.tooltip {
  font-weight: 500 !important;
  font-size: 14px !important;
  border: 1px solid #b8b8b8 !important;
  margin-top: -5px !important;
}
.track-filled {
  background-color: #fff !important;
}
</style>
