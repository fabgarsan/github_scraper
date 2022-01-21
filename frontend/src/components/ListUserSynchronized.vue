<template>
  <div class="row">
    <div class="col-12 mb-2"><h2>Synchronized</h2></div>
    <ul id="example-1">
      <li v-for="user in list" :key="user">
        {{ user }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ListUserSynchronized",
  props: {
    list: [],
  }
}
</script>

<style scoped>

</style>
