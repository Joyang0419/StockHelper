<template>
<div>
  <section class="login-block">
    <div class="container">
        <div class="row">
            <div class="col-md-4 login-sec">
                <h2 class="text-center">Login StockHelper</h2>
                <form class="login-form">
                  <div class="g-signin2 center" data-longtitle="true" data-onsuccess="onSignIn"></div>
                  <hr size="8px" align="center" width="100%">
                  <div class="form-group">
                    <label for="exampleInputEmail1">Username</label>
                    <input type="text" id="exampleInputEmail1" class="form-control" placeholder="">
                  </div>
                  <div class="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input type="password" id="exampleInputPassword1" class="form-control" placeholder="">
                  </div>
                  <div class="form-check">
                    <label class="form-check-label">
                      <input type="checkbox" class="form-check-input">
                      <small>Remember Me</small>
                    </label>
                    <button type="submit" class="btn btn-login float-right">Submit</button>
                  </div>
                </form>
                <div class="copy-text">Created by <i class="fa fa-heart"></i> by StockHelper</div>
            </div>

            <div class="col-md-8 banner-sec">
                <div class="carousel-item active">
                    <img class="d-block img-fluid" src="https://static.pexels.com/photos/33972/pexels-photo.jpg" alt="First slide">
                </div>
            </div>
        </div>
    </div>
  </section>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<script>
  function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
  }

  function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login-block{
  float:left;
  width:100%;
  padding : 75px 0;
}

.banner-sec{background:url(https://static.pexels.com/photos/33972/pexels-photo.jpg)  no-repeat left bottom; background-size:cover; min-height:500px; border-radius: 0 10px 10px 0; padding:0;}
/* Created by  by StockHelper */
.login-sec{padding: 50px 30px; position:relative;}
.login-sec .copy-text{position:absolute; width:80%; bottom:20px; font-size:13px; text-align:center;}
.login-sec .copy-text i{color:#FEB58A;}
/*login now*/
.login-sec h2{margin-bottom:30px; font-weight:800; font-size:30px; color: #DE6262;}
.login-sec h2:after{content:" "; width:100px; height:5px; background:#FEB58A; display:block; margin-top:20px; border-radius:3px; margin-left:auto;margin-right:auto}
.center {
  position: relative;
  left: 20%;
}
.container{background:#fff; border-radius: 10px}
.btn-login{background: #DE6262; color:#fff; font-weight:600;}
.login-sec{padding: 50px 30px; position:relative;}
.login-sec .copy-text{position:absolute; width:80%; bottom:20px; font-size:13px; text-align:center;}
.login-sec .copy-text i{color:#FEB58A;}
.login-sec .copy-text a{color:#E36262;}
.login-sec h2{margin-bottom:30px; font-weight:800; font-size:30px; color: #DE6262;}
.login-sec h2:after{content:" "; width:100px; height:5px; background:#FEB58A; display:block; margin-top:20px; border-radius:3px; margin-left:auto;margin-right:auto}
</style>
