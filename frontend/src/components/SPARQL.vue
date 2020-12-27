<template>
  <v-container>
    <v-row>
      <v-text-field label="Query" v-model="query"></v-text-field>
      <v-btn id="unesiBtn" @click="unesiQuery" class="primary">unesi</v-btn>
    </v-row>
    <v-row>
      <v-simple-table v-if="redovi.length !== 0">
        <template>
          <thead>
            <tr>
              <th class="text-left">Text</th>
              <th class="text-left">URL</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in redovi" :key="item.smer">
              <td>{{ item.smer }}</td>
              <td>
                <a :href="item.url">{{ item.url }}</a>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "SPARQL",
  data() {
    return {
      query: "",
      redovi: [],
    };
  },
  methods: {
    unesiQuery() {
      axios
        .get(`http://localhost:5000/query`, {
          params: this.queryParams,
        })
        .then((response) => {
          this.redovi = response.data.redovi;
          this.query = "";
        })
        .catch((error) => {
          alert(error.response.data);
        });
    },
  },
  computed: {
    queryParams() {
      const params = new URLSearchParams();
      params.append("query", this.query);
      return params;
    },
  },
};
</script>

<style>
#unesiBtn {
  margin-top: 10px;
  margin-left: 30px;
}
</style>