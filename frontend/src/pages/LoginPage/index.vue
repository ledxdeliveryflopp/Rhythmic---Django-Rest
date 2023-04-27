<template>
  <div class="login-page">
    <v-sheet class="mx-auto" width="300">
      <v-form @submit.prevent>
        <v-text-field
          v-model="login"
          :rules="loginRule"
          label="Логин"
        ></v-text-field>
        <v-text-field v-model="password" label="Пароль"></v-text-field>
        <v-btn block class="mt-2" type="submit">Submit</v-btn>
      </v-form>
    </v-sheet>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      valid: false,
      login: "",
      password: "",
      loginRule: [
        (value) => {
          if (value) return true;

          return "Name is requred.";
        },
        (value) => {
          if (value?.length <= 10) return true;

          return "Name must be less than 10 characters.";
        },
      ],
    };
  },
};
</script>

<style scoped></style>
