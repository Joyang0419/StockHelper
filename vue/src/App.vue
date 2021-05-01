<template>
  <div id="app">
    <div class="wrapper">
        <!-- Sidebar  -->
        <nav id="sidebar" :class="{active: sidebar_Status}">
          <!-- User Info-->
          <div class="sidenav-header-inner text-center">
              <img src="@/assets/user_images/joyang0419@gmail.com.jpg" alt="user_image" class="img-fluid rounded-circle user_image">
              <h6 class="#homeSubmenu" aria-expanded="false">Nathan Andrews</h6>
              <label class="switch">
                  <input type="checkbox" checked class="btn btn-info" @click="toggle_sidebar()">
                  <span class="slider round"></span>
              </label>
          </div>
            <ul class="list-unstyled components">
                <li>
                    <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                        <i class="fas fa-home"></i>
                        股票資訊
                    </a>
                    <ul class="collapse list-unstyled" id="homeSubmenu">
                        <li>
                            <a href="#">台股大盤</a>
                        </li>
                        <li>
                            <a href="#">產業類別指標</a>
                        </li>
                        <li>
                            <a href="#">個股指標</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                        <i class="fas fa-copy"></i>
                        個人資訊
                    </a>
                    <ul class="collapse list-unstyled" id="pageSubmenu">
                        <li>
                            <a href="#">個人資料</a>
                        </li>
                        <li>
                            <a href="#">即時庫存</a>
                        </li>
                    </ul>
                </li>
            </ul>
        </nav>

        <!-- Page Content  -->
        <div id="content">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                    <img class="stock_increase_image" src="@/assets/stock_increase.png" alt="stock_increase">
                    <h2 class="text-center red_text">StockHelper</h2>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="nav navbar-nav ml-auto">
                            <li class="nav-item active">
                                <a class="nav-link" href="#" data-toggle="modal" data-target="#exampleModal">LogOut</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <router-view/>
        </div>
    </div>
      <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
                確定要登出嗎?
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">No</button>
              <button type="button" class="btn btn-primary" data-dismiss="modal">Yes</button>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
      return {
        sidebar_Status: false,
      }
  },
  mounted: function () {
      var jQueryScript = document.createElement('script');
      jQueryScript.setAttribute('src', 'https://code.jquery.com/jquery-3.3.1.slim.min.js');
      document.body.appendChild(jQueryScript);

      var popperScript = document.createElement('script');
      popperScript.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js');
      document.body.appendChild(popperScript);

      var BootstrapScript = document.createElement('script');
      BootstrapScript.setAttribute('src', 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js');
      document.body.appendChild(BootstrapScript);
  },
  methods: {
      toggle_sidebar: function () {
        this.sidebar_Status = !this.sidebar_Status
      }

  }
}
</script>

<style>
  /* custom CSS */
  @import "assets/index/css/index.css";
  /* Bootstrap CSS */
  @import "https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css";
  /* Font Awesome JS */
  @import "https://use.fontawesome.com/releases/v5.0.13/js/solid.js";
  @import "https://use.fontawesome.com/releases/v5.0.13/js/fontawesome.js";
</style>
