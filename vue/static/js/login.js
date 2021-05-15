function onSignIn(googleUser) {
  // get login token, and pass to API
  var id_token = googleUser.getAuthResponse().id_token;
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
  // Connect API
  axios({
      method: 'post',
      url: 'http://www.stockhelper.com.tw:8889/api/users',
      data: {
        id_token: id_token
      }
  })
  .then(function (response) {
      console.log(response);
      // cookie record token
      document.cookie = 'google_token=' + id_token;
      // 轉頁
      location.href = response.data['url']
  })
  .catch(function (error) {
      console.log(error);
  })
}
