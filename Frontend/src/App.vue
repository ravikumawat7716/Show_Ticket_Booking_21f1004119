<template>
  <HelloWorld />
  <h1>Welcome {{ message }} !</h1>
  <HelloWorld />
  <HelloWorld />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'; // import the component
export default {
  name: 'App',
  components: {
    HelloWorld,
  },
  data() {
    return {
      message: 'Thomas',
    };
  },
};
</script>

<style>
</style>