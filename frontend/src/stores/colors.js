import { defineStore } from 'pinia';
import axios from 'axios';

const API_URL = import.meta.env.VITE_BASE_API;

export default defineStore('colors', {
  state: () => ({
    imageBase64: '',
  }),
  actions: {
    async sendImageWithChanges({ x1, x2, y1, y2, scheme, lightness, saturation, file }) {
      const res = await axios.post(`${API_URL}api/colors/change_color_model`, {
        x1,
        x2,
        y1,
        y2,
        scheme,
        lightness,
        saturation,
        file,
      });
      this.imageBase64 = res.data.image;
    },
    changeImageBase64(base64) {
      this.imageBase64 = base64;
    },
  },
});
