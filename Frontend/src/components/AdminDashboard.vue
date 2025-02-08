<template>
    This is Admin Dashboard.
    <h1> Venues </h1>
    <ul>
        <li v-for="venue in venues" :key="venue.id">
            Name : {{ venue.name }}
            <br>
            Location : {{ venue.location }}
            <br>
            Capacity : {{ venue.capacity }}
            <br>
            <button @click="updateVenue(venue.id)">Update</button>
        </li>
    </ul>
    


</template>

<script>
import axios from 'axios';

// import axios from 'axios';
export default {
    name: 'AdminDashboard',
    data() {
        return {
            venues : [],
        };

    },
    methods: {
        async updateVenue(id) {
            this.$router.push(`/updatevenue/${id}`);
        },
    },
    async mounted() {
        try {
            const response = await axios.get('http://localhost:5000/venues')
            console.log(response);
            if (response.status === 200) {
                this.venues = response.data;
            } else {
                alert('Something went wrong');
            }
    }
    catch (error) {
        console.error(error);
    }
    },
};


</script>