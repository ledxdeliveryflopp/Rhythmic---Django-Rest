<template>
  <header class="header">
    <div class="header__container">Header</div>
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: center;
}

.header__container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 1100px;
}
</style>
