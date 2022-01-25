<template>
    <link
        rel="stylesheet"
        type="text/css"
        href="http://cdn.bootcss.com/select2/4.0.0/css/select2.css"
    />
    <link
        rel="stylesheet"
        type="text/css"
        href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.css"
    />
    <link
        rel="stylesheet"
        type="text/css"
        href="https://select2.github.io/select2-bootstrap-theme/css/select2-bootstrap.css"
    />

    <!-- Google Font: Source Sans Pro -->
    <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"
    />
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="../../../static/plugins/fontawesome-free/css/all.min.css" />
    <div id="app">
        <NavBar />
        <div class="main container">
            <router-view v-slot="{ Component }">
                <keep-alive>
                    <component :is="Component" />
                </keep-alive>
            </router-view>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue';
export default {
    components: {
        NavBar,
    },
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
