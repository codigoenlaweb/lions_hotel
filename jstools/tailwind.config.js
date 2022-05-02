module.exports = {
  content: [
    '../templates/*.html',
    '../apps/**/forms.py',
    '../templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        principalgreen:"#8bc392",
        secondarygray:"#C7C7C7",
        textinputfield:"#F7F7F7",
        dark:"#232830"
      },
      fontFamily: {
        'quicksand': ['Quicksand', 'sans-seri'],
        'roboto': ['Roboto', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
