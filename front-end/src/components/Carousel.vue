<template> 
<div class="mt-12">
    <v-img
  max-height="150"
  max-width="250"
  src="https://www.twilightitsolutions.com/web/image/website/1/logo/Twilight%20IT%20Solutions?unique=0dd685d"
></v-img>
</div>

<div class="ma-16 mt-12">
    <div class="d-flex justify-content-center align-items-center mt-16">
      <v-carousel cycle height="600" width="80%" class="mx-auto my-auto" hide-delimiter-background show-arrows="hover">
        <v-carousel-item :src="Slide1" class="carousel-item"></v-carousel-item>
        <v-carousel-item :src="Slide2" class="carousel-item"></v-carousel-item>
        <v-carousel-item :src="Slide3" class="carousel-item"></v-carousel-item>
      </v-carousel>
    </div>
</div>
  </template> 
  <script>
  import Slide1 from '@/assets/Login/46207-programmer-1.gif';
  import Slide2 from '@/assets/Login/bwgg.gif';
  import Slide3 from '@/assets/Login/fa7b4bdc3b2f73e749e5c2c646d4ae13.gif';
  
  export default {
    data() {
      return {
        Slide1,
        Slide2,
        Slide3,
      };
    },
  };
  </script>
  
  <style scoped>
  .carousel-item {
    object-fit: none !important;
  }
  </style>
  