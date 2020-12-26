<template>
  <v-container>
    <v-card outlined >
      <v-row class="formClass">
          
        <v-col  align="center">
                    <h2>Nastavni materijal</h2>

          <v-text-field label="Id"></v-text-field>
          <v-text-field label="Creator"></v-text-field>
          <v-text-field label="Description"></v-text-field>
          <v-text-field label="Language"></v-text-field>
          <v-text-field label="Title"></v-text-field>
          <v-text-field label="Subject"></v-text-field>
          <v-text-field label="Source"></v-text-field>
          <v-btn id="submitId" class="primary"> submit </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "NastavniMaterijal",
};
</script>

<style>
.formClass{
    padding-left: 50px;
    padding-right: 50px;

}
#submitId{
    margin-bottom: 10px;
}

</style>