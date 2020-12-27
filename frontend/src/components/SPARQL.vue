<template>
  <v-container>
    <v-text-field label="Query" v-model="query"></v-text-field>
  </v-container>
</template>

<script>
export default {
  name: "SPARQL",
  data() {
    return {
      query: "",
    };
  },
};
</script>

<style>
</style>