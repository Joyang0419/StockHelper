<template>
  <section class="login-block">
    <div class="container">
        <div class="row">
            <div class="col-md-4 login-sec">
                <img alt="Winner" class="center" src="@/assets/login/images/winner.jpg">
                <h2 class="text-center">Login StockHelper</h2>
                <form class="login-form">
                    <div class="g-signin2" data-width="300px" data-height="50" data-longtitle="true" data-onsuccess="onSignIn"></div>
                </form>
                <div class="copy-text">Created by <i class="fa fa-heart"></i> by StockHelper</div>
            </div>

            <div class="col-md-8 banner-sec">
                <div class="carousel-item active">
                    <img class="d-block img-fluid" src="@/assets/login/images/login_image.jpg" alt="First slide">
                </div>
            </div>
        </div>
  </div>
  </section>
</template>

<script>
export default {
    name: 'Login',
    data () {
      return {
      }
    },
    mounted: function () {
        // 渲染google login 按鈕
        var google_login_Script = document.createElement('script');
        google_login_Script.setAttribute('src', 'https://apis.google.com/js/platform.js?onload=renderButton');
        document.body.appendChild(google_login_Script);
    },
    methods: {
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="@/assets/login/css/login.css">

</style>
