<template>
  <div class="dashboard-container">
<!--    <div class="dashboard-text">name: {{ name }}</div>-->
    <div class="header">
      <h1>焊装车间生产线监控系统</h1>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
  .header{
    position: center;
    text-align: center;
    color:#303133;
  }
</style>
