<template>
  <div id="app">
    <nav>
      <router-link to="/" class="nav-link">Home</router-link>
      <router-link to="/add" class="nav-link">Add New Product</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f7f7f7;
  min-height: 100vh;
}

nav {
  background-color: #000000;
  padding: 1rem;
  text-align: center;
}

nav .nav-link {
  color: white;
  text-decoration: none;
  margin: 0 1rem;
  font-size: 16px;
}

nav .nav-link:hover {
  text-decoration: underline;
}
</style>
