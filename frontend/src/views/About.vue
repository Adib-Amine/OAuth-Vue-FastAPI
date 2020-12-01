<template>
        <div class="container">
          <div class="row justify-content-center">
              <h1>About</h1>
          </div>  
          <div class="row justify-content-center mt-5">
          <h6>Your Token : </h6><br>
          </div>
          <div class="row">
          <p>{{$myauth.access_token}}</p>
        </div>
        </div>
</template>
<script>
  export default {

  }
</script>