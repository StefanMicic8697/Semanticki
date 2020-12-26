<template>
  <v-app-bar color="deep-purple accent-4" dark max-height="64px">
    <v-toolbar-title>Sematic web</v-toolbar-title>

    <v-btn
      text
      @click="
        () => {
          this.$router.push('/studijski-program');
        }
      "
    >
      Study program
    </v-btn>

    <v-btn
      text
      @click="
        () => {
          this.$router.push('/kurs');
        }
      "
    >
      course
    </v-btn>

    <v-btn
      text
      @click="
        () => {
          this.$router.push('/obrazovni-cilj');
        }
      "
    >
      obrazovni cilj
    </v-btn>

    <v-btn
      text
      @click="
        () => {
          this.$router.push('/nastavni-materijal');
        }
      "
    >
      nastavni materijal
    </v-btn>
  </v-app-bar>
</template>

<script>
import axios from "axios";
export default {
  name: "AppBar",
  data() {
    return {};
  },
  methods: {},
  computed: {},
  created() {},
};
</script>

<style>
.add-question-btn {
  margin: 10px;
}
</style>