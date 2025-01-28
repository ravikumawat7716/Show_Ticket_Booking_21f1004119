<template>
    This is Admin Dashboard.
    <!-- <div v-if="users">
        <ul>
            <li v-for="user in users" :key="user.id">
                {{ user.email }} - {{ user.name }} 
            </li>
            
        </ul></div>
    <div v-else>
        User data is loading...
    </div> -->


</template>

<script>
// import axios from 'axios';
export default {
    name: 'AdminDashboard',
    data() {
        return {
            users : [],
        };

    },
    async mounted() {
        // if (!localStorage.getItem('token')) {
        //     this.$router.push('/login');
        // }
        // else {
        //     console.log('Token is present');
        //     if (localStorage.getItem('role') !== 'admin') {
        //         this.$router.push('/');
        //     }
        //     else {
        //         console.log('Role is admin');
        //         try{
        //         const response = await axios.get('http://localhost:5000/admin', {
        //             headers: {
        //                 Authorization: `${localStorage.getItem('token')}`,
        //             },
        //         });
        //         console.log(response);
        //         this.users = response.data;
        //         console.log("===============================");
        //         console.log(this.users);
        //     }
        //     catch (error) {
        //         console.error(error);
        //         alert("Something went wrong");

        //     }
        // }
    // }
    },
};


</script>