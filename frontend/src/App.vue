<template>
  <div class="container-fluid" id="app">
    <div class="row p-2">
      <div class="col-12 col-md-8">
        <form v-on:submit.prevent="sendForm">
          <div class="row" style="color: red; border: solid black 1px">
            <div class="col-12">
              <h1>Testing Dashboard</h1>
            </div>
            <div class="p-3 col-12 col-md-6">Username to scrape:
              <input
                  type="text"
                  v-model="username">
            </div>
            <div class="p-3 col-12 col-md-6">
              Run in
              <input
                  type="number"
                  v-model="countdown"> seconds
            </div>
            <div class="p-3 col-12">
              <input type="submit" value="Send" :disabled="sendIsDisable">
            </div>
          </div>
        </form>
      </div>
      <div class="col-12 col-md-4">
        <ListUserSynchronized :list="socketMessage"/>
      </div>
    </div>
    <div>
      <ListUser/>
    </div>
  </div>
</template>

<script>
import ListUser from './components/ListUser.vue';
import ListUserSynchronized from './components/ListUserSynchronized.vue';
import {io} from 'socket.io-client';
import axios from "axios";

const socket = io(process.env.VUE_APP_SOCKET_ENDPOINT);

export default {
  name: 'App',
  data() {
    return {
      timeStampToSent: new Date(),
      username: "",
      countdown: 5,
      isConnected: false,
      socketMessage: []
    }
  },
  components: {
    ListUser,
    ListUserSynchronized
  },
  computed: {
    sendIsDisable: function () {
      return this.username === '';
    }
  },
  created() {
    socket.on("chat message", (data) => {
      this.socketMessage = this.socketMessage.filter(item => item !== data)
      this.socketMessage.push(data);
    });
  },
  beforeUnmount() {
    socket.disconnect()
  },
  methods: {
    sendForm: async function () {
      await axios.post(`${process.env.VUE_APP_API}/github/cron_query/`, {
        username: this.username,
        countdown: this.countdown,
      });
      this.username = '';
      this.countdown = 5;
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
