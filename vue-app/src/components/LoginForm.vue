<template>
  <div
    class="w-full max-w-sm mx-auto bg-white p-8 rounded-xl shadow-md flex items-center justify-between flex-col"
  >
    <h2 class="text-3xl font-semibold mb-6 text-gray-700">Login</h2>
    <form @submit.prevent="handleSubmit" class="w-full">
      <input
        type="email"
        name="email"
        id="email"
        v-model="email"
        placeholder="Email address"
        required
        class="bg-gray-100 border-b-2 border-gray-200 text-sm rounded-lg p-3 mb-6 focus:outline-none focus:border-blue-500 w-full"
      />
      <input
        type="password"
        name="password"
        id="password"
        v-model="password"
        placeholder="Password"
        required
        class="bg-gray-100 border-b-2 border-gray-200 text-sm rounded-lg p-3 focus:outline-none focus:border-blue-500 w-full"
      />
      <div v-if="passwordError" class="text-red-600 text-sm">
        {{ passwordError }}
      </div>
      <button
        type="submit"
        @click="handleSubmit"
        class="bg-blue-500 hover:bg-blue-700 text-white font-semibold py-2 rounded-lg w-full mt-8"
      >
        Sign in
      </button>
    </form>
    <p>{{ email }}</p>
    <p>{{ password }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      passwordError: "",
    };
  },
  methods: {
    async handleSubmit() {
      this.passwordError =
        this.password.length > 7
          ? ""
          : "Password must be at least 8 characters long.";
      window.email = this.email;
      this.$router.push({ name: "Home" });
    },
  },
};
</script>
