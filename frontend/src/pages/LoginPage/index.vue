<template>
  <v-sheet class="pa-12 h-screen d-flex align-center bgc-dark">
    <v-card class="mx-auto px-6 py-8 w-33" min-width="250">
      <v-form @submit.prevent="onSubmit">
        <v-text-field
          v-model="login"
          :readonly="loading"
          :rules="loginRule"
          class="mb-2"
          label="Логин"
        ></v-text-field>

        <v-text-field
          v-model="password"
          :append-icon="hiddenPassword ? 'visibility' : 'visibility_off'"
          :readonly="loading"
          :rules="passwordRule"
          :type="hiddenPassword ? 'password' : 'text'"
          label="Пароль"
          placeholder="Введите пароль"
          @click:append="() => (hiddenPassword = !hiddenPassword)"
        ></v-text-field>

        <br />

        <v-btn
          :loading="loading"
          block
          class="bgc-highlight"
          size="large"
          type="submit"
          variant="elevated"
        >
          Войти
        </v-btn>
      </v-form>
    </v-card>
  </v-sheet>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      valid: false,
      hiddenPassword: true,
      login: "",
      password: "",
      loginRule: [
        (value) => {
          if (value) return true;

          return "Логин обязателен";
        },
        (value) => {
          if (value?.length <= 5) return true;

          return "Длина не менее 5 символов";
        },
      ],
    };
  },
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
}
</style>
