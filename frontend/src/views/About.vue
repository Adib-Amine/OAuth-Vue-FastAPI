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
        <div class="row justify-content-center mt-5">
            <table class="table table-striped table-hover table-white">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Label</th>						
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in this.info.data" :key="item.id">
                        <td>{{item.id}}</td>
                        <td>{{item.label}}</td>
                        <td>{{item.price}}</td>                    
                    </tr>
                </tbody>
            </table>
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