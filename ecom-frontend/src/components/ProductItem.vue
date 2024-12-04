<template>
  <div class="product-card">
    <!-- Display the product name -->
    <h2>{{ product.name }}</h2>
    
    <!-- Display the product description -->
    <p>Description : {{ product.description }}</p>
    
    <!-- Display the product price -->
    <p class="price">Price: ${{ product.price }}</p>
    
    <!-- Conditional styling for stock status -->
    <p :class="{
      'out-of-stock': product.stock === 0,  // Apply 'out-of-stock' class if stock is 0
      'in-stock': product.stock >= 1      // Apply 'in-stock' class if stock is 1
    }">
      Stock: 
      <!-- Show 'in stock' if stock is greater than 0 -->
      <span v-if="product.stock > 0"> in stock</span>
      <!-- Show 'Out of stock' if stock is 0 -->
      <span v-else>Out of stock</span>
    </p>

    <!-- Button to delete the product -->
    <button class="delete-btn" @click="deleteProduct">Delete</button>
    
    <!-- Link to the edit page for the product -->
    <router-link :to="'/edit/' + product.id">
      <button class="edit-btn">Edit</button>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  // Expect a 'product' object as a prop from the parent component
  props: ['product'],
  methods: {
    // Method to delete the product
    deleteProduct() {
      axios
        .delete(`http://127.0.0.1:8000/api/products/${this.product.id}/`) // API call to delete the product
        .then(() => {
          this.$emit('productDeleted', this.product.id); // Emit an event to notify the parent that the product was deleted
        })
        .catch(error => {
          console.error(error); // Log errors if the delete operation fails
        });
    },
  },
};
</script>

<style scoped>
/* Container styling for the product card */
.product-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 15px;
  width: 250px;
  text-align: center;
  margin: 10px;
}

/* Styling for the product name */
.product-card h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

/* General styling for paragraph elements */
.product-card p {
  font-size: 1rem;
  color: #555;
}

/* Styling for the price */
.product-card .price {
  font-weight: bold;
  font-size: 1.2rem;
  color: #333;
}

/* Styling for out-of-stock status */
.product-card .out-of-stock {
  color: red;
  font-weight: bold;
}

/* Styling for in-stock status */
.product-card .in-stock {
  color: green;
  font-weight: bold;
}

/* General styling for buttons */
.product-card button {
  padding: 8px 12px;
  cursor: pointer;
  margin-top: 10px;
  border-radius: 4px;
  font-size: 14px;
  border: 2px solid transparent; /* Transparent border */
  transition: all 0.3s ease; /* Smooth transition for hover effect */
}

/* Delete button normal state */
.product-card .delete-btn {
  background-color: white;
  color: black;
  border: 2px solid black;
}

/* Delete button hover state */
.product-card .delete-btn:hover {
  background-color: red;
  color: white;
  border-color: red;
}

/* Edit button normal state */
.product-card .edit-btn {
  background-color: white;
  color: black;
  border: 2px solid black;
  margin-left: 10px;
}

/* Edit button hover state */
.product-card .edit-btn:hover {
  background-color: green;
  color: white;
  border-color: green;
}
</style>
