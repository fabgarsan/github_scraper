<template>
  <div class="row">
    <div class="col-12 mb-2"><h2>Users</h2></div>
    <div class="col-12">
      <form v-on:submit.prevent="loadUsers">
        <div class="row">
          <div class="col-12 col-md-2">
            <input type="submit" value="Fetch Users">
          </div>
        </div>
      </form>
    </div>
    <div class="row">
      <div v-for="user in users" :key="user.id" class="p-2 col-12 col-md-2"
           @click="loadRepositories(user.id)" style="cursor: pointer">
        <div class="border border-1 border-primary p-2">
          <h5>{{ user.name }}</h5>
          <img :src="user.avatar_url" :alt="user.login" style="max-height: 100%; max-width: 100%"/>
          <p>
          </p>
          <div>
            Username: {{ user.login }}
          </div>
          <div>
            Synchronized:
            <p>{{ timeAgo(user.synchronized_at) }} Seconds Ago</p>
          </div>
        </div>
      </div>
    </div>
    <ListRepository v-if="selectedUser" :user="selectedUser.login" :repositories="repositories"/>
  </div>
</template>

<script>
import axios from "axios";
import ListRepository from '../components/ListRepository.vue';

export default {
  name: "ListUser",
  data() {
    return {
      selectedUser: null,
      users: [],
      repositories: [],
    }
  },
  components: {
    ListRepository
  },
  methods: {
    loadUsers: async function () {
      const result = await axios.get(`${process.env.VUE_APP_API}/github/github_user_list/`);
      this.users = result.data;
    },
    loadRepositories: async function (selectedUserId) {
      let params = {
        user_id: selectedUserId
      };
      this.selectedUser = this.users.find(user => user.id === selectedUserId);
      const result = await axios.get(`${process.env.VUE_APP_API}/github/github_user_repositories/`, {params});
      this.repositories = result.data;
    },
    timeAgo: function (synchronized_at) {
      return Math.floor((new Date() - new Date(synchronized_at)) / 1000);
    }
  },

}
</script>

<style scoped>

</style>
