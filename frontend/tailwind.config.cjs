/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        mainBG: "#212121",
        primaryDark: "#321C5F",
        primary: "#5E35B1",
        secondary: "#8762D0",
        ligth: "#EFEFEF",
      },
    },
  },
  plugins: [],
};
