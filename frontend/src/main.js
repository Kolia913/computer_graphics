import './assets/main.scss';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

import VeeValidationPlugin from '@/includes/validation';
import Toast from '@/includes/toast';
import VueSelect from '@/includes/v-select';

import Components from '@/includes/components';

const app = createApp(App);

// includes
app.use(createPinia());
app.use(router);
app.use(VeeValidationPlugin);
app.use(Toast);
app.use(VueSelect);

// global components
app.use(Components);

app.mount('#app');
