import { defineStore } from 'pinia';
import axios from 'axios';

const API_URL = import.meta.env.VITE_BASE_API;

export default defineStore('fractals', {
  state: () => ({
    currentFractal: 'mandelbrot',
    mandelbrotImage: '',
    juliaImage: '',
    vicsekImage: '',
    colorsSchemes: [],
  }),
  actions: {
    setCurrentFractal({ currentFractal }) {
      this.currentFractal = currentFractal;
    },
    async getColorSchemes() {
      const res = await axios.get(`${API_URL}api/color_maps`);

      this.colorsSchemes = res.data.color_maps;
    },

    async getMandlebrot({ max_iterations, zoom_percentage, color_map, save_to_file }) {
      const res = await axios.post(`${API_URL}api/mandelbrot`, {
        max_iterations,
        zoom_percentage,
        color_map,
        save_to_file,
      });

      this.mandelbrotImage = res.data;
    },

    async getJulia({ max_iterations, zoom_percentage, color_map, c_real, c_imag, save_to_file }) {
      const res = await axios.post(`${API_URL}api/julia`, {
        max_iterations,
        zoom_percentage,
        color_map,
        c_real,
        c_imag,
        save_to_file,
      });

      this.juliaImae = res.data;
    },

    async getVicsek({ levels }) {
      const res = await axios.post(`${API_URL}api/vicsek`, {
        levels,
      });

      this.vicsekImage = res.data;
    },
  },
});
