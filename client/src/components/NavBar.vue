<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark bg-primary">
            <a class="navbar-brand" href="/">FastAPI + Vue Sample</a>
            <button
                class="navbar-toggler"
                type="button"
                data-toggle="collapse"
                data-target="#navbarNav"
                aria-controls="navbarNav"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mr-auto mb-2 mb-md-0">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/"
                            ><i class="fas fa-home"></i> Home</router-link
                        >
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/about"
                            ><i class="fas fa-info-circle"></i> About</router-link
                        >
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/myselectbox">MySelectBox</router-link>
                    </li>
                </ul>
            </div>
        </nav>
    </header>
</template>
