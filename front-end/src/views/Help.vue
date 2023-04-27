<template>
  <div>
    <h1 class="text-center mt-5 text-grey-darken-2">Mock Interview</h1>
    <h3 class="text-center text-blue-grey-darken-1">
      A quick way to prepare your next Interview in
      <span class="bg-deep-purple-lighten-5 w-100 pa-1 text-blue-accent-4 font-weight-bold">{{ currentWord }}</span>
    </h3>
    <h3 class="text-center text-blue-grey-darken-1">
      Practice key questions, get insight about your aneswer and get more
    </h3>
    <h3 class="text-center text-blue-grey-darken-1">
      comfortable interviewing
    </h3>
  </div>
  <v-layout>
    <v-container class="d-flex align-center justify-center mt-16">
      <v-card class="w-75" elevation="24">
        <v-main>
          <v-card-text class="text-center">
            <h3 class="">Rules And Regulations</h3>
            <v-container>
              <v-col justify="space-around">
                <v-expansion-panels v-model="dos" class="mb-5">
                  <v-expansion-panel title="Do's" value="dos"
                    text="1. Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                      Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                      Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                      Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                      Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima">
                  </v-expansion-panel>
                </v-expansion-panels>
                <v-expansion-panels v-model="dont">
                  <v-expansion-panel title="Don't" value="dont"
                    text="1. Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima">
                  </v-expansion-panel>
                </v-expansion-panels>
                <router-link to="/" class="link"><v-btn :disabled="!bothChecked" class="mt-5 bg-blue">Start
                    Practicing</v-btn></router-link>
              </v-col>
            </v-container>
          </v-card-text>
        </v-main>
      </v-card>
    </v-container>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      dos: false,
      dont: false,
      words: ["Front - End", "Back - End", "Full Stack"],
      currentWord: "Front-End",
      index: 0,
    };
  },
  computed: {
    bothChecked() {
      return this.dos && this.dont;
    },
  },
  mounted() {
    setInterval(() => {
      this.currentWord = this.words[this.index];
      this.index = (this.index + 1) % this.words.length;
    }, 2000);
  },
};
</script>
<style scoped>
.link {
  text-decoration: none;
}
</style>