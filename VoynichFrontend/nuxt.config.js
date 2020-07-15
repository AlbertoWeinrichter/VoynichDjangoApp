const VuetifyLoaderPlugin = require("vuetify-loader/lib/plugin");
const pkg = require("./package");

module.exports = {
  mode: "spa",
  env: {
    AUTH0_CLIENT_ID: "YOUR AUTH 0 ID",
    AUTH0_CLIENT_DOMAIN: "YOUR DOMAIN"
  },
  router: {
    middleware: "check-auth"
  },
  head: {
    title: pkg.name,
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: pkg.description }
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons"
      }
    ]
  },
  loading: { color: "#fff" },
  css: ["~/assets/style/app.styl"],
  plugins: ["@/plugins/vuetify", "@/plugins/axios"],
  modules: ["@nuxtjs/axios"],
  axios: {
    //    baseURL: process.env.BASE_URL,
    //    browserBaseURL: process.env.BROWSER_BASE_URL
    baseURL: "http://127.0.0.1:8000/api",
    browserBaseURL: "http://127.0.0.1:8000/api"
  },
  build: {
    transpile: ["vuetify/lib"],
    plugins: [new VuetifyLoaderPlugin()],
    loaders: {
      stylus: {
        import: ["~assets/style/variables.styl"]
      }
    },
    extend(config, ctx) {
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: "pre",
          test: /\.(js|vue)$/,
          loader: "eslint-loader",
          exclude: /(node_modules)/
        });
      }
    }
  }
};
