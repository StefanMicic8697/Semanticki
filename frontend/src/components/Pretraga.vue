<template>
  <v-container>
    <v-row>
      <v-col>
        <v-radio-group row v-model="radioSelect">
          <v-radio label="Kurs" value="kurs"></v-radio>
          <v-radio label="Smer" value="smer"></v-radio>
        </v-radio-group>
      </v-col>
    </v-row>
    <v-row v-if="radioSelect !== false">
      <v-col>
        <v-card v-if="radioSelect === 'kurs'" outlined>
          <v-row>
            <v-col align="center">
              <v-text-field
                label="Kurs"
                :disabled="obrazovniCilj !== '' || smer !== ''"
                v-model="kurs"
              ></v-text-field>
              <v-text-field
                label="Obrazovni cilj"
                :disabled="kurs !== ''"
                v-model="obrazovniCilj"
              ></v-text-field>
              <v-text-field
                label="Smer"
                :disabled="kurs !== ''"
                v-model="smer"
              ></v-text-field>

              <v-btn class="primary" @click="pretraziKurs"> Pretrazi </v-btn>
            </v-col>
          </v-row>
        </v-card>
        <v-card v-if="radioSelect === 'smer'" outlined>
          <v-row>
            <v-col align="center">
              <v-text-field label="Jezik" v-model="jezik"></v-text-field>
              <v-btn class="primary" @click="pretraziSmer"> Pretrazi </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-simple-table v-if="kursevi.length !== 0">
          <template>
            <thead>
              <tr>
                <th class="text-left">Kurs</th>
                <th class="text-left">URL</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in kursevi" :key="item.kurs">
                <td>{{ item.kurs }}</td>
                <td>{{ item.url }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
        <v-simple-table v-if="smerovi.length !== 0">
          <template>
            <thead>
              <tr>
                <th class="text-left">Kurs</th>
                <th class="text-left">URL</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in smerovi" :key="item.smer">
                <td>{{ item.smer }}</td>
                <td>{{ item.url }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Pretraga",
  data: () => ({
    radioSelect: false,
    smer: "",
    kurs: "",
    jezik: "",
    obrazovniCilj: "",
    kursevi: [],
    smerovi: [],
  }),
  methods: {
    pretraziSmer() {
      this.kursevi = [];
      axios
        .get(`http://localhost:5000/smerovi`, {
          params: this.smerParams,
        })
        .then((response) => {
          this.smerovi = response.data.smerovi;
          this.jezik = "";
        })
        .catch((error) => {
          alert(error.response.data);
        });
    },
    pretraziKurs() {
      this.smerovi = [];
      axios
        .get(`http://localhost:5000/kursevi`, {
          params: this.kursParams,
        })
        .then((response) => {
          this.kursevi = response.data.kursevi;
          this.smer = "";
          this.kurs = "";
          this.obrazovniCilj = "";
        })
        .catch((error) => {
          alert(error.response.data);
        });
    },
  },
  computed: {
    kursParams() {
      const params = new URLSearchParams();
      params.append("obrazovni_cilj", this.obrazovniCilj);
      params.append("smer", this.smer);
      params.append("kurs", this.kurs);
      return params;
    },
    smerParams() {
      const params = new URLSearchParams();
      params.append("jezik", this.jezik);
      return params;
    },
  },
};
</script>

<style>
</style>