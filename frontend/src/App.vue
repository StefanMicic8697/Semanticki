<template>
    <v-app>
      <app-bar/>
      <router-view/>
    </v-app>
</template>

<script>
import AppBar from './components/AppBar.vue';
export default {
    components: {
        AppBar,
    },
    data() {
        return {
        };
    },
};
</script>

<style>
html {
  height: 100%;
  overflow: hidden;
}
</style>