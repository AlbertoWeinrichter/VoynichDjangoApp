<template>
  <v-toolbar>
    <v-toolbar-title>Startup in a box</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat>Section One</v-btn>
      <v-btn flat>Section Two</v-btn>

      <v-btn v-if="isAuthenticated" flat>
        <nuxt-link to="/auth/sign-off" class="link">Sign Out</nuxt-link>
      </v-btn>
      <v-btn v-else flat>
        <nuxt-link to="/auth/sign-in" class="link">sign in</nuxt-link>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Header",
  computed: mapGetters(["isAuthenticated", "loggedUser"])
};
</script>

<style lang="scss" scoped>
img {
  &.img-logo {
    height: 90px;
    width: auto;
    margin-top: -55px;
  }
  &.img-logo-small {
    height: 40px;
    width: auto;
  }
}
</style>
