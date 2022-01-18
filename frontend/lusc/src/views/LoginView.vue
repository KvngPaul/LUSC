<template>
    <div class="login">
        <form @submit.prevent="formSubmit" action="POST">
            <h1>LU<br> <span>SC</span></h1>
            <input type="text" name="username" placeholder="Username" v-model="credentials.username" autofocus>
            <input type="password" name="password" placeholder="Password" v-model="credentials.password">
            <button type="submit" class="submit">Submit</button>
            <h4 v-if="authKey != ''"> {{ authKey }} </h4>
        </form>

    </div>
</template>

<script>
import { reactive, toRefs, computed } from 'vue'
import { useStore } from 'vuex'

export default {
    name: 'LoginComponent',
    setup () {
        const store = useStore()

        const state = reactive({
            credentials: {
                username: '',
                password: ''
            }
        })

        const authKey = computed(() => store.state.user.authKey)

        function formSubmit () {
            store.dispatch('getAuthKey', state.credentials)
            state.credentials.username = ''
            state.credentials.password = ''
        }
    
        return {
            ...toRefs(state),
            formSubmit,
            authKey,
        }
    }
}
</script>

<style lang="css" scoped>
    .login {
        width: 100vw;
        height: 100vh;
        position: absolute;
        z-index: 999;
        background-color: var(--clr--light);
    }

    form {
        position: absolute;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        height: 75%;
        width: 33%;
        background-color: white;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 0 5%;
        border-radius: 25px;
        box-shadow: 0px 0px 75px 5px var(--clr--dark--drop);
    }

    form > h1 {
        font-size: 5rem;
        color: var(--clr--primary);
        margin-bottom: 10%;
        line-height: 75%;
    }

    form > h1 span {
        font: inherit;
        color: var(--clr--secondary);
    }

    form > input{
        width: 100%;
        height: 50px;
        border-radius: 10px;
        border: 1.5px solid var(--clr--dark);
        padding-left: 10px;
        margin-bottom: 5%;
    }

    form > input:focus{
        outline: none;
    }

    form .submit {
        width: 65%;
        height: 50px;
        border-radius: 10px;
        border: 1.5px solid var(--clr--primary);
        background-color: inherit;
        font-weight: bold;
        color: var(--clr--primary);
    }

    form .submit:hover {
        background-color: var(--clr--primary);
        color: white;
    }

    form h4 {
        width: 100%;
        color: red;
    }
</style>