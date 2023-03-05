<template>
  <div class="page">
    <header-component />
    <router-view />
    <footer-component />
  </div>
</template>

<script setup>
import HeaderComponent from "@/components/HeaderComponent/index.vue";
import FooterComponent from "@/components/FooterComponent/index.vue";
</script>

<style lang="scss">
@use "main";
</style>
