<template>
<div>
    <router-view />
  </div>
</template>
<script>
export default {
  mounted() {
    const token = localStorage.getItem("token");
    if (token) {
      // Redirect to home page
      this.$router.push("/help");
    } else {
      // Redirect to login page
      this.$router.push("/login");
    }
  },
};
</script>
