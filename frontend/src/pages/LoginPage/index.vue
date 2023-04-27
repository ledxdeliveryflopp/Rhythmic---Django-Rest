<template>
  <v-sheet class="mx-auto" width="300">
    <v-form @submit.prevent>
      <v-text-field
        v-model="login"
        :rules="[requiredField, minChar]"
        label="First name"
      ></v-text-field>
      <v-btn block class="mt-2" type="submit">Submit</v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
import { minChar, requiredField } from "@/helpers/validation/validation";

export default {
  name: "LoginPage",
  computed: {
    requiredField() {
      return requiredField();
    },
    minChar() {
      return minChar();
    },
  },
  data() {
    return {
      login: "",
      password: "",
    };
  },
};
</script>

<style scoped></style>
