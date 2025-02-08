<template>
    <h1> This is user home page.</h1>
    <h1> Name :{{ name_variable }}</h1>
    <h2 v-if="email">Email :{{ email }}</h2>
    <h2 v-else>Email : Loading...</h2>
    <h2 v-if="linkedin_url">Linkedin URL :{{ linkedin_url }}</h2>
    <h2 v-else>We do not have the linkedin_url</h2>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'HomePage',
    data() {
      return {
      name_variable: '',
      email : null,
      linkedin_url : null,
      };
    },
     mounted() {
        console.log('==============================');
        console.log("HomePage is mounted");
        if (localStorage.getItem('token')) {
          if (localStorage.getItem('role') === 'admin') {
            this.$router.push('/admindashboard');
          }
        }
        else {
          this.$router.push('/login');
        }
      const name = localStorage.getItem('username');
      this.name_variable = name;
      console.log('==============================');
    //   try {
    //     const response = await axios.get('http://localhost:5000/userdata', {
    //       headers: {
    //         Authorization: `${localStorage.getItem('token')}`,
    //       },
    //     });
    //     console.log(response);
    //     if (response.status === 200) {
    //       if (response.data.message === 'Unauthorized') {
    //         alert('Unauthorized Access');
    //         localStorage.removeItem('token');
    //         localStorage.removeItem('username');
    //         localStorage.removeItem('role');
    //         this.$router.push('/login');
    //       }
    //       this.email = response.data.email;
    //       this.linkedin_url = 'linkedin.com';
    //     }
        
  
    //   } catch (error) {
    //     console.error(error);
    //     alert("Something went wrong");
    //   }
      
  },
  };
  </script>