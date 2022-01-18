<template>
  <div id="home">
     <section id="services">
      <h4 class="header-secondary">CORE SERVICES</h4>
      <h3 class="header-primary">Our Services</h3>
      <div class="service-group">
        <div class="service">
          <div class="service-icon">

          </div>
          <div class="service-info">
            <h3>Transport</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque nostrum aliquam molestiae enim ipsam. Repellendus asperiores a minus blanditiis quam.</p>
          </div>
        </div>


        <div class="service">
          <div class="service-icon">

          </div>
          <div class="service-info">
            <h3>Transport</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque nostrum aliquam molestiae enim ipsam. Repellendus asperiores a minus blanditiis quam.</p>
          </div>
        </div>
        <div class="service">
          <div class="service-icon">

          </div>
          <div class="service-info">
            <h3>Transport</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque nostrum aliquam molestiae enim ipsam. Repellendus asperiores a minus blanditiis quam.</p>
          </div>
        </div>

      </div>
    </section>
    <section id="quotes">
      <h2 class="quote-header">QUOTE OF THE DAY</h2>
      <p class="quote">Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora libero ex quos voluptatibus, quaerat necessitatibus ullam accusamus ipsam expedita earum atque omnis repellat eos, tempore delectus iusto aspernatur odit distinctio.</p>
      <p class="quote-author">Lorem, ipsum.</p>
    </section>
    <section id="team">
      <h4 class="header-secondary">MEET THE TEAM</h4>
      <h3 class="header-primary">Council Members</h3>

      <div class="council-members">
        <div class="council-top">
          <div class="vcp"></div>
          <div class="chairperson"></div>
          <div class="vcp"></div>
        </div>

        <div class="council-bottom">
          <div class="mem"></div>
          <div class="mem"></div>
          <div class="mem"></div>
          <div class="mem"></div>
          <div class="mem"></div>
        </div>
      </div>
    </section>
    <section id="social">
      <div class="grid-form">
        <div class="grid-wide"></div>
        <div class="grid-wide"></div>
        <div class="grid-group">
          <div class="grid-group-outer">
            <div class="grid-group-long"></div>
            <div class="grid-group-long"></div>
          </div>
          <div class="grid-group-inner">
            <div class="grid-group-short"></div>
            <div class="grid-group-long"></div>
          </div>
        </div>
      </div>
      <div class="grid-form">
        <div class="grid-long"></div>
        <div class="grid-short"></div>
      </div>
      <div class="grid-form">
        <div class="grid-wide"></div>
        <div class="grid-center-pair">
          <div class="align">
            <div class="grid-box-center"></div>
            <div class="grid-box-center"></div>
          </div>
        </div>
      </div>
      <div class="grid-form">
        <div class="grid-long"></div>
        <div class="grid-short"></div>
      </div>
      <div class="grid-form">
        <div class="grid-wide"></div>
        <div class="grid-wide"></div>
        <div class="grid-group">
          <div class="grid-group-inner">
            <div class="grid-group-short"></div>
            <div class="grid-group-long"></div>
          </div>
          <div class="grid-group-outer margin-2">
            <div class="grid-group-long"></div>
            <div class="grid-group-long"></div>
          </div>
        </div>
      </div>


      <div class="social-header">
        <h4 class="header-secondary">LIFE AT LMU</h4>
        <h3 class="header-primary">CAMPUS</h3>
        <h3 class="header-life">Life</h3>

        <div class="socials">
          <p>Lorem ipsum dolor sit amet.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "HomeComponent",
  setup() {
    return {};
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  #home {
    width: 100vw;
    height: 100vh;
    overflow-y: scroll;
    overflow-x: hidden;
    scroll-snap-type: y mandatory;
  }

  .service-group {
    display: grid;
    grid-template-columns: 300px 300px 300px;
    justify-content: center;
    width: 100%;
    margin-top: 10%;
    gap: 50px;
  }

  .service {
    height: 450px;
    background-color: rgb(255, 255, 255);
    border-radius: 10px;
    box-shadow: 0 0 10px 3px rgba(100, 100, 100, .15);
  }

  .service-icon {
    height: 225px;
  }

  .service-info {
    height: 225px;
    padding: 8%;
    overflow: hidden;
  }

  .service-info p {
    /* font-size: 0.35em; */
  }

  .service-info h3 {
    color: var(--clr--secondary);
  }

  #quotes{
    padding: 0;
    margin: 0;
    justify-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;
    position: relative;
    text-align: center;
    /* display: none; */
  }

  .quote-header {
    padding-bottom: 1%;
    font-size: 2.5rem;
    text-transform: uppercase;
    color: var(--clr--secondary);
  }

  .quote {
    width: 75%;
    padding: 6% 0;
    margin: 1% 0;
    font-size: 1.5rem;
    border-top: 1px solid var(--clr--dark);
  }

  .quote-author {
    width: 25%;
    border-top: 1px solid var(--clr--dark);
    padding: 1%;
    font-size: 1.3rem;
    color: var(--clr--primary);
  }

  #team {
    display: flex;
    flex-direction: column;
    /* display: none; */
  }

  .council-members {
    width: 95%;
    height: 80%;
    justify-self: center;
    align-self: center;
    margin-top: 2%;
  }

  .council-top {
    width: 100%;
    height: 60%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .vcp {
    width: 250px;
    height: 250px;
    border: 5px solid var(--clr--secondary);
    border-radius: 50%;
    margin: 0 5%;
  }

  .chairperson {
    width: 300px;
    height: 300px;
    border: 5px solid var(--clr--secondary);
    border-radius: 50%;
  }

  .council-bottom {
    width: 100%;
    height: 40%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-top: 2%;
  }

  .mem {
    width: 200px;
    height: 200px;
    border: 5px solid var(--clr--secondary);
    border-radius: 50%;
    margin: 0 1%;
  }

  .council-top *:hover, .council-bottom *:hover {
    border-color: var(--clr--primary);
  }

  #social {
    position: relative;
    margin: 0;
    padding: 0 0.5% 1%;
    display: grid;
    grid-template-columns: 22.55% 13.13% 22.55% 13.13% 22.55%;
    gap: 1%;
    justify-content: center;
    /* display: none; */
  }

  .grid-form {
    border-radius: 10px;
    display: flex;
    flex-flow: column-reverse;
    position: relative;
  }

  .grid-wide {
    margin-top: 4%;
    width: 100%;
    padding-top: 56.35%;
    border: 1px solid var(--clr--dark);
    border-radius: inherit;
  }

  .grid-center-pair {
    width: 100%;
    padding-top: 48.04%;
    border-radius: inherit;
    position: relative;
    display: flex;
    flex-direction: row;
  }

  .align {
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    top: 0;
    left: 0;
    border-radius: inherit;
  }

  .grid-box-center {
    height: 100%;
    width: 48%;
    border: 1px solid var(--clr--dark);
    border-radius: inherit;
  }

  .grid-box-center:nth-child(1) {
    margin-right: 4%;
  }

  .grid-long {
    margin-top: 6%;
    width: 100%;
    padding-top: 125%;
    border: 1px solid var(--clr--dark);
    border-radius: inherit;
  }

  .grid-short {
    width: 100%;
    padding-top: 100%;
    border: 1px solid var(--clr--dark);
    border-radius: inherit;
  }

  .grid-group {
    width: 100%;
    border-radius: inherit;
    display: flex;
    flex-flow: row wrap;
    position: relative;
  }

  .grid-group-outer {
    width: 49.65%;
    margin-right: 6.25%;
    display: flex;
    flex-direction: column-reverse;
    border-radius: inherit;
  }

  .grid-group-long {
    width: 100%;
    padding-top: 125.12%;
    border: 1px solid var(--clr--dark);
    border-radius: inherit;
  }

  .grid-group-long:nth-child(1) {
    margin-top: 6%;
  }

  .grid-group-inner {
    width: 44.11%;
    display: flex;
    flex-direction: column-reverse;
    border-radius: inherit;
  }

  .grid-group-short {
    margin-top: 8%;
    width: 100%;
    padding-top: 100%;
    border: 1px solid var(--clr--dark);
    border-radius: inherit;
  }

  .margin-2 {
    margin: 0;
    margin-left: 6.25%;
  }

  .social-header {
    position: absolute;
    left: 50%;
    bottom: 45%;
    transform: translateX(-50%);
    text-align: center;
  }

  .social-header > .socials {
    margin-top: 75%;
  }


</style>
