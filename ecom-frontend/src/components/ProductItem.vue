<template>
  <div class="product-card">
    <h2>{{ product.name }}</h2>
    <p>Description : {{ product.description }}</p>
    <p class="price">Price: ${{ product.price }}</p>
    <p :class="{
      'out-of-stock': product.stock === 0,
      'in-stock': product.stock === 1
    }">
      Stock: 
      <span v-if="product.stock > 0"> in stock</span>
      <span v-else>Out of stock</span>
    </p>
    <button class="delete-btn" @click="deleteProduct">Delete</button>
    <router-link :to="'/edit/' + product.id">
      <button class="edit-btn">Edit</button>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['product'],
  methods: {
    deleteProduct() {
      axios
        .delete(`http://127.0.0.1:8000/api/products/${this.product.id}/`)
        .then(() => {
          this.$emit('productDeleted', this.product.id);
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.product-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 15px;
  width: 250px;
  text-align: center;
  margin: 10px;
}

.product-card h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.product-card p {
  font-size: 1rem;
  color: #555;
}

.product-card .price {
  font-weight: bold;
  font-size: 1.2rem;
  color: #333;
}

.product-card .out-of-stock {
  color: red;
  font-weight: bold;
}

.product-card .in-stock {
  color: green;
  font-weight: bold;
}

.product-card button {
  padding: 8px 12px;
  cursor: pointer;
  margin-top: 10px;
  border-radius: 4px;
  font-size: 14px;
  border: 2px solid transparent; 
  transition: all 0.3s ease; 
}


.product-card .delete-btn {
  background-color: white;
  color: black;
  border: 2px solid black;
}


.product-card .delete-btn:hover {
  background-color: red;
  color: white;
  border-color: red;
}


.product-card .edit-btn {
  background-color: white;
  color: black;
  border: 2px solid black;
  margin-left: 10px;
}


.product-card .edit-btn:hover {
  background-color: green;
  color: white;
  border-color: green;
}
</style>
