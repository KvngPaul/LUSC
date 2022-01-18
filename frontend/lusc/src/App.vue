<template>
  <router-view/>
</template>

<style>

:root{
  --clr--light: rgba(244, 244, 244, 1);
  --clr--dark: rgba(100, 100, 100, 1);
  --clr--dark--drop: rgba(100, 100, 100, .3);

  --clr--primary: rgba(25, 135, 84, 1);
  --clr--secondary: rgba(195, 141, 47, 1);
}

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  font-size: 1rem;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 1em;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: var(--clr--light);
  color: var(--clr--dark);
  width: 100vw;
  height: 100vh;
  overflow: hidden;
} 

a.router-link-exact-active {
  color: var(--clr--primary);
  /* fill: rgba(25, 135, 84, 0.95); */
  font-weight: bold;
  text-decoration: none;
}

a {
  color: var(--clr--secondary);
  font-weight: bold;
  text-decoration: none;
}

a:hover {
  color: var(--clr--primary);
  cursor: pointer;
}


h3 {
  font-size: 1.3em;
  margin-bottom: .5%;
}

h4 {
  font-size: 1.1em;
}

section {
  margin: 0;
  width: 100vw;
  height: 100vh;
  position: relative;
  padding: 5% 10%;
  overflow: hidden;
  scroll-snap-align: start;
}

.header-secondary {
  font-size: 1rem;
  color: var(--clr--secondary);
  font-weight: bold;
}

.header-primary {
  font-size: 2rem;
  color: var(--clr--primary);
  font-weight: 600;
}

 table {
  margin-top: 3%;
  width: 100%;
  height: 65%;
  border-collapse: collapse;
}
thead td {
  font-weight: bold;
  vertical-align: bottom;
  padding-bottom: 5px;
}

td {
  border-bottom: 1px solid var(--clr--dark);
  border-collapse: collapse;
  font-size: .9rem;
}

</style>