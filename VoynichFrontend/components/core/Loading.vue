<template>
  <div>
    <div class="bt-loading">
      <div class="inner">
        <img src="~assets/img/spinbg.png" class="spinbg-img" alt="" />
        <div>
          <h4 class="loading-title">{{ "Loading" }}</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Loading"
};
</script>

<style lang="scss">
.bt-loading {
  margin: 150px 0px;
  .inner {
    text-align: center;
  }
  .spinbg-img {
    width: 60px;
    height: 60px;
    -webkit-animation: spin 4s linear infinite;
    -moz-animation: spin 4s linear infinite;
    animation: spin 4s linear infinite;
  }
  h4.loading-title {
    margin-top: 15px;
    font-weight: 700;
    color: gray("200");
    letter-spacing: 0.1em;
    font-size: 16px;
    text-transform: uppercase;
  }
  @-moz-keyframes spin {
    100% {
      -moz-transform: rotate(360deg);
    }
  }
  @-webkit-keyframes spin {
    100% {
      -webkit-transform: rotate(360deg);
    }
  }
  @keyframes spin {
    100% {
      -webkit-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
}
</style>
