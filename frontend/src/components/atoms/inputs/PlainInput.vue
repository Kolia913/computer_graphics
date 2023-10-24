<template>
  <div class="relative">
    <VeeField
      class="bg-white border border-solid border-stroke rounded-md h-8 px-2"
      :name="name"
      :type="type ? type : 'text'"
    />
    <ErrorMessage :name="name" class="text-red text-xs font-light absolute left-0 top-8" />
  </div>
</template>
<script>
export default {
  name: 'PlainInput',
  props: ['name', 'type'],
};
</script>
