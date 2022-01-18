<template>
    <div id="dashboard">
        <div class="container">
            <div class="header">
                <div class="nameplate">
                    <div class="namepic">

                    </div>
                    <p class="hi">Hi, Paul</p>
                </div>
            </div>
            <div class="dashboard-grid">
                <div class="luggage">
                    <h3>Luggage Bookings</h3>
                    <table>
                        <thead>
                            <td>Luggage Id</td>
                            <td>Luggage</td>
                            <td>Date Collected</td>
                        </thead>
                        <tbody>
                            <tr>
                                <td>#2108</td>
                                <td>Box</td>
                                <td>30 Sep 2021</td>
                            </tr>
                            <tr>
                                <td>#2108</td>
                                <td>Bag</td>
                                <td>30 Sep 2021</td>
                            </tr>
                            <tr>
                                <td>#2108</td>
                                <td>Bucket</td>
                                <td>30 Sep 2021</td>
                            </tr>
                            <tr>
                                <td>#2108</td>
                                <td>Box</td>
                                <td>30 Sep 2021</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="actions">
                        <button class="history" @click="openPopups('Luggage')">View History</button>
                        <button class="bookings">Book Space</button>
                    </div>
                </div>
                <div class="transport">
                    <h3>Transport Bookings</h3>
                    <table>
                        <thead>
                            <td>Transport Id</td>
                            <td>Destination</td>
                            <td>Date Booked</td>
                            <td>Status</td>
                        </thead>
                        <tbody>
                            <tr>
                                <td>#1708</td>
                                <td>Ilorin</td>
                                <td>30 Sep 2021</td>
                                <td><div class="status-icon"></div></td>
                            </tr>
                            <tr>
                                <td>#1708</td>
                                <td>Ilorin</td>
                                <td>30 Sep 2021</td>
                                <td><div class="status-icon"></div></td>
                            </tr>
                            <tr>
                                <td>#1708</td>
                                <td>Ilorin</td>
                                <td>30 Sep 2021</td>
                                <td><div class="status-icon"></div></td>
                            </tr>
                            <tr>
                                <td>#1708</td>
                                <td>Ilorin</td>
                                <td>30 Sep 2021</td>
                                <td><div class="status-icon"></div></td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="actions">
                        <button class="history" @click="openPopups('Transport')">View History</button>
                        <button class="bookings">Book Space</button>
                    </div>
                </div>
                <div class="sidebar"></div>
                <div class="grid-group">
                    <div class="tradefair">
                        <h3>TradeFair Bookings</h3>
                        <table>
                            <thead>
                                <td>Transport Id</td>
                                <td>Date Booked</td>
                                <td>Duration</td>
                                <td>Payment</td>
                                <td>Status</td>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>#1708</td>
                                    <td>30 Sep 2021</td>
                                    <td>3</td>
                                    <td>₦3 000</td>
                                    <td><div class="status-icon"></div></td>
                                </tr>
                                <tr>
                                    <td>#1708</td>
                                    <td>30 Sep 2021</td>
                                    <td>3</td>
                                    <td>₦3 000</td>
                                    <td><div class="status-icon"></div></td>
                                </tr>
                                <tr>
                                    <td>#1708</td>
                                    <td>30 Sep 2021</td>
                                    <td>3</td>
                                    <td>₦3 000</td>
                                    <td><div class="status-icon"></div></td>
                                </tr>
                                <tr>
                                    <td>#1708</td>
                                    <td>30 Sep 2021</td>
                                    <td>3</td>
                                    <td>₦3 000</td>
                                    <td><div class="status-icon"></div></td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="trade-actions">
                            <button class="history" @click="openPopups('Tradefair')">View History</button>
                            <button class="bookings">Book Space</button>
                        </div>
                    </div>
                    <div class="misc">
                        
                    </div>
                </div>
            </div>
        </div>

        <div id="popups" :class="{ closepopup: !popup}">
            <router-view> </router-view>
        </div>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'

export default {
    name: 'DashboardComponent',
    setup () {
        const state = reactive({
            count: 0,
            popup: false,
            focusApp: '',
            appData: [],
            search: '',
        }) 

        function openPopups(app) {
            state.focusApp = app

            state.popup = true
        }

        function closePopups() {
            state.popup = false;
            state.appData = [];
        }

    
        return {
            ...toRefs(state), 
            openPopups,
            closePopups,
        }
    }
}
</script>

