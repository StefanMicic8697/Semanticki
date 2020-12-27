<template>
  <v-container>
    <v-card outlined>
      <v-row class="formClass">
        <v-col align="center">
          <h2>Obrazovni cilj</h2>
          <v-text-field label="Id"></v-text-field>
          <v-text-field label="Opis"></v-text-field>
          <v-text-field label="Naslov"></v-text-field>
          <v-btn id="submitId" class="primary"> submit </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "ObrazovniCilj",
};
</script>

<style>
.formClass {
  padding-left: 50px;
  padding-right: 50px;
}
#submitId {
  margin-bottom: 10px;
}
</style>