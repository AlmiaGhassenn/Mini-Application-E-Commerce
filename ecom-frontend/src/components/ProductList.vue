<template>
  <div class="product-list-container">
    <h1 class="title">Product List</h1>
    <router-link to="/add" class="add-button">Add New Product</router-link>


    <div class="filter-container">
      <label for="in-stock">Filter by availability:</label>
      <select id="in-stock" v-model="inStock" @change="filterProducts">
        <option value="all">All</option>
        <option value="inStock">In Stock</option>
        <option value="outStock">Out of Stock</option>
      </select>
    </div>

    <div class="product-cards">
      <div v-for="product in displayedProducts" :key="product.id" class="product-card">
        <ProductItem
          :product="product"
          @productDeleted="fetchProducts"
        />
      </div>
    </div>

   
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
      products: [],  
      currentPage: 1,  
      productsPerPage: 5,  
      inStock: 'all',  
    };
  },
  computed: {
    filteredProducts() {
      if (this.inStock === 'inStock') {
        return this.products.filter(product => product.stock > 0);  
      } else if (this.inStock === 'outStock') {
        return this.products.filter(product => product.stock === 0);  
      }
      return this.products;  
    },
    displayedProducts() {
      const startIndex = (this.currentPage - 1) * this.productsPerPage;
      const endIndex = startIndex + this.productsPerPage;
      return this.filteredProducts.slice(startIndex, endIndex);  
    },
    totalPages() {
      return Math.ceil(this.filteredProducts.length / this.productsPerPage);  
    },
  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:8000/api/products/')
        .then(response => {
          this.products = response.data;  
        })
        .catch(error => {
          console.error(error);
        });
    },
    filterProducts() {
      this.currentPage = 1;  
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;  
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;  
      }
    },
  },
  created() {
    this.fetchProducts();  
  },
};
</script>

<style scoped>
.product-list-container {
  padding: 2rem;
}

.title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 20px;
}

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

.product-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
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
