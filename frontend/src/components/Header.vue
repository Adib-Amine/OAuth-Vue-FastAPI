<template>
    <nav class="navbar navbar-dark bg-primary navbar-expand-md">
        <div class="container-fluid">
        <router-link class="navbar-brand" to="/">OAuth-Vue-FastAPI.</router-link>
        <div class="collapse navbar-collapse" id="navcol-1">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item" v-if="!$myauth.isAuthenticated"> <router-link  class="nav-link" to="/login">Login</router-link></li>
                    <li class="nav-item" v-if="$myauth.isAuthenticated" > <div @click='logout' class="nav-link" to="/">SignOut</div></li>
                </ul>
            </div>
        </div>    
    </nav>
</template>

<script>
export default {
    name:"Header",
    data (){
        return {
        }
    },
    methods : {
        logout() {
            this.$myauth.isAuthenticated = false
            this.$router.push({name: 'Home'})
        }
    }    
}
</script>

<style scoped>
nav{
    max-height:45px;
    /* margin-left: 40px; */
}
</style>