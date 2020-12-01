<template>
    <section class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-lg-4">
                <div class="login-panel bg-white text-left">
                    <div class="alert alert-primary" role="alert" :style="{opacity: isAlertShow ? 1 : 0}">
                        Login successfully. <small>waiting for redirect.</small>
                        <loader-component width="30"></loader-component>
                    </div>
                    <div class="alert alert-primary" role="alert" :style="{opacity: error ? 1 : 0}">
                        {{errorMessage}}.
                    </div>
                    <h1 class="display-3 font-weight-bold">Login</h1>
                    <p class="font-weight-bold">Welcome back</p>
                    <br>
                    <form action="">
                        <div class="form-group">
                            <label class="input-label">Username</label>
                            <input type="text" class="form-control" v-model="requestBody.username" placeholder="Username">
                        </div>
                        <div class="form-group">
                            <label class="input-label">Password</label>
                            <input type="password" class="form-control" v-model="requestBody.password" placeholder="Password">
                        </div>
                        <br>
                        <div class="form-group d-flex justify-content-center">
                            <button class="btn btn-primary w-25" id="login" @click.prevent="login" v-if="!isLoggingIn">Login</button>
                            <button class="btn btn-primary w-25" disabled @click.prevent="login" v-if="isLoggingIn"><loader-component width="30"></loader-component></button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div v-show="error">
          {{errorMessage}}
        </div>
    </section>
</template>

<script>
import LoaderComponent from '../components/LoadingComponent'
import { setTimeout } from 'timers';
import axios from 'axios'
import qs from 'qs'

export default {
    components: { LoaderComponent },
    data() {
        return {
            isLoggingIn: false,
            isAlertShow: false,
            error : false,
            errorMessage : null,
            config : {
                headers: {
                    'content-type': 'application/x-www-form-urlencoded'
                }
            },
            requestBody : {
                username : null,
                password : null
            }
        }
    },
    methods: {
        async login() {
            const res = await this.gettoken()
            if(res.status == 200){
                this.$myauth.access_token = res.data.access_token
                this.isLoggingIn = true
                setTimeout(() => {
                    this.$myauth.isAuthenticated = true
                    this.isLoggingIn = false
                    this.isAlertShow = true
                    setTimeout(() => this.redirect(), 1000)
                }, 1000)   
            }
            else{
                this.error = true
                setTimeout(() => this.showError(),2000)
                this.errorMessage = res.data.detail
            }
            
        },
        redirect() {
            this.$router.push({name: 'About'})
        },
        showError(){
            this.error = false
        },
        async gettoken(){
            try {
                const res = await axios.post("http://localhost:8000/token",qs.stringify(this.requestBody),this.config)
                return res
            } catch (err) {
                return err.response
            }
        }
    }
}
</script>

<style lang="scss">
.widget {
    margin: 0;
    height: unset;
}
.login-panel {
    position: relative;
    padding: 100px 0;
    .alert {
        opacity: 0;
        position: absolute;
        width: 100%;
        top: 100px;
        transition: all .5s;
        &.alert-primary {
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            border: none;
        }
        .widget {
            position: absolute;
            right: 5px;
            top: 0;
            margin: 10px;
        }
    }
}
</style>