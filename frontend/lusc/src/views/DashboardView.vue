<template>
    <div id="dashboard">
        <router-view name= 'userprofile'></router-view>
        <router-view name= 'usertransport'></router-view>
        <router-view name= 'userluggage'></router-view>
        <router-view name= 'usertradefair'></router-view>
    </div>
</template>

<script>
export default {
    name: 'DashboardView',
    components: { 

    }
}
</script>

<style scoped>
    #dashboard {
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1%;
        padding: 1%;
    }

    #dashboard > * {
        border: 2px solid var(--clr--dark);
        width: 100%;
        height: 100%;
    }
</style>