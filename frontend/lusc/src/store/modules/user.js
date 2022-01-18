import axios from 'axios' 

export default {

    state: {
        authKey: ''
    },

    getters: {

    getAuthKey: (state) => {
        alert('getters worked')
        return state.authKey
    }

    },
    mutations: {

    setAuthKey: (state, payload) => {
        state.authKey = 'Token: ' + payload;
    } 

    },
    actions: {

    async getAuthKey({ commit }, payload) {
        await axios.post(
        'http://localhost:8000/api/login/', 
        payload, {
            headers: {
                'Authorization': 'Token ' + 'c4dd1242cd871faaadc6058e98fc431118cd4b9e',
                'Content-Type': 'application/json'
            }
        }).then(response => {
        commit('setAuthKey', response.data.token)
        console.log(response.data)
        }).catch((error) => {
        commit('setAuthKey', error)
        console.log(error)
        })
    }

    },
    modules: {
    }

}