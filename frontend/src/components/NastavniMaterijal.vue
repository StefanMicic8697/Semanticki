<template>
  <v-container>
    <v-card outlined>
      <v-row class="formClass">
        <v-col align="center">
          <h2>Nastavni materijal</h2>

          <v-text-field label="Id" v-model="id"></v-text-field>
          <v-text-field label="Autor" v-model="autor"></v-text-field>
          <v-text-field label="Opis" v-model="opis"></v-text-field>
          <v-text-field label="Jezik" v-model="jezik"></v-text-field>
          <v-text-field label="Naslov" v-model="naslov"></v-text-field>
          <v-text-field label="Predmet" v-model="predmet"></v-text-field>
          <v-text-field label="Izvor" v-model="izvor"></v-text-field>
          <v-btn id="submitId" @click="dodajNastavniMaterijal" class="primary">
            Dodaj
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "NastavniMaterijal",
  data() {
    return {
      id: "",
      autor: "",
      opis: "",
      jezik: "",
      naslov: "",
      predmet: "",
      izvor: "",
    };
  },
  methods: {
    dodajNastavniMaterijal() {
      axios
        .post("http://localhost:5000/dodaj-nastavni-materijal", {
          id: this.id,
          autor: this.autor,
          opis: this.opis,
          jezik: this.jezik,
          naslov: this.naslov,
          predmet: this.predmet,
          izvor: this.izvor,
        })
        .then((response) => {
          alert(response.data.message);
        })
        .catch((error) => {
          alert(error.response.data.message);
        });
    },
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