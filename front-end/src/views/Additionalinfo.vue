<template>
  <v-img :width="2000" height="969" cover
    src="https://images.unsplash.com/photo-1625225233840-695456021cde?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
    <v-container class="d-flex align-center justify-center">
      <v-card title="Provide Some Additional Information to Set-up Your Account"
        class="w-50 text-center text-grey-darken-3" elevation="24" rounded="lg">
        <v-container>
          <v-text-field clearable label="Phone Number" type="number" color="blue" variant="solo"
            v-model="phone"></v-text-field>
          <v-select label="Designation" color="blue" variant="solo" :items="['Front-End', 'Back-End', 'Full Stack']"
            v-model="designation"></v-select>
          <v-text-field label="Years of Experiance" color="blue" variant="solo" type="number"
            v-model="experiance"></v-text-field>
          <v-select label="Interested In" color="blue" multiple variant="solo"
            :items="['Design', 'Integration', 'Database', 'Cloud', 'DevOps']" v-model="interest"></v-select>
        </v-container>
        <router-link to="/login" class="link">
          <v-btn class="mb-8" color="blue" size="large" @click="additionalInfo">
            Submit
          </v-btn>
        </router-link>
      </v-card>
    </v-container>
  </v-img>
</template>
<script>
import axiosInstance from "../services/services.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  data() {
    return {
      phone: "",
      designation: "",
      experiance: "",
      interest: "",
    };
  },
  methods: {
    additionalInfo() {
      const info = {
        email: this.$route.params.email,
        phone: this.phone,
        designation: this.designation,
        experiance: this.experiance,
        interest: JSON.stringify(this.interest),
      };
      axiosInstance
        .post("register-update/", info)
        .then((response) => {
          toast.success("Additional information added successfully", {
            transition: toast.TRANSITIONS.BOUNCE,
            position: toast.POSITION.TOP_RIGHT,
            autoClose: 2000,
          });
          console.log("Response from server:", response.data);
        })
        .catch((error) => {
          console.log("Error from server:", error);
        });
      console.log("info", info);
    },
  },
};
</script>
<style scoped>
.link {
  text-decoration: none;
}
</style>