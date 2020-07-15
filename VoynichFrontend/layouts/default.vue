<template>
  <v-app dark>
    <Header></Header>

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <Footer></Footer>
  </v-app>
</template>

<script>
import Cookie from "js-cookie";
import Header from "~/components/core/Header.vue";
import Footer from "~/components/core/Footer.vue";

//  import {
//    createSocket,
//    openSocket,//eslint-disable-line
//    closeSocket,//eslint-disable-line
//    messageReceived//eslint-disable-line
//  } from '~/plugins/websocket'

export default {
  components: {
    Header,
    Footer
  },
  created() {
    this.fetchUser();
  },
  methods: {
    //    import { mapGetters } from "vuex";
    async fetchUser() {
      console.log("FETCH ME");
      if (Cookie.get("voynich_jwt")) {
        await this.$axios.$get(`/login`).then(response => {
          this.$store.commit("SET_USER", response);
          //            createSocket(response.username)
        });
      }
    }
  }
};
</script>
