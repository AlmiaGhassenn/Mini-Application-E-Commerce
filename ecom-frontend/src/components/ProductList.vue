<template>
  <div class="product-list-container">
    <!-- Title of the page -->
    <h1 class="title">Product List</h1>
    
    <!-- Link to add a new product -->
    <router-link to="/add" class="add-button">Add New Product</router-link>

    <!-- Filter by product availability (dropdown) -->
    <div class="filter-container">
      <label for="in-stock">Filter by availability:</label>
      <select id="in-stock" v-model="inStock" @change="filterProducts">
        <option value="all">All</option>
        <option value="inStock">In Stock</option>
        <option value="outStock">Out of Stock</option>
      </select>
    </div>

    <!-- Display the list of products as cards -->
    <div class="product-cards">
      <!-- Loop through the displayed products and show each product card -->
      <div v-for="product in displayedProducts" :key="product.id" class="product-card">
        <ProductItem
          :product="product"
          @productDeleted="fetchProducts"
        />
      </div>
    </div>

    <!-- Pagination controls -->
    <div v-if="totalPages > 1" class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ProductItem from './ProductItem.vue';

export default {
  components: { ProductItem },
  data() {
    return {
      // List of all products fetched from the API
      products: [],
      
      // Pagination related variables
      currentPage: 1,          // Current page number
      productsPerPage: 5,      // Number of products displayed per page
      
      // Filter state (can be 'all', 'inStock', or 'outStock')
      inStock: 'all',  
    };
  },
  computed: {
    // Filter products based on the 'inStock' filter
    filteredProducts() {
      if (this.inStock === 'inStock') {
        return this.products.filter(product => product.stock > 0);  // Filter in-stock products
      } else if (this.inStock === 'outStock') {
        return this.products.filter(product => product.stock === 0);  // Filter out-of-stock products
      }
      return this.products;  // If no filter, return all products
    },
    // Paginate the filtered products based on the current page
    displayedProducts() {
      const startIndex = (this.currentPage - 1) * this.productsPerPage;
      const endIndex = startIndex + this.productsPerPage;
      return this.filteredProducts.slice(startIndex, endIndex);  // Return products for the current page
    },
    // Calculate the total number of pages for pagination
    totalPages() {
      return Math.ceil(this.filteredProducts.length / this.productsPerPage);  // Calculate total pages based on filtered products
    },
  },
  methods: {
    // Fetch products from the API
    fetchProducts() {
      axios.get('http://127.0.0.1:8000/api/products/')
        .then(response => {
          this.products = response.data;  // Store the fetched products
        })
        .catch(error => {
          console.error(error);  // Log any errors that occur during the fetch
        });
    },
    
    // Method to handle changes in the filter dropdown
    filterProducts() {
      this.currentPage = 1;  // Reset to the first page when the filter changes
    },
    
    // Move to the next page in pagination
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;  // Increment the current page
      }
    },
    
    // Move to the previous page in pagination
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;  // Decrement the current page
      }
    },
  },
  created() {
    this.fetchProducts();  // Fetch products when the component is created
  },
};
</script>

<style scoped>
/* Styling for the product list container */
.product-list-container {
  padding: 2rem;
}

/* Title styling */
.title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 20px;
}

/* Add product button styling */
.add-button {
  display: block;
  background-color: #28a745;
  color: white;
  text-decoration: none;
  padding: 10px 15px;
  margin-bottom: 20px;
  width: 200px;
  text-align: center;
  border-radius: 5px;
  font-size: 18px;
  margin: 0 auto;
}

.add-button:hover {
  background-color: #218838;
}

/* Filter container for the dropdown */
.filter-container {
  margin-bottom: 20px;
  text-align: right;
}

.filter-container label {
  font-size: 16px;
  margin-right: 10px;
}

.filter-container select {
  font-size: 16px;
  padding: 5px 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

/* Layout for the product cards */
.product-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

/* Styling for the product card title (product name) */
.product-card h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.product-card p {
  font-size: 1rem;
  color: #555;
}

/* Styling for the product price */
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

/* Styling for product buttons */
.product-card button {
  background-color: #ffc107;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  margin-top: 10px;
  border-radius: 4px;
}

.product-card button:hover {
  background-color: #e0a800;
}

/* Pagination controls styling */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 20px;
}

.pagination button {
  padding: 10px 15px;
  background-color: #000000;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.pagination span {
  font-size: 16px;
}
</style>
