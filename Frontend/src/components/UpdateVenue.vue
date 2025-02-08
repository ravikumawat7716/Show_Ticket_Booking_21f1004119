<template>
    <div>
        <h1>Update Venue</h1>
        <input type="text" v-model="name" placeholder="Enter name" />
        <input type="text" v-model="location" placeholder="Enter location" />
        <input type="number" v-model="capacity" placeholder="Enter capacity" />
        <button @click="updateVenue">Update</button>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'UpdateVenue',
    data() {
        return {
            id: '',
            name: '',
            location: '',
            capacity: '',
        };
    },
    methods: {
        async updateVenue() {
            console.log("Update Venue is clicked");
            console.log('==============================');

            try {
                console.log('==============================');
                const response = await axios.put('http://localhost:5000/venues/', {
                    id : 1,
                    name: this.name,
                    location: this.location,
                    capacity: this.capacity,
                });
                if (response.status == 200) {
                    console.log("Venue Updated Successfully.")
                    alert('Venue Updated Successfully');
                    this.$router.push('/admindashboard');
                }
                else {
                    alert('Something went wrong');
                }
            }   
            catch (error) {
                console.error(error);
            }
        },
    },
    async mounted() {
        if (localStorage.getItem('token')) {
            if (localStorage.getItem('role') === 'admin') {
                console.log('==============================');
                console.log('AdminDashboard is mounted');
                console.log('==============================');
                this.id = this.$route.params.id;
                try {
                    const response = await axios.get('http://localhost:5000/venues')
                    console.log(response.data)
                    if (response.status == 200) {
                        console.log("Venues Fetched Successfully.")
                        for (let i = 0; i < response.data.length; i++) {
                            if (response.data[i].id == this.$route.params.id) {
                                this.name = response.data[i].name;
                                this.location = response.data[i].location;
                                this.capacity = response.data[i].capacity;
                            }
                        }
                    
                    }

                }
                catch (error){
                    console.error;
                }

            } else {
                this.$router.push('/');
            }
        } else {
            this.$router.push('/login');
        }
    },
};


</script>