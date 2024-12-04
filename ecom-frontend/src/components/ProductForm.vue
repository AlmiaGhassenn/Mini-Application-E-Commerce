<template>
  <div class="form-container">
    <!-- Display the form title based on whether it's an edit or add operation -->
    <h1>{{ form.id ? 'Edit Product' : 'Add Product' }}</h1> 
    <form @submit.prevent="submitForm">
      <!-- Input field for the product name -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" v-model="form.name" id="name" required />
      </div>
      
      <!-- Input field for the product description -->
      <div class="form-group">
        <label for="description">Description:</label>
        <textarea v-model="form.description" id="description"></textarea>
      </div>
      
      <!-- Input field for the product price -->
      <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" v-model="form.price" id="price" required min="0" step="0.01" />
      </div>
      
      <!-- Input field for the product stock -->
      <div class="form-group">
        <label for="stock">Stock:</label>
        <input type="number" v-model="form.stock" id="stock" required min="0" />
      </div>
      
      <!-- Submit button with dynamic label based on operation -->
      <button type="submit" class="submit-button">
        {{ form.id ? 'Update Product' : 'Add Product' }} 
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      // Data model for the product form
      form: {
        id: null,           // Product ID (null for new product)
        name: '',           // Product name
        description: '',    // Product description
        price: 0,           // Product price
        stock: 0,           // Product stock
      },
    };
  },
  methods: {
    // Fetch product details for editing
    fetchProduct() {
      const productId = this.$route.params.id; // Get product ID from the route parameters
      axios.get(`http://127.0.0.1:8000/api/products/${productId}/`)
        .then(response => {
          this.form = response.data; // Populate the form with fetched product data
        })
        .catch(error => {
          console.error(error); // Log errors if fetching fails
        });
    },
    
    // Handle form submission (add or update based on the form's state)
    submitForm() {
      if (this.form.id) {
        this.updateProduct(); // Call update if editing
      } else {
        this.addProduct();    // Call add if creating
      }
    },
    
    // Add a new product
    addProduct() {
      axios.post('http://127.0.0.1:8000/api/products/', this.form)
        .then(() => {
          this.$router.push('/'); // Redirect to the product list after adding
        })
        .catch(error => {
          console.error(error); // Log errors if adding fails
        });
    },
    
    // Update an existing product
    updateProduct() {
      const productId = this.$route.params.id; // Get product ID from the route parameters
      axios.put(`http://127.0.0.1:8000/api/products/${productId}/`, this.form)
        .then(() => {
          this.$router.push('/'); // Redirect to the product list after updating
        })
        .catch(error => {
          console.error(error); // Log errors if updating fails
        });
    },
  },
  // Lifecycle hook to fetch product data if editing
  created() {
    if (this.$route.params.id) {
      this.fetchProduct(); // Fetch product data for editing
    }
  },
};
</script>

<style scoped>
/* Container styling for the form */
.form-container {
  padding: 2rem;
  max-width: 600px;
  margin: 0 auto;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Title styling */
h1 {
  text-align: center;
  margin-bottom: 20px;
}

/* Form group styling */
.form-group {
  margin-bottom: 1.5rem;
}

/* Label styling */
label {
  display: block;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

/* Input and textarea styling */
input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

/* Submit button styling */
button.submit-button {
  width: 100%;
  padding: 12px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
}

button.submit-button:hover {
  background-color: #218838;
}
</style>
