import { defineStore } from 'pinia';
import axios from 'axios';

const API_URL = import.meta.env.VITE_BASE_API;

export default defineStore('aphine', {
  state: () => ({
    aphineChart: null,
  }),
  actions: {
    async getAphineChart({ x1, y1, x2, y2, move_top, move_right, scale_a, scale_d, rotation }) {
      const res = await axios.post(`${API_URL}api/transformations/affine_transform`, {
        diagonal_1: [x1, y1],
        diagonal_2: [x2, y2],
        move_top,
        move_right,
        scale_a,
        scale_d,
        rotation,
      });
      this.aphineChart = res.data.image;
    },
  },
});
