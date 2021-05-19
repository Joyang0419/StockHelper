<template>
  <ol class="breadcrumb" style="background-color: #fafafa; color: blue">
    <li class="breadcrumb-item" :class="{ active: breadcrumbList.length == index + 1}" v-for="(item, index) in breadcrumbList">
      <a href="" @click="routeTo(index)">{{ item.name }}</a>
    </li>
  </ol>
</template>

<script>
export default {
    name: 'Breadcrumb',
    data() {
        return {
            breadcrumbList: []
        }
    },
    mounted () { this.updateList() },
    watch: { '$route' () { this.updateList() } },
    methods: {
    routeTo (pRouteTo) {
        if (this.breadcrumbList[pRouteTo].path) this.$router.push(this.breadcrumbList[pRouteTo].path)
    },
    updateList () { this.breadcrumbList = this.$route.meta.breadcrumb }
    }
}
</script>

<style scoped>
.active {
  color: #DE6262;
}

</style>
