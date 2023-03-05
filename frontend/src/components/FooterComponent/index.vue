<template>
  <footer class="footer">
    <div class="footer__container">footer</div>
  </footer>
</template>

<script>
export default {
  name: "FooterComponent",
};
</script>

<style scoped lang="scss">
.footer {
  width: 100%;
  display: flex;
  justify-content: center;
}
.footer__container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 1100px;
}
</style>
