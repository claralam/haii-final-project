/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}",
            "./static/**/*.{html,js}"
            ],
  theme: {
    extend: {
      colors : {
        lightBlue: '#e0e9ff',
      }
    },
  },
  plugins: [],
}