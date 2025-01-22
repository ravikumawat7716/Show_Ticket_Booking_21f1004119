<template>
  <h1> Name :{{ name_variable }}</h1>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
    name_variable: 'Ravi',
    };
  },
};
</script>