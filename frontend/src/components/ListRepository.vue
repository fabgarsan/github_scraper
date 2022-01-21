<template>
  <div class="row">
    <div class="col-12 mb-2"><h2>Repositories from {{ this.user }} </h2></div>
    <ul id="example-1">
      <li v-for="repository in repositories" :key="repository.id">
        {{ repository.full_name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ListRepository",
  props: {
    repositories: [],
    user: String
  },
}
</script>

<style scoped>

</style>
