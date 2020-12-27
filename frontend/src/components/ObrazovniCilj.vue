<template>
  <v-container>
    <v-card outlined>
      <v-row class="formClass">
        <v-col align="center">
          <h2>Obrazovni cilj</h2>
          <v-text-field label="Id"></v-text-field>
          <v-text-field label="Opis"></v-text-field>
          <v-text-field label="Naslov"></v-text-field>
          <v-btn id="submitId" @click="dodajObrazovniCilj" class="primary">
            dodaj
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "ObrazovniCilj",
  data() {
    return {
      id: "",
      opis: "",
      naslov: "",
    };
  },
  methods: {
    dodajObrazovniCilj() {
      axios
        .post("http://localhost:5000/dodaj-obrazovni-cilj", {
          id: this.id,
          opis: this.opis,
          naslov: this.naslov,
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