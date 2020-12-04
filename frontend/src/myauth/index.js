

const MyPlugin = {
    install(Vue) {
      var userOAuth = new Vue({
        data: {
            isAuthenticated : false,
            access_token : null,
            token_type : 'bearer',
            user_type : '',
            config : {
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
              }
            },
        },
        methods : {
          getBearer(){
            return {  headers: {'Authorization': `Bearer ${this.access_token}`}}
          }
        }
      })
      // Vue.prototype.$myVar = () => {
      //   return testvar
      // }
      Vue.prototype.$myauth = userOAuth
      
  }
};

export default MyPlugin;


// Vue.prototype.$amineadib = 'amine'
//       Vue.prototype.$adib = true   

// <br><br><br>
//       <p>{{$amineadib}}</p>
//       <p>{{$myauth.testMethod()}}</p>
//       <p v-if="$adib">show1</p>
//       <p v-if="!$myauth.isAuthenticated">show2</p>
//       <p v-if="$myVar">show3</p>