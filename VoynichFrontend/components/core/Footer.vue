<template>
  <div>
    <v-footer app>
      <span>&copy;Voynich Data 2019</span>
    </v-footer>

    <no-ssr>
      <cookie-law theme="dark-lime">
        <div slot-scope="props">
          <p>
            Esta web utiliza cookies propias y de terceros (concretamente de
            Google Analytics Y Facebook). Continuar navegando implica la
            aceptación de nuestra Política de Cookies 🍪🍪🍪
          </p>
          <div class="cookie-btn important" @click="props.accept">
            Entendido
          </div>
          <div class="cookie-btn" @click="props.close">
            <nuxt-link class="non-styled-link" to="/footer/legal">
              ¿Desea saber mas?
            </nuxt-link>
          </div>
        </div>
      </cookie-law>
    </no-ssr>
  </div>
</template>

<script>
import CookieLaw from "vue-cookie-law";
import NoSSR from "vue-no-ssr";

export default {
  name: "Footer",
  components: {
    CookieLaw,
    "no-ssr": NoSSR
  }
};
</script>

<style scoped></style>
