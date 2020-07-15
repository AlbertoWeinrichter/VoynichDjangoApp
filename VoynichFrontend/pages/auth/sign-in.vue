<template>
  <div id="auth0-lock" />
</template>

<script>
export default {
  middleware: "anonymous",
  mounted() {
    const showLogin = require("~/services/lock").showLogin;
    showLogin("auth0-lock");
  }
};
</script>
