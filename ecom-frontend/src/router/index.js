// Import necessary modules from vue-router
import { createRouter, createWebHistory } from 'vue-router'; 
import ProductList from '../components/ProductList.vue'; // Import ProductList component
import ProductForm from '../components/ProductForm.vue'; // Import ProductForm component

// Define the routes for the application
const routes = [
  // Route for the homepage, displays the list of products
  { path: '/', component: ProductList },

  // Route for adding a new product, displays the product form
  { path: '/add', component: ProductForm },

  // Route for editing an existing product, passing the product ID as a route parameter
  { path: '/edit/:id', component: ProductForm, props: true }, // `props: true` allows route params to be passed as props to the component
];

// Create the Vue Router instance
const router = createRouter({
  history: createWebHistory(), // Use HTML5 history mode (removes the hash from the URL)
  routes, // Pass the defined routes to the router
});

// Export the router instance to be used in the main Vue instance
export default router;
