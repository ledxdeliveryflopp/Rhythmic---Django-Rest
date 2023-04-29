<template>
  <v-sheet class="pa-12 h-screen d-flex align-center login-page">
    <v-card
      class="mx-auto px-6 py-8 w-33 rounded bg-opacity-50"
      max-width="500"
      min-width="250"
    >
      <v-form v-model="valid" @submit.prevent="onSubmit">
        <v-text-field
          v-model="login"
          :readonly="loading"
          :rules="loginRule"
          class="mb-2 text-field"
          label="Логин"
          name="login"
        ></v-text-field>

        <v-text-field
          v-model="password"
          :append-inner-icon="
            hiddenPassword ? 'mdi-eye-outline' : 'mdi-eye-off-outline'
          "
          :readonly="loading"
          :rules="passwordRule"
          :type="hiddenPassword ? 'password' : 'text'"
          label="Пароль"
          name="password"
          placeholder="Введите пароль"
          @click:appendInner="() => (hiddenPassword = !hiddenPassword)"
        ></v-text-field>

        <br />

        <v-btn
          :disabled="!valid"
          :loading="loading"
          block
          class="button"
          size="large"
          type="submit"
          variant="elevated"
        >
          Войти
        </v-btn>
      </v-form>
      <p class="error-text mt-2">{{ error }}</p>
    </v-card>
  </v-sheet>
</template>

<script>
import { loginService } from "@/helpers/api/user";

export default {
  name: "LoginPage",
  data() {
    return {
      error: "",
      loading: false,
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
          if (value?.length >= 5) return true;
          return "Длина не менее 5 символов";
        },
      ],
      passwordRule: [
        (value) => {
          if (value) return true;
          return "Пароль обязателен";
        },
        (value) => {
          if (value?.length >= 5) return true;
          return "Длина не менее 5 символов";
        },
      ],
    };
  },
  computed: {
    preparingFormData() {
      return {
        username: this.login,
        password: this.password,
      };
    },
  },
  methods: {
    onSubmit() {
      this.loading = true;
      loginService(this.preparingFormData)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          if (error.non_field_errors) {
            this.error = error.non_field_errors[0];
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="scss">
@use "style";
</style>
