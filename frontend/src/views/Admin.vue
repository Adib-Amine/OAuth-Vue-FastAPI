<template>
        <div class="container">
            <div class="row justify-content-center">
                <h1>Admin</h1>
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
import axios from 'axios'
  export default {
    data () {
        return {
          info : "",
        }
    },
    methods: {
      async fetchItems(){
          axios.get("http://localhost:8000/user/items",this.$myauth.getBearer())
          .then(response => (this.info = response)) 
      },
    },
    mounted(){
      this.fetchItems()
    }
  }
</script>