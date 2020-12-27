<template>
  <v-container>
    <v-card outlined>
      <v-row class="formClass">
        <v-col align="center">
          <h2>Kurs</h2>

          <v-text-field label="Id" v-model="id"></v-text-field>
          <v-text-field label="Autor" v-model="autor"></v-text-field>
          <v-text-field label="Datum" v-model="datum"></v-text-field>
          <v-text-field label="Opis" v-model="opis"></v-text-field>
          <v-text-field label="Jezik" v-model="jezik"></v-text-field>
          <v-text-field label="Naslov" v-model="naslov"></v-text-field>
          <v-text-field label="Predmet" v-model="predmet"></v-text-field>
          <v-text-field label="Izvor" v-model="izvor"></v-text-field>
          <v-btn id="submitId" class="primary"> submit </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "Kurs",
  data() {
    return {
      id: "",
      autor: "",
      datum: "",
      opis: "",
      jezik: "",
      naslov: "",
      predmet: "",
      izvor: "",
    };
  },
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