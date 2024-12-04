<template>
  <div class="form-container">
    <h1>{{ form.id ? 'Edit Product' : 'Add Product' }}</h1> 
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" v-model="form.name" id="name" required />
      </div>
      <div class="form-group">
        <label for="description">Description:</label>
        <textarea v-model="form.description" id="description"></textarea>
      </div>
      <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" v-model="form.price" id="price" required min="0" step="0.01" />
      </div>
      <div class="form-group">
        <label for="stock">Stock:</label>
        <input type="number" v-model="form.stock" id="stock" required min="0" />
      </div>
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
      form: {
        id: null,
        name: '',
        description: '',
        price: 0,
        stock: 0,
      },
    };
  },
  methods: {
    fetchProduct() {
      const productId = this.$route.params.id;
      axios.get(`http://127.0.0.1:8000/api/products/${productId}/`)
        .then(response => {
          this.form = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    submitForm() {
      if (this.form.id) {
        
        this.updateProduct();
      } else {
        
        this.addProduct();
      }
    },
    addProduct() {
      axios.post('http://127.0.0.1:8000/api/products/', this.form)
        .then(() => {
          this.$router.push('/'); 
        })
        .catch(error => {
          console.error(error);
        });
    },
    updateProduct() {
      const productId = this.$route.params.id;
      axios.put(`http://127.0.0.1:8000/api/products/${productId}/`, this.form)
        .then(() => {
          this.$router.push('/'); 
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
  created() {
    if (this.$route.params.id) {
      this.fetchProduct();  
    }
  },
};
</script>

<style scoped>
.form-container {
  padding: 2rem;
  max-width: 600px;
  margin: 0 auto;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

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
