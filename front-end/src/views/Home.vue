<template>
  <v-card>
    <v-layout>
      <v-app-bar prominent>
        <v-toolbar-title>Mock Interview</v-toolbar-title>
        <v-col cols="auto">
          <v-btn @click="startQuestions" color="deep-purple-darken-2" elevation="4">Start Questions</v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn color="deep-purple-darken-2" elevation="4" @click="logout">Logout</v-btn>
        </v-col>
      </v-app-bar>
      <v-main style="height: 968px">
        <div class="h-50">
          <h1 class="text-center text-blue-grey-darken-2 h-50"> Questions </h1>
          <span>
            <h2 :key="quest" class="text-center text-blue-grey-darken-2" v-if="showQuestions">
              {{ quest }}
            </h2>
          </span>
        </div>
        <div>
          <div class="d-flex justify-end align-end fixed-bottom-right">
            <v-card class="w-auto elevation-24">
              <video ref="videoElement" width="350" height="263" class="bg-black" autoplay></video>
              <div class="d-flex justify-center align-center bg-cyan-lighten-5">
                <v-card-actions>
                  <v-btn class="bg-blue-grey-darken-1" @click="startCamaraRecording"><i class="fa-solid fa-video"></i>
                    <v-tooltip activator="parent" location="bottom">Turn on Camara</v-tooltip></v-btn>
                  <v-btn class="bg-blue-grey-darken-1" @click="stopRecording"><i
                      class="fa-solid fa-video-slash"></i><v-tooltip activator="parent" location="bottom">Turn Off
                      Camara</v-tooltip></v-btn>
                  <v-btn class="bg-blue-grey-darken-1" @click="startScreenRecording"><i
                      class="fa-solid fa-desktop"></i><v-tooltip activator="parent" location="bottom">Screen
                      Share</v-tooltip></v-btn>
                  <v-btn class="bg-blue-grey-darken-1" @click="uploadVideo"><i class="fa-solid fa-upload"></i>
                    <v-tooltip activator="parent" location="bottom">Upload</v-tooltip>
                  </v-btn>
                </v-card-actions>
              </div>
            </v-card>
          </div>
        </div>
      </v-main>
    </v-layout>
  </v-card>
</template>
<script>
import axiosInstance from "../services/services.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  data() {
    return {
      stream: null,
      streams: null,
      recorder: null,
      chunks: [],
      isRecording: false,
      questions: [],
      currentIndex: 0,
      quest: "",
      showQuestions: false
    };
  },
  methods: {
    // vedio camara
    async startCamaraRecording() {
      try {
        this.streams = await navigator.mediaDevices.getUserMedia({ video: true, audio: true, });
        this.$refs.videoElement.srcObject = this.streams;
        this.recorder = new MediaRecorder(this.streams);
        this.recorder.ondataavailable = (event) => {
          this.chunks.push(event.data);
        };
        this.recorder.start();
        this.isRecording = true;
      } catch (err) {
        console.error("Error starting recording:", err);
      }
    },
    // screen Record
    async startScreenRecording() {
      try {
        const stream = await navigator.mediaDevices.getDisplayMedia({ video: true, audio: true, });
        this.srcObject = stream;
        this.recorder = new MediaRecorder(stream);
        this.recorder.ondataavailable = (event) => {
          this.chunks.push(event.data);
        };
        this.recorder.start();
        this.isRecording = true;
      } catch (err) {
        console.error("Error starting recording:", err);
      }
    },
    //stop vedio
    stopRecording() {
      if (this.isRecording) {
        this.recorder.stop();
        this.streams.getTracks().forEach((track) => track.stop());
        this.isRecording = false;
      }
    },
    //upload record
    async uploadVideo() {
      const blob = new Blob(this.chunks, { type: "video/webm" });
      const formData = new FormData();
      formData.append("user_video_path", blob, "video.webm");
      try {
        const response = await axiosInstance.post("self-screening/", formData);
        console.log("Video uploaded successfully:", response.data);
      } catch (error) {
        console.error("Error uploading video:", error);
      }
    },
    // for questions
    async fetchQuestions() {
      try {
        const response = await axiosInstance.get("self-screening/");
        this.questions = response.data;
        console.log(this.questions);
      } catch (error) {
        console.error(error);
      };
    },
    startQuestions() {
      this.fetchQuestions().then(() => {
        if (this.questions.length > 0) {
          this.quest = this.questions[0].question;
          console.log(this.quest);
          this.showQuestions = true;
          let currentIndex = 1;
          const intervalId = setInterval(() => {
            if (currentIndex < this.questions.length) {
              let quest = this.questions[currentIndex].question;
              // assign the current question to the `quest` variable
              this.quest = quest;
              console.log(quest);
              currentIndex++;
            } else {
              clearInterval(intervalId);
            }
          }, 5000);
        }
      });
    },
    async logout() {
      try {
        // clear user data from local storage or state
        localStorage.removeItem("token");
        // redirect the user to the login page
        this.$router.push("/login");
        toast.success("Logged out successfully", {
          transition: toast.TRANSITIONS.BOUNCE,
          position: toast.POSITION.TOP_RIGHT,
          autoClose: 2000,
        });
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>