<style lang="css" scoped>
    #dashboard {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        overflow: hidden;
        background-color: rgb(255, 255, 255);
        position: relative;
    }

    .container {
        width: 90%;
        height: 100%;
    }

    .header {
        width: 100%;
        height: 6%;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    .nameplate {
        height: 30px;
        margin-right: 17px;
        background-color: var(--clr--secondary);
        position: relative;
        display: flex;
        justify-content: center;
        border-radius: 5px;
    }

    .namepic {
        height: 35px;
        width: 35px;
        border-radius: 50%;
        background-color: var(--clr--primary);
        position: absolute;
        top: 50%;
        left: 100%;
        transform: translate(-50%, -50%);
    }

    .hi {
        margin-left: 10px;
        margin-right: 30px;
        line-height: 200%;
        color: var(--clr--light);
        font-weight: bolder;
    }

    .dashboard-grid {
        width: 100%;
        height: 94%;
        display: grid;
        padding-bottom: 1.5%;
        column-gap: 1.5%;
        row-gap: 3%;
        grid-template-columns: 0.31fr 0.40fr 0.29fr;
        grid-template-rows: 0.56fr 0.44fr;
    }

    .dashboard-grid > * {
        border-radius: 30px;
        padding: 10% 8%;
    }

    .luggage {
        background-color: var(--clr--light);
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

    .actions {
        margin-top: 7%;
        display: flex;
        justify-content: center;
        height: 15%;
    }

    button {
        width: 45%;
        height: 100%;
        cursor: pointer;
        border-radius: 10px;
    }

    .history {
        margin-right: 5%;
        border: 2px solid var(--clr--secondary);
        color: var(--clr--secondary);
        font-weight: bold;
    }

    .history:hover {
        background-color: var(--clr--secondary);
        color: var(--clr--light);
    }

    .bookings {
        border: 2px solid var(--clr--primary);
        color: var(--clr--primary);
        font-weight: bold;
    }

    .bookings:hover {
        background-color: var(--clr--primary);
        color: var(--clr--light);
    }

    .transport {
        background-color: var(--clr--light);
    }

    .status-icon {
        height: 15px;
        width: 15px;
        border-radius: 50%;
        border: none;
        background-color: var(--clr--primary);
        margin-left: 30%;
    }

    .sidebar {
        background-color: var(--clr--light);
        grid-column: 3/4;
        grid-row: 1/3;
    }

    .grid-group {
        grid-column: 1/3;
        display: grid;
        grid-template-columns: 0.6fr 0.4fr;
        padding: 0;
        column-gap: 2%;
    }

    .tradefair {
        padding: 5% 7%;
        background-color: var(--clr--light);
        border-radius: inherit;
    }

    .trade-actions {
        margin-top: 3%;
        display: flex;
        justify-content: center;
        height: 17%;
        padding: 0 10%;
    }

    .misc {
        padding: 10% 10%;
        background-color: var(--clr--light);
        border-radius: inherit;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    #popups {
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .5);
        position: absolute;
    }

    .pop {
        position: absolute;
        width: 65%;
        height: 75%;
        background-color: var(--clr--light);
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 20px;
        padding: 2%;
        overflow-y: scroll;
    }

    .close {
        position: absolute;
        right: 0;
        top: 0;
        margin: 2.5% 3%;
        cursor: pointer;
    }

    .closepopup {
        display: none;
    }

    .search {
        position: absolute;
        left: 0;
        top: 0;
        margin: 2% 3%;
        cursor: pointer;
        height: 5%;
        border: none;
        border-bottom: .5px solid var(--clr--dark);
        background-color: var(--clr-light);
        width: 30%;
        color: var(--clr--dark);
    }

    .search:focus, .search:active {
        outline: none;
    }

    .popup-table {
        margin: 5% 0;
        height: 0;
    }

    .popup-table thead td {
        height: 50px;
    }

    .popup-table tbody tr {
        height: 50px;
        cursor: pointer;
    }

    .popup-status {
        display: flex;
        justify-content: center;
        align-items: center;
        height: inherit;
    }

    .table-title {
        position: absolute;
        left: 50%;
        top: 0;
        margin: 2.5% 0;
    }

    .else {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: bold;
        font-size: 1.2rem;
        text-align: center;
        color: rgba(200, 0, 0, 1);
    }

    .extra {
        font-size: 3rem;
    }
</style>