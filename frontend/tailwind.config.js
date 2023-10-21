/* eslint-disable no-undef */
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      colors: {
        green: '#83B52E',
        blue: '#5C8FC2',
        primary: '#E95420',
        'primary-dark': '#CF3600',
        secondary: '#343434',
        red: '#EA0303',
        stroke: '#B8B8B8',
        'grey-light': '#D9D9D9',
        'grey-light-darker': '#BBBBBB',
        terminal: '#333333',
        'terminal-stroke': '#606060',
        milk: '#F6F6F5',
      },
    },
  },
  plugins: [],
};
