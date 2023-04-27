<template>
  <header-component />
  <router-view />
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent/index.vue";

export default {
  name: "App",
  components: { HeaderComponent },
};
</script>

<style scoped></style>
