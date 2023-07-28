<template>
    <div>
        <h1>Calorie Estimator</h1>
        <input type="file" ref="fileInput" @change="handleFileUpload">
        <button @click="uploadImage">Estimate Calories</button>
        <div v-if="showResult">
            <p>Estimated Calories: {{ estimatedCalories }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            selectedFile: null,
            showResult: false,
            estimatedCalories: null
        };
    },
    methods: {
        handleFileUpload(event) {
            this.selectedFile = event.target.files[0];
        },
        uploadImage() {
            const formData = new FormData();
            formData.append('image', this.selectedFile);

            axios.post('http://localhost:5000/api/estimate_calories', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
                    this.estimatedCalories = response.data.estimated_calories;
                    this.showResult = true;
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
};
</script>
