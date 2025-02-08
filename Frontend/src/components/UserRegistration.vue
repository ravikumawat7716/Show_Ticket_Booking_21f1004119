<template>
    <div>
        <h1>User Registration</h1>
        <input type="text" v-model="username" placeholder="Enter username" />
        <input type="password" v-model="password" placeholder="Enter password" />
        <input type="email" v-model="email" placeholder="Enter email" />
        <button @click="register">Register</button>
    </div>

</template>

<script>
import axios from 'axios';
export default {
    name: 'UserRegistration',
    data() {
        return {
            username: '',
            password: '',
            email: '',
        };
    },
    methods: {
        async register() {
            try {
                const response = await axios.post('http://localhost:5000/register', {
                    username: this.username,
                    password: this.password,
                    email: this.email,
                });
                console.log(response);
                if (response.status === 201) {
                    alert('Registration Successful');
                    this.$router.push('/login');
                }
                if (response.status === 401) {
                    alert('Invalid Credentials');
                }

            } catch (error) {
                console.error(error);
            }

        },

    },

}

</script>

<style></style>