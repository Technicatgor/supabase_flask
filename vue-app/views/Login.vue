<script setup>
import LoginForm from "../src/components/LoginForm.vue";
</script>
<template>
  <div>
    <h1>Login</h1>
    <LoginForm />
    <router-link :to="{ name: 'Home' }">Home</router-link>
  </div>
</template>
