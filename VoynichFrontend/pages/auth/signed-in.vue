<template>
  <Loading text="Signing In" />
</template>

<script>
import { extractInfoFromHash } from "~/services/auth"; //eslint-disable-line
import { mapMutations } from "vuex";
import Cookie from "js-cookie";
import Loading from "~/components/core/Loading";

export default {
  name: "SignedIn",
  components: { Loading },
  computed: {
    ...mapMutations(["SET_USER"])
  },
  mounted() {
    const token = extractInfoFromHash();
    Cookie.set("voynich_jwt", token.token);
    window.localStorage.setItem("voynich_jwt", token.token);
    this.fetchUser();
    this.$router.replace("/");
  },
  methods: {
    fetchUser() {
      this.$axios
        .$get(`/login`)
        .then(response => {
          this.$store.commit("SET_USER", response);
        })
        .finally();
    }
  }
};
</script>
