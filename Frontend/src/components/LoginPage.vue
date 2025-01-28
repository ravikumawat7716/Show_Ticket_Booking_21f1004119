<template>
    <div>
        <h1>Login Page</h1>
        <input type="text" v-model="username" placeholder="Enter username" />
        <input type="password" v-model="password" placeholder="Enter password" />
        <button @click="login">Login</button>
    </div>  
</template>

<script>
import axios from 'axios';
export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async login() {
            try {

                const response = await axios.post('http://localhost:5000/login', {
                    username: this.username,
                    password: this.password,
                });
                console.log(response);
                if (response.status === 200) {
                    alert('Login Successful');
                    localStorage.setItem('token', response.data.token);
                    localStorage.setItem('username', response.data.username);
                    localStorage.setItem('role', response.data.user_role);
                    this.$router.push('/');
                }
                if (response.status === 401) {
                    alert('Invalid Credentials');
                }

            } catch (error) {
                console.error(error);
            }

        },

    },
    mounted() {
            if (localStorage.getItem('token')) {
                if (localStorage.getItem('role') === 'admin') {
                    this.$router.push('/admindashboard');
                }
                else {
                    this.$router.push('/');
                }
            }
        },
};
</script